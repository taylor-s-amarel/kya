import { connect } from 'react-redux'
import Warning from '../components/Warning';
import searchForAgency from '../actions/search.js';

const mapStateToProps = state => {
  return {
    warnings: state.searchReducer.agencyRelationships
  };
}

const mapDispatchToProps = dispatch => {
  return {
    selectAgency: id => {
      dispatch(searchForAgency(id));
    }
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Warning);
