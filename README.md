# Live Site
To view the live version of this project, please click [here](https://know-your-agency.herokuapp.com/).

# About The Project
A fantastic description of the project is available [here](https://www.scmp.com/news/hong-kong/hong-kong-law-and-crime/article/2155292/data-lays-bare-hidden-links-hong-kongs) by the South China Morning Post, Hong Kong's largest newspaper. 

Hong Kong is home to over **1,400** domestic worker employment agencies - more agencies than Mcdonalds, 7-11, and Starbucks combined. Research has shown that over **70%** of agencies are known to be operating illegally [[1]](http://www.scmp.com/news/hong-kong/law-crime/article/2093836/study-finds-hong-kong-domestic-helpers-subjected-employment). We have created this tool to better visualize the conflicts and caveats that should not exist in an ethical and competitive industry.

The research and visualization tool shows:

- **22%** of agencies share the exact same address and room number with another agency. Address sharing between agencies is highly suspicious.
- In fact, there exists a cluster with **17** agencies all sharing the exact same address
- **16%** of agencies are located adjacent to a money lender or financial service provider. An ageny located near a money lender is suspicious because the agency may require domestic helpers to take out high-interest loans from the money lender.
- **26%** of agencies do not provide a phone number
Despite such obvious concerns, the number of Employment Agencies in Hong Kong continues to increase.

# Agency Visualizer
Using publicly scraped data, the Agency Visualizer tool illustrates potentially concerning relationships between employment agencies and other employment agencies as well as relationships between money lenders and employment agencies. The visualizer displays the following relationships that may exist between entities.

- **Exact Address:** Represents two entities located in the same building in the same room on the same floor.
- **Bounding Address:** Represents two entities located in the same building on the same floor but in different rooms.
- **Telephone:** Represents two entities sharing the same phone number. 
- **Email:** Represents two entities sharing the same email address. 
- **Fax:** Represents two entities sharing the same fax number. 

# Agency Search
The Agency Search tool provides a more detailed view of each employment agency's information, including a textual view of the relationships displayed in the Agency Visualizer.

# Datasets
To view processed datasets used for the project, navigate to client --> src --> data. 
To view scraping code, navigate to the data-pipeline directory.
