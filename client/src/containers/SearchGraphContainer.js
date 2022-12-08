import { connect } from 'react-redux'
import Search from '../components/Search';
import {zoomOnNode} from '../actions/visualization.js';

const mapStateToProps = state => {
  return {
    data: state.visualizationReducer.data
  };
}

const mapDispatchToProps = dispatch => {
  return {
    selectAgency: id => {
      dispatch(zoomOnNode(id));
    }
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Search);
