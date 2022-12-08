'use strict';

const express = require('express');
const helpers = require('./helpers.js');

const app = express();
const port = process.env.PORT || 5000;

app.get('/api/agencyData', (req, res) => {
  let fields = Object.keys(req.query).map(function(key) {
    return req.query[key];
  });
  console.time('helper.retrieveGraphData');
  let data = helpers.retrieveGraphData(fields);
  console.timeEnd('helper.retrieveGraphData');
  res.send(data);
});

app.get('/api/agencyDetail', (req, res) => {
  let data = helpers.retrieveAgenciesDetails();
  res.send(data);
});

app.get('/api/agencyRelationships', (req, res) => {
  let _id = req.query["_id"]
  let data = helpers.retrieveAgencyRelationships(_id);
  res.send(data);
});

app.listen(port, () => console.log(`Listening on port ${port}`));
