import initialState from './initialState';
import {SELECT_PAGE} from '../actions/actionTypes';

export default function selectReducer(state = initialState, action) {
  switch (action.type) {
    case SELECT_PAGE:
      return state
    default:
      return state;
  }
}
