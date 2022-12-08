import React from 'react';
import { Button } from 'react-bootstrap';
import PropTypes from 'prop-types';
import '../css/know-your-agency.css';

const propTypes = {
  Reset: PropTypes.func.isRequired
};

class ButtonFeatures extends React.Component {
  constructor(props) {
    super();
  }

  render() {
    return(
      <Button bsStyle="primary" bsSize="large" block onClick={this.props.Reset} className="know-your-agency-center-button">
        Reset Filter
      </Button>
    )
  }
}

ButtonFeatures.propTypes = propTypes;

export default ButtonFeatures;
