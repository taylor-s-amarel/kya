import { connect } from 'react-redux'
import Information from '../components/Information';

const mapStateToProps = state => {
  return {
    data: state.searchReducer.data[state.searchReducer.agency]
  };
}

export default connect(mapStateToProps)(Information);
