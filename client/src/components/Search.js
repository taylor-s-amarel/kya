import React from 'react';
import {Typeahead} from 'react-bootstrap-typeahead';
import PropTypes from 'prop-types';
import '../css/know-your-agency.css';

const propTypes = {
  selectAgency: PropTypes.func.isRequired,
  data: PropTypes.object.isRequired,
  placeholder: PropTypes.string,
  class: PropTypes.string.isRequired,
  size: PropTypes.string
};

class Search extends React.Component {
  constructor(props) {
    super();
    this.state = {
      agencyNames: []
    };
    this.getAgencyNames = this.getAgencyNames.bind(this);
  }

  componentDidUpdate(prevProps) {
    // Typical usage (don't forget to compare props):
    if (this.props.data !== prevProps.data) {
      this.getAgencyNames(this.props.data);
    }
  }

  componentDidMount() {
    this.getAgencyNames(this.props.data);
  }

  /**
  * Processes names of agencies currently displayed in graph to be searchable. sets
  * state used in Typeahead to current agencies.
  * @param {Object} data - Data object including all agency relationship information.
  */
  getAgencyNames(data) {
    // Keep track of IDs already added
    let agencyNames = [];
    for (let _id in data) {
      let agency = data[_id];
      agencyNames.push(agency.english_name + " - " + _id);
    }
    // Make list display alphabetically
    agencyNames.sort(function(a, b) {
      a = a.substring(0, a.lastIndexOf(" -"));
      b = b.substring(0, b.lastIndexOf(" -"));
      if(a < b) return -1;
      if(a > b) return 1;
      return 0;
    })
    this.setState({agencyNames: agencyNames});
  }

  render() {
    return(
      <Typeahead className={this.props.class}
        placeholder={this.props.placeholder}
        emptyLabel=""
        ref={(typeahead) => this.typeahead = typeahead}
        bsSize={this.props.size}
        onChange={(selected) => {
          if (selected[0]) {
            let split = selected[0].split("-");
            let agencyId = split[split.length - 1].trim();
            this.props.selectAgency(agencyId);
          }
          if (selected.length) {
            this.typeahead.getInstance().clear()
          }
        }}
        options={this.state.agencyNames}
      />
    )
  }
}

Search.propTypes = propTypes;

export default Search;
