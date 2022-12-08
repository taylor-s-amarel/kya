import React, { Component } from 'react';
// import AccessRestrictor from './AccessRestrictor';
import TopNavContainer from '../containers/TopNavContainer';
import Filter from './Filter';
import Contact from './Contact';
import DetailContainer from '../containers/DetailContainer';
import About from './About';
import TermsOfService from './TermsOfService';
import { Route } from 'react-router-dom';

class App extends Component {
  constructor(props) {
    super();
  }

  render() {
    // const accessAllowed = JSON.parse(
    //   window.localStorage.getItem('accessAllowed')
    // );

    return (
        <div>
          <TopNavContainer />
          <div className="know-your-agency-content">
            <Route path="/Visualizer" component={Filter} />
            <Route path="/Search" component={DetailContainer} />
            <Route path="/Contact" component={Contact} />
            <Route path="/TermsOfService" component={TermsOfService} />
          </div>
          {this.props.location.pathname === "/" ? <About /> :<p></p>}
        </div>
      )
  }
}

export default App;
