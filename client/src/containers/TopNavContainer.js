import { connect } from 'react-redux'
import TopNav from '../components/TopNav';
import SelectPage from '../actions/select.js';

const mapDispatchToProps = dispatch => {
  return {
    resetState: () => {
      dispatch(SelectPage());
    }
  }
}

export default connect(null, mapDispatchToProps, null, {
  pure: false
})(TopNav);
