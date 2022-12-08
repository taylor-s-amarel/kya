import { connect } from 'react-redux'
import Search from '../components/Search';
import searchForAgency from '../actions/search.js';

const mapStateToProps = state => {
  return {
    data: state.searchReducer.data
  };
}

const mapDispatchToProps = dispatch => {
  return {
    selectAgency: id => {
      dispatch(searchForAgency(id));
    }
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Search);
