import { connect } from 'react-redux'
import Detail from '../components/Detail';

const mapStateToProps = state => {
  return {
    agency: state.searchReducer.agency
  };
}

export default connect(mapStateToProps)(Detail);
