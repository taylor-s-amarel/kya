import { connect } from 'react-redux'
import Toggle from '../components/Toggle';
import {filterGraph} from '../actions/visualization.js';

const mapStateToProps = state => {
  return {
    activeFilters: state.visualizationReducer.filter
  };
}

const mapDispatchToProps = dispatch => {
  return {
    selectFilter: name => {
      dispatch(filterGraph(name));
    }
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Toggle);
