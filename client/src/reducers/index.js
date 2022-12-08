import visualizationReducer from './visualization.js';
import searchReducer from './search.js';
import selectReducer from './select.js';
import {SELECT_PAGE} from '../actions/actionTypes';
import { combineReducers } from 'redux';


const appReducer = combineReducers({
  visualizationReducer,
  searchReducer,
  selectReducer
});

const rootReducer = (state, action) => {
  if (action.type === SELECT_PAGE) {
    state = undefined;
  }
  return appReducer(state, action);
}

export default rootReducer;
