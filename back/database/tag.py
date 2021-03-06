# Author Nagai Ryusei - fix import
# Author Sakai Atsuya - all except Nagai's part
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from .model import Tag
#from database import db
from . import db

def insert_tag(user_id, tag_name):
    tag_ref = db.collection(u'Tag')
    tag = Tag(user_id, tag_name)
    tag_ref.add(tag.to_dict())
    return

def get_tags(user_id):
    tags = []
    tag_ref = db.collection(u'Tag').where(u'user_id', u'==', user_id)
    tag_docs = tag_ref.stream()
    print("tag_docs: ", tag_docs)
    for tag_doc in tag_docs:
        tag_name = tag_doc.to_dict()['tag_name']
        tags.append({
            'tag_id': tag_doc.id,
            'tag_name': tag_name
            })
    print("tags: ", tags)
    return tags

def delete_tag(user_id, tag_name):
    tag_ref = db.collection(u'Tag').where(u'user_id', u'==', user_id).where(u'tag_name', u'==', tag_name)
    tag_docs = tag_ref.stream()
    for tag_doc in tag_docs:
        db.collection(u'Tag').document(tag_doc.id).delete()
    return

def exists(user_id, tag_name):
    exist_flag = 0
    tag_ref = db.collection(u'Tag').where(u'user_id', u'==', user_id).where(u'tag_name', u'==', tag_name)
    tag_docs = tag_ref.stream()
    for _ in tag_docs:
        exist_flag = 1
    return exist_flag
