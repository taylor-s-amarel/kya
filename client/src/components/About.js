import React from 'react';
import '../css/know-your-agency.css';

const About = () => (
  <div className="know-your-agency-about">
    <h2>About The Project</h2>
    <p>
      Hong Kong is home to over <b>1,400</b> domestic worker employment agencies - more agencies
      than Mcdonalds, 7-11, and Starbucks combined. Research has shown that over <b>70%</b> of agencies are
      known to be operating illegally <sup><a href=" http://www.scmp.com/news/hong-kong/law-crime/article/2093836/study-finds-hong-kong-domestic-helpers-subjected-employment">[1]</a></sup>.
      We have created this tool to better visualize the conflicts and caveats that should not
      exist in an ethical and competitive industry.
    </p>
    <p>
      The research and visualization tool shows:
    </p>
    <ul>
      <li>
        <b>22%</b> of agencies share the exact same address and room number with another agency.
        Address sharing between agencies is highly suspicious.
      </li>
      <li>
        In fact, there exists a cluster with <b>17</b> agencies all sharing the exact same address
      </li>
      <li>
        <b>16%</b> of agencies are located adjacent to a money lender or financial service provider.
        An ageny located near a money lender is suspicious because the agency
        may require domestic helpers to take out high-interest loans from the money lender.
      </li>
      <li>
        <b>26%</b> of agencies do not provide a phone number
      </li>
    </ul>
    <p>
      Despite such obvious concerns, the number of Employment Agencies in Hong Kong continues to increase.
    </p>
    <h2>Agency Visualizer</h2>
    <p>
      Using publicly scraped data, the Agency Visualizer tool illustrates potentially concerning relationships
      between employment agencies and other employment agencies as well as relationships between
      money lenders and employment agencies.
      The visualizer displays the following relationships that may exist between entities.
    </p>
    <p>
      <b>Exact Address:</b> Represents two entities located in the same building in the
      same room on the same floor. <br />

      <b>Bounding Address:</b> Represents two entities located
      in the same building on the same floor but in different rooms. <br />

      <b>Telephone:</b> Represents two entities sharing the same phone number. <br />

      <b>Email:</b> Represents two entities sharing the same email address. <br />

      <b>Fax:</b> Represents two entities sharing the same fax number. <br />
    </p>
    <h2>Agency Search</h2>
    <p>
      {'The Agency Search tool provides a more detailed view of each employment agency\'s information, ' +
      'including a textual view of the relationships displayed in the Agency Visualizer.'}
    </p>
  </div>
)

export default About;
