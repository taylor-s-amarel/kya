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
    newAgency['address'] = agencyInformation['address'];
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
    return {};
  }
}

const hasAddressRelationship = (data, id) => {
  let agencyInformation = data[id];
  if (!agencyInformation) {
      return true;
  }
  let agencyRelationships = Object.keys(agencyInformation.relationships);
  if (agencyRelationships.includes('Exact Address') || agencyRelationships.includes('Bounding Address')) {
    return true;
  }
  return false;
}

const isAccredited = (id) => {
  let agencyInformation = allAgencies[id];
  if (!agencyInformation) {
    return false;
  }
  if (agencyInformation["isAccredited"]) {
    return true
  }
  return false;
}

const formatNetworkData = (data) => {
  let graph = {
    nodes: [],
    edges: []
  };

  const relationships = {"Exact Address": 0,
                       "Bounding Address": 1,
                       "Telephone": 2,
                       "Fax": 3,
                       "Email": 4};

  const edgeColors = ["#f45c42", "#3c843b", "#9445a0", "#db870a", "#0acddb"];


  // Keep track of IDs already added
  let usedIDs = {};

  Object.keys(data).forEach(function(key) {
    let agencyInformation = data[key];
    let nodeTitle = "<p>" + agencyInformation.english_name + "</p> <br />" +
                    "<p>Government ID: " + key + "</p>";
    if (hasAddressRelationship(data, key)) {
      nodeTitle += "<br /><p>" + agencyInformation.address + "</p>"
    }
    if (!usedIDs[key]) {
      if (isAccredited(key)) {
        graph["nodes"].push({id: key, title: nodeTitle, color: "#42f48c"});
      } else {
        graph["nodes"].push({id: key, title: nodeTitle});
      }
      usedIDs[key] = true;
    }
    Object.keys(agencyInformation.relationships).forEach(function(relationship) {
      let connectedAgencies = agencyInformation["relationships"][relationship];
      connectedAgencies.forEach(function(agency) {
        let agencyId = agency[0];
        let agencyName = agency[1];
        let nodeType = agency[2];
        let agencyAddress = agency[3];
        if (!usedIDs[agencyId]) {
          if (nodeType === "A") {
            let info = data[agencyId]
            if (info) {
              agencyAddress = data[agencyId]["address"];
            }
            let nodeTitle = "<p>" + agencyName + "</p> <br />" +
                    "<p>Government ID: " + agencyId + "</p>";
            if (hasAddressRelationship(data, agencyId)) {
              nodeTitle += "<br /><p>" + agencyAddress + "</p>"
            }
            if (isAccredited(agencyId)) {
              graph["nodes"].push({id: agencyId, title: nodeTitle, color: "#42f48c"});
            } else {
              graph["nodes"].push({id: agencyId, title: nodeTitle});
            }
          } else {
            let nodeTitle = "<p>" + agencyName + "</p> <br />" +
                    "<p>" + agencyAddress + "</p>";
            graph["nodes"].push({id: agencyId, title: nodeTitle, color: "rgb(219, 57, 57)"});
          }
          usedIDs[agencyId] = true;
        }
        let edgeColor = edgeColors[relationships[relationship]];
        if (!usedIDs[key + agencyId + relationship] && !usedIDs[agencyId + key + relationship]) {
          graph["edges"].push({from: key, to: agencyId, label: relationship, color: {color: edgeColor}});
          usedIDs[key + agencyId + relationship] = true;
        }
      })
    })
  });
  return graph;
}

module.exports = {
  retrieveGraphData,
  retrieveAgenciesDetails,
  retrieveAgencyRelationships,
  formatNetworkData
};
