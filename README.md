# itinerary-optimizer

### Description
Itinerary-optimizer is a cli tool that take a list of locations and generates a word doc itinerary of the optimal order to visit them in.
This project is inspired by an operational painpoint of an NGO that needs to pick up a car and volunteers before going to a client. The full project was written in ~24h.

### Installation
1. Set up or find an OSRM server for the area the locations are located in. Instructions on how to run your own OSRM server can be found in the [Quick Start guide for Project-OSRM backend](https://github.com/Project-OSRM/osrm-backend). 
2. Create a csv file with the locations you need to visit, with the format specified below.  
3. Clone this project
4. Run `python -m optimizer.main`

#### CSV format
The expected columns are as follows:

Street | City | Country | PostalCode | Mandatory | Role | RouteRestriction | nearestIntersection
--- | --- | --- | --- |--- |--- |--- |---
Street address (i.e. 10 King's College Rd) | City (i.e. Toronto) | Country (i.e. Canada) | Postal Code |  Does the route need to include this location? (True/False) *(still to be implemented)* | Location annotation (i.e. car pickup) | (start) if starting point | Closest major intersection *(still to be implemented)*
