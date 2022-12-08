import React from 'react';
import PropTypes from 'prop-types';
import '../css/know-your-agency.css';

const propTypes = {
  data: PropTypes.object.isRequired
};

const Information = ({data}) => (
  <div className="know-your-agency-detail">
    <h3>
      {data.isAccredited ? data.english_name + " - (Accredited Employment Agency)" : data.english_name}
      {data.isAccredited ? <sup>
                            <a href="https://polohk.org/">[1]</a>
                           </sup> : <span></span>}
    </h3>
    <h3>{data.chinese_name}</h3>
    <p><strong>District:</strong></p>
    <p>{data.district}</p>
    <p><strong>Address:</strong></p>
    <p>{data.original_address}</p>
    {data.email ?<div><p><strong>Email:</strong></p><p>{data.email}</p></div>:<span></span>}
    {data.fax ?<div><p><strong>Fax:</strong></p><p>{data.fax}</p></div>:<span></span>}
  </div>
)

Information.propTypes = propTypes;

export default Information;
