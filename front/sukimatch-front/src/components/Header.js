import React from 'react';
import { NavLink } from 'react-router-dom';

const Header = () => {
  return (
  <header>
    <NavLink to="/" activeClassName="is-active" exact={true} >Home</NavLink>
    <NavLink to="/user" activeClassName="is-active" exact={true} >Mypage</NavLink>
    <NavLink to="/user" activeClassName="is-active" >Log in</NavLink>
    <NavLink to="/user/edit" activeClassName="is-active" >Edit</NavLink>
  </header>
  )
}

export default Header;