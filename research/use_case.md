# Use Case Definition

**This project is an AI-powered decision support tool for used-car buyers. It helps users evaluate a vehicle before purchase, understand the main risks, and ask the right questions to the seller.**

The tool would produce a structured report for a specific car model or listing, covering:
* Typical maintenance needs and common failure points
* Known reliability concerns and how to estimate whether they are likely to affect the specific vehicle
* Features, model years, trims, and equipment to prefer or avoid
* Checks that compare a concrete listing against the known model-level risks and strengths
* Practical questions to ask the seller before buying

The main target users are:
* Private buyers who want a low-cost or one-off report before purchasing
* Dealerships that want to minimize the risk in their purchases and have a repeatable advisory tool for sales staff or customer support

The data used for this analysis includes:
* Used-car market structure and transaction volumes
* Reliability and aftersales claim statistics
* Vehicle availability by age and mileage
* Depreciation trends
* Emissions rules and low-emission-zone restrictions that affect vehicle usability

Why this use case is timely:
* Low Emission Zones are forcing vehicle replacement in many European cities
* A large share of buyers still lacks confidence in car knowledge and buying processes
* The market is fragmented, making expert-style guidance valuable and difficult to scale manually
* AI can make personalized purchase support much cheaper than traditional inspection or advisory services

Important product principles:
* The output must be explainable and transparent about its sources
* The tool should support, not replace, the buyer's final decision
* It should include confidence levels or clear warnings when the data is incomplete
* Expert human feedback would be useful during the development and early rollout phases

The product should be designed as an MVP first, with a narrow and high-value scope. The first version can focus on a limited set of popular models or markets, then expand as the knowledge base grows.

Possible expansion ideas:
* Direct comparison of multiple listings
* Integration with repair cost estimates and maintenance planning
* Checklist generation for in-person inspection or test drive
