import React from 'react';
import NetworkContainer from '../containers/NetworkContainer';
import ToggleContainer from '../containers/ToggleContainer';
import SearchGraphContainer from '../containers/SearchGraphContainer';
import ButtonFeaturesContainer from '../containers/ButtonFeaturesContainer';
import { Nav, NavItem } from 'react-bootstrap';
import '../css/know-your-agency.css';

class Filter extends React.Component {
  constructor(props) {
    super();
    this.generateToggles = this.generateToggles.bind(this);
  }

  /**
  * Function that creates all of the toggles within the filter.
  * Iterates trough filter object, and creates a toggle for each
  * key.
  * @param {Object} filter -- object containing all filter categories and items
  * @param {function} updateFilter -- function that updates state on click
  * @returns {HTML} -- HTML of toggles
  */
  generateToggles = () => {
    let filter = ['Exact Address', 'Bounding Address', 'Telephone', 'Email', 'Fax'];
    let toggles = [];
    let i = 0;
    filter.forEach(function(toggle) {
      toggles.push(<ToggleContainer eventkey={i++}
                      name={toggle} key={i}/>)
    })
    return (
      <div>
        {toggles}
      </div>
    )
  }

  render() {
    return (
      <div>
        <div className="know-your-agency-filter">
          <Nav bsStyle="pills" stacked activeKey={1}>
            <NavItem disabled>Filter</NavItem>
          </Nav>
          {this.generateToggles()}
          <SearchGraphContainer placeholder="Search Displayed Agencies" class="know-your-agency-search" />
          <ButtonFeaturesContainer />
          <div className="key-container">
            <div className="key-container">
              <div>
                <span className="agency-dot" />
                <p className="key">   = Employment Agency</p>
              </div>
              <div>
                <span className="accredited-agency-dot" />
                <p className="key">   = Accredited Employment Agency <sup><a href="https://polohk.org/">[1]</a></sup></p>
              </div>
              <div>
                <span className="money-lender-dot" />
                <p className="key">   = Money Lender /
                <p className="FSP">Financial Service Provider</p>
              </p>
              </div>
            </div>
            <div className="key-container">
              Zoom with mouse / trackpad scroll or navigation buttons
            </div>
          </div>
        </div>
        <NetworkContainer />
      </div>
    );
  }
}


export default Filter;
