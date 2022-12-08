import React from 'react';
import PropTypes from 'prop-types';
import '../css/know-your-agency.css';
import '../css/vis.min.css';
import Graph from 'react-graph-vis';

const propTypes = {
  data: PropTypes.object.isRequired,
  zoom: PropTypes.string.isRequired,
  graph: PropTypes.object.isRequired
};

const options = {
          "layout": {
            "improvedLayout": false
          },
          "interaction": {
            "hover": true,
            navigationButtons: true,
            keyboard: true,
            hideEdgesOnDrag: true,
            tooltipDelay: 200,
            dragNodes: false
          },
          "edges": {
            "arrows": {
              "to": {
                "enabled": false,
                "scaleFactor": 0.5
              }
            },
            "smooth": {
              "forceDirection": "none"
            },
          },
          "physics": {
            "timestep": 0.8,
            "minVelocity": 0.9,
            "solver": "forceAtlas2Based",
            "forceAtlas2Based": {
              "gravitationalConstant": -35,
              "avoidOverlap": 0,
            },
            "stabilization": {
              "enabled": false,
            }
          }
        };

class Network extends React.Component {
  constructor(props) {
    super();
    this.state = {
      display: false,
      graph: props.graph
    };
    this.setNetworkInstance = this.setNetworkInstance.bind(this);
  }

  /**
  * Sets zoom if agency searched for. Else zoom.
  * is searched for.
  * @param {Object} nextProps - props passed down from Filter.
  */
  componentWillReceiveProps(nextProps) {
    if (nextProps.zoom) {
      this.network.focus(nextProps.zoom, {scale: 2, locked: true});
    } else {
      this.setState({display: false}, () => {
        setTimeout(function() {
          this.setState({graph: nextProps.graph});
        }.bind(this), 10);
        setTimeout(function() {
          this.setState({display: true});
          this.network.fit();
        }.bind(this), 20);
      });
    }
  }

  /**
  * When DOM mounted, wait for graph to stabilize and then show container. Otherwise,
  * graph stabilizes after rendering and UX is terrible.
  */
  componentDidMount() {
    this.network.stabilize(100)
    setTimeout(function() {
      this.setState({display: true});
      this.network.fit();
    }.bind(this), 8000);
  }

  /**
  * Sets this.network to refer to the graph.
  */
  setNetworkInstance = nw => {
    // Intercept the click event
    nw.on("click", function (params) {
      // Check if you clicked on a node; if so, display the title (if any) in a popup
      nw.interactionHandler._checkShowPopup(params.pointer.DOM);
    });
    this.network = nw;
  };

  render() {
    return(
      <div className="know-your-agency-page-content-wrapper">
        <div className={this.state.display ? "hidden" : "loader"} />
        <div style={this.state.display ? {"display": "inline-block", "height": "100%", "width": "100%"} : {"visibility": "hidden"}}>
          <Graph className='know-your-agency-graph' graph={this.state.graph} options={options}
           getNetwork={this.setNetworkInstance} style={{"height": "85vh"}} />
        </div>
      </div>
    );
  }
}

Network.propTypes = propTypes;

export default Network;
