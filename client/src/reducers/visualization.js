import initialState from './initialState';
import {FILTER_GRAPH, ZOOM_NODE, RESET} from '../actions/actionTypes';
const helpers = require('../helpers.js');

export default function visualizationReducer(state = initialState.visualization, action) {
  switch (action.type) {
    case FILTER_GRAPH:
      let currentFilter = state.filter.slice();
      let index = currentFilter.indexOf(action.filter);
      if (index !== -1) {
        currentFilter.splice(index, 1);
      } else {
        currentFilter.push(action.filter);
      }
      let data = helpers.retrieveGraphData(currentFilter);
      return {zoom: "", filter: currentFilter, data, graph: helpers.formatNetworkData(data), center: false}
    case ZOOM_NODE:
      return {...state, zoom: action._id, center: false};
    case RESET:
      if (state !== initialState.visualization) {
        return {...state, zoom: "", data: initialState.visualization.data, filter: initialState.visualization.filter, graph: helpers.formatNetworkData(helpers.retrieveGraphData(['Exact Address', 'Bounding Address', 'Telephone', 'Email', 'Fax']))};
      } else {
        return state;
      }
    default:
      return state;
  }
}
