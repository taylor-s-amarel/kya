import { connect } from 'react-redux'
import ButtonFeatures from '../components/ButtonFeatures';
import {resetGraph} from '../actions/visualization.js';

const mapDispatchToProps = dispatch => {
  return {
    Reset: () => {
      dispatch(resetGraph());
    }
  }
}

export default connect(null, mapDispatchToProps)(ButtonFeatures);
