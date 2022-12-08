import { connect } from 'react-redux'
import Network from '../components/Network';

const mapStateToProps = state => {
  return {
    data: state.visualizationReducer.data,
    zoom: state.visualizationReducer.zoom,
    graph: state.visualizationReducer.graph
  };
}

export default connect(mapStateToProps)(Network);
