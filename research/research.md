# Use Case Discovery

**AI tool that supports the purchase of used cars.**
* Informs about questions the purchaser should ask the seller
* About the process after the purchase

Given a model, returns a report about:
* Required maintenance
* Known reliability concerns and how to estimate the current status
* Features to avoid and to look for (model year, pre/post restyling, interesting versions and optional equipment...) and how to identify them
* Checks concrete vehicle postings against this information, compares them

Target audience:
* Dealerships: suscription or cost per report
* Private users: very low cost per report or ads-based revenue

Necessary data:
* Used car sales vs total or new
* Statistics of aftersales claims
* Distribution of availability vs age and mileage
* Depreciation curves

To build a stronger case (why the project makes sense now):
* Implementation of Low Emissions Zones in EU forces vehicle replacement
* Still early adoption, biggest impact yet to come


# Sector trends

## State of the Art
Historical data:
* Used cars represent around 70% of all yearly transactions in Europe
* Below 1/3 of citizens estimate that they have enough knowledge about cars or the trading process. As a result, 25% believe they have been victims of unfair practices
* Aproximately 60% of the purchases are through professional dealerships. 41% of those vehicles present a problem within the first year.
    * 40% of them (16% of the total) already within the first month.
    * Only 27% manage to have them covered by a guarantee (11% of the total)
* Average cost of a claim: 675 €

Emissions Milestones and Low Emissions Zones:
* Cars newer than average are already starting to be excluded
    * The average vehicle age at the EU is 12.3 years (manufacture date around March 2014)
    * The most restrictive LEZs ban diesel cars before Euro 6 (release after September 2015)
* Euro 7 to be introduced in December 2026
    * Likely to trigger stricter exclusions on existing vehicles
* Only 24% of europeans (+100 million) currently live in a LEZ, but 70% live in urban areas (+300 million)
    * High probability of rapid adoption and impact on millions, specially in Eastern Europe (older vehicles and fewer LEZ to date)

See dashboard or data for details

## Opportunities
Several on-site vehicle inspection/test-drive/reporting services, at prices around 300 € per vehicle. 
Downside: in most cases, the buyer has to choose the vehicle first, then hire these services  
Examples: https://iautomato.de/en (also offers vehicle selection advice for 90€), https://www.carspector.de/, https://needcarhelp.es/

https://www.meistercheck.de/ratgeber Offers buyer support in the same direction as this proposal, but in form of checklists, articles... no sign of personalization or AI implementation

## AI Adoption Signals
Many services focusing on the sales side of the business (displaying products, gaining customers, contact with customers, pricing...)
Examples: https://carpilot.ai/de, https://www.carmar.digital/autohausgpt/, 
https://www.scayle.com/apparel-retail-ai/, https://impel.ai/, https://www.podium.com/

https://www.vettx.com focused on finding and pricing vehicles

No tool found that guides the purchasing based on the technical aspects of the vehicles

## Risks
* Omission of relevant common issues when generating a report (potential repair costs if problems detected later)
* Hallucination of potential issues (missing interesting opportunities)
* Hallucination of interesting features (disappointment of the customers)
* Bias of the used LLMs in favour of or against certain manufacturers and models and their countries of origin, certain technologies...


# Sources

## General Data
* https://commission.europa.eu/publications/study-second-hand-cars-market_en
* https://www.best-selling-cars.com/europe/2025-full-year-europe-car-sales-per-eu-uk-and-efta-country

## Depreciation
* https://www.autoexpress.co.uk/tips-advice/359491/car-depreciation-explained-future-residual-values-and-how-theyre-calculated
* https://www.bls.gov/opub/mlr/2024/highcharts/data/autos-chart-1.stm
* https://motorway.co.uk/sell-my-car/guides/car-depreciation-guide
* https://www.carwow.co.uk/car-valuation/guides/how-much-do-cars-depreciate-per-year#gref

## Low Emission Zones, Emissions, Ban Combustion
* https://link.springer.com/article/10.1186/s12544-025-00749-2
* https://www.rac.co.uk/drive/advice/emissions/euro-emissions-standards/