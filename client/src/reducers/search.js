import initialState from './initialState';
import {SEARCH_AGENCY} from '../actions/actionTypes';
const helpers = require('../helpers.js');

export default function searchReducer(state = initialState.search, action) {
  switch (action.type) {
    case SEARCH_AGENCY:
      let relationships = helpers.retrieveAgencyRelationships(action._id);
      return {...state, agency: action._id, agencyRelationships: relationships}
    default:
      return state;
  }
}
