import React, { Component } from 'react';
import { FormControl, Button } from 'react-bootstrap';
import { Redirect } from 'react-router-dom'
import '../css/know-your-agency.css';

class AccessRestrictor extends Component  {
  constructor(props, context) {
    super(props, context);
    this.state = {
      accessAttempted: false,
      value: '',
    };
  }

  onSubmit = (e) => {
    if(e) e.preventDefault();
    const accessCode = this.state.value;
    if (accessCode === 'KnowYourAgency2042') {
      window.localStorage.setItem('accessAllowed', true);
      window.location.reload();
    } else {
      this.setState({ accessAttempted: true });
    }
  }

  handleChange = (e) => {
    this.setState({ value: e.target.value });
  }

  render() {
    const { accessAttempted, value } = this.state;
    return (
      <form className="access-restrictor__form" onSubmit={this.onSubmit}>
        <div className="access-restrictor__container">
          <div className="access-restrictor__form-content">
            <FormControl
              bsSize="large"
              className="access-restrictor__input"
              onChange={this.handleChange}
              placeholder="Enter password for access"
              type="text"
              value={value}
            />
            <Button
              bsStyle="primary"
              className="access-restrictor__button"
              type="submit"
            >
              Submit
            </Button>
          </div>
          {accessAttempted && (
            <p className="access-restrictor__incorrect-password">
              Incorrect password. Please request a password by emailing knowyouragency@gmail.com.
            </p>
          )}
        </div>
      </form>
    )
  }
}

export default AccessRestrictor;