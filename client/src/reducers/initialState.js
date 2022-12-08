const helpers = require('../helpers.js');

export default {
  select: {
  },
  search: {
    data: helpers.retrieveAgenciesDetails(),
    agency: "",
    agencyRelationships: {}
  },
  visualization: {
    zoom: "",
    data: helpers.retrieveGraphData(['Exact Address', 'Bounding Address', 'Telephone', 'Email', 'Fax']),
    filter: ['Exact Address', 'Bounding Address', 'Telephone', 'Email', 'Fax'],
    graph: helpers.formatNetworkData(helpers.retrieveGraphData(['Exact Address', 'Bounding Address', 'Telephone', 'Email', 'Fax']))
  }
}
