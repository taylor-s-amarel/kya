import React from 'react';
import { render } from 'react-dom'
import { createStore } from 'redux'
import rootReducer from './reducers'
import './css/index.css';
import registerServiceWorker from './registerServiceWorker';
import Root from './components/Root'
const store = createStore(rootReducer,
              window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
            );
render(
  <Root store={store} />,
  document.getElementById('root')
)
registerServiceWorker();
