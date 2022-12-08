import React from 'react';
import SearchContainer from '../containers/SearchContainer.js';
import InformationContainer from '../containers/InformationContainer.js';
import WarningContainer from '../containers/WarningContainer.js';
import PropTypes from 'prop-types';
import '../css/know-your-agency.css';


const propTypes = {
  agency: PropTypes.string.isRequired
}

const Detail = ({agency}) => (
  <div>
  {agency ? <div>
              <InformationContainer />
              <WarningContainer />
            </div> :
            <div className="agency-search-container">
              <h1>Agency Search</h1>
              <SearchContainer size="large" placeholder="Search All Agencies" class="know-your-agency-detail-search" />
            </div>}
  </div>
)

Detail.propTypes = propTypes;

export default Detail;
