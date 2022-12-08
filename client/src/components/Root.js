import React from 'react'
import PropTypes from 'prop-types'
import { Provider } from 'react-redux'
import { BrowserRouter as Router, Route } from 'react-router-dom'
import App from './App'
import withTracker from './withTracker';

const Root = ({ store }) => (
  <Provider store={store}>
    <Router>
      <Route path="/" component={withTracker(App)} />
    </Router>
  </Provider>
)

Root.propTypes = {
  store: PropTypes.object.isRequired
}

export default Root
