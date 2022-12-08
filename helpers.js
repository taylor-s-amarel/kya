'use strict';

var agencyRelationships = require('./data/agencyRelationships.json');
var allAgencies = require('./data/allAgencies.json');

/**
* @description - Based on the requested fields, this function returns an object
* which includes the necessary data to render the agency visualization.
* @param {Array} relationshipsToInclude - Array containing strings of node relationships to include.
* @returns {Object} - Node data to be rendered.
*/
const retrieveGraphData = (relationshipsToInclude) => {
  let agencyData = Object.assign({}, agencyRelationships);
  let finalAgencies = {};
  Object.keys(agencyData).forEach(function(key) {
    let agencyInformation = agencyData[key];
    let newAgency = {};
    newAgency['_id'] = agencyInformation['_id'];
    newAgency['english_name'] = agencyInformation['english_name'];
    newAgency['relationships'] = {};
    Object.keys(agencyInformation.relationships).forEach(function(relationship) {
      if (relationshipsToInclude.includes(relationship)) {
        newAgency['relationships'][relationship] = agencyInformation["relationships"][relationship];
      }
    })
    if (Object.keys(newAgency.relationships).length) {
      finalAgencies[key] = newAgency;
    }
  });
  return finalAgencies;
}

const retrieveAgenciesDetails = () => {
  return allAgencies;
}

const retrieveAgencyRelationships = (_id) => {
  if (agencyRelationships[_id]) {
    return agencyRelationships[_id]['relationships'];
  } else {
    return null;
  }
}

module.exports = {
  retrieveGraphData,
  retrieveAgenciesDetails,
  retrieveAgencyRelationships
};
