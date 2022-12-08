import React from 'react';
import Switch from "react-switch";
import PropTypes from 'prop-types';
import '../css/know-your-agency.css';

const propTypes = {
  name: PropTypes.string.isRequired,
  selectFilter: PropTypes.func.isRequired,
  activeFilters: PropTypes.array.isRequired
};

class Toggle extends React.Component {
  constructor(props) {
    super();
    this.state = {
      activeFilters: ['Exact Address', 'Bounding Address', 'Telephone', 'Email', 'Fax']
    };
    this.handleToggleChange = this.handleToggleChange.bind(this);
  }

  static getDerivedStateFromProps(props, state) {
    return {activeFilters: props.activeFilters}
  }


  handleToggleChange = (selected) => {
    let currentFilter = this.state.activeFilters.slice();
    let index = currentFilter.indexOf(selected);
    if (index !== -1) {
      currentFilter.splice(index, 1);
    } else {
      currentFilter.push(selected);
    }
    this.setState({activeFilters: currentFilter}, () => {
      this.props.selectFilter(this.props.name)
    });
  }

  render() {
    return(
      <div className="know-your-agency-toggle">
        <label htmlFor="normal-switch">
          <Switch
            onChange={() => this.handleToggleChange(this.props.name)}
            checked={this.state.activeFilters.includes(this.props.name)}
            className="react-switch"
            id="normal-switch"
          />
          <span className="toggle-text">{this.props.name}</span>
        </label>
      </div>
    );
  }
}

// const Toggle = ({name, selectFilter, key, activeFilters}) => (
//   <div className="know-your-agency-toggle">
//     <label htmlFor="normal-switch">
//       <Switch
//         onChange={() =>
//           handleToggleChange(name);
//           selectFilter(name)}
//         checked={this.state.activeFilters.includes(this.props.name)}
//         className="react-switch"
//         id="normal-switch"
//       />
//       <span className="toggle-text">{this.props.name}</span>
//     </label>
//   </div>
// )

Toggle.propTypes = propTypes;

export default Toggle;
