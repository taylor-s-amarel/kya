import { ZOOM_NODE, FILTER_GRAPH, RESET } from './actionTypes';

export function zoomOnNode(_id) {
  return {type: ZOOM_NODE, _id}
}

export function filterGraph(filter) {
  return {type: FILTER_GRAPH, filter}
}

export function resetGraph() {
  return {type: RESET}
}
