import React from 'react';
import PropTypes from 'prop-types';
import { Alert } from 'react-bootstrap'
import '../css/know-your-agency.css';


const propTypes = {
  warnings: PropTypes.object.isRequired,
  selectAgency: PropTypes.func.isRequired
}

class Warning extends React.Component {
  constructor(props) {
    super();
    this.generateList = this.generateList.bind(this);
  }

  generateList(warnings, selectAgency) {
    let list = [];
    let id = 0;
    Object.keys(warnings).forEach(function(relationship) {
      for (let agency in Object.keys(warnings[relationship])) {
        if (warnings[relationship][agency][2] === "A") {
          list.unshift(<li key={id}><span className="know-your-agency-agency-name" onClick={() => {selectAgency(warnings[relationship][agency][0])}}>{warnings[relationship][agency][1]} - {warnings[relationship][agency][0]}</span> <br /><p>{relationship}: {warnings[relationship][agency][3]}</p></li>);
        } else {
          list.push(<li key={id}><span className="know-your-agency-ml-name">{warnings[relationship][agency][1]}</span><p>{relationship}: {warnings[relationship][agency][3]}</p></li>);
        }
        id++;
      }
    })
    return(
      <ul>
        {list}
      </ul>
    );
  }

  render() {
    return(
      <div>
        {Object.keys(this.props.warnings).length ?
          <div>
            <Alert className="know-your-agency-warning" bsStyle="info">
              <span>
                <span className="agency-square" />
                <p className="search-key">   = Employment Agency</p>
              </span>
              <span>
                <span className="money-lender-square" />
                <p className="search-key">   = Money Lender / Financial Service Provider</p>
              </span>
            </Alert>
            <Alert className="know-your-agency-warning" bsStyle="warning"><b>Suspicious Relationships:</b>
                {this.generateList(this.props.warnings, this.props.selectAgency)}
            </Alert>
          </div> : <Alert className="know-your-agency-warning" bsStyle="success">No suspicious relationships associated with this agency.</Alert>
        }
      </div>
    )
  }
}


Warning.propTypes = propTypes;

export default Warning;
