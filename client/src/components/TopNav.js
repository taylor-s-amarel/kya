import React from 'react';
import '../css/know-your-agency.css'
import PropTypes from 'prop-types';
import { LinkContainer } from 'react-router-bootstrap';
import { IndexLinkContainer } from 'react-router-bootstrap'
import { Nav, Navbar, NavItem } from 'react-bootstrap';

const propTypes = {
  resetState: PropTypes.func.isRequired
}

const TopNav = ({resetState}) => (
  <Navbar inverse fixedTop collapseOnSelect>
    <Navbar.Header>
      <Navbar.Toggle />
    </Navbar.Header>
    <Navbar.Collapse>
      <Nav pullRight className="know-your-agency-navbar-items">
        <IndexLinkContainer to="/" onClick={resetState}>
          <NavItem>Home</NavItem>
        </IndexLinkContainer>
        <LinkContainer to="/Visualizer" onClick={resetState}>
          <NavItem className="know-your-agency-navbar-items">Agency Visualizer</NavItem>
        </LinkContainer>
        <LinkContainer to="/Search" onClick={resetState}>
          <NavItem className="know-your-agency-navbar-items">Agency Search</NavItem>
        </LinkContainer>
        <LinkContainer to="/Contact" onClick={resetState}>
          <NavItem className="know-your-agency-navbar-items">
            Contact ✉
          </NavItem>
        </LinkContainer>
        <LinkContainer to="/TermsOfService" onClick={resetState}>
          <NavItem className="know-your-agency-navbar-items">
            Terms of Service
          </NavItem>
        </LinkContainer>
      </Nav>
    </Navbar.Collapse>
  </Navbar>
)

TopNav.propTypes = propTypes;

export default TopNav;
