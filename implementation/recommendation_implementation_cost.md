# Recommendation

Overall, the research suggests a strong opportunity for an AI assistant that helps used-car buyers compare listings, understand risks, and ask the right questions before purchase. The combination of market scale, buyer uncertainty, rising emissions pressure, and the lack of personalized buyer-side tools makes this a timely use case.

It is recommended to build this tool as an MVP first, because the market signal is strong, the use case is clear, and the initial scope can be kept focused.

## Implementation Steps And Timeline

| Step | Main activities | Duration |
|---|---|---:|
| 1. Scope and data definition | Confirm MVP features, define target users, identify required datasets, and choose the first supported car segments or markets. | 1 week |
| 2. Data collection and normalization | Gather used-car market data, depreciation data, reliability data, emissions rules, and model-specific vehicle information. Clean and structure the data. | 2-3 weeks |
| 3. Knowledge base and rules engine | Build the logic that turns model data into recommendations, red flags, and questions to ask the seller. | 2 weeks |
| 4. AI report generation | Connect the structured data with the LLM layer so it can produce clear, personalized purchase reports. | 2 weeks |
| 5. Frontend and user flow | Create a simple interface for car search, report generation, and report comparison against listings. | 2 weeks |
| 6. Testing and validation | Check accuracy, reduce hallucinations, test with real listings, and validate the output with car experts or experienced buyers. | 1-2 weeks |
| 7. Pilot launch | Release a limited beta to a small group of users or dealerships and collect feedback for iteration. | 1 week |

Total estimated MVP timeline: 9-13 weeks.

## Cost Estimate

The following is a rough cost estimate for development and early deployment from Germany, assuming a small MVP team and outsourced or freelance support:

| Cost item | Assumption | Estimated cost |
|---|---|---:|
| Product discovery and planning | Scope definition, data mapping, and MVP design | 1,500-4,000 EUR |
| Data acquisition and preparation | Manual sourcing, cleaning, enrichment, and structuring | 3,000-8,000 EUR |
| Development | Backend, prompt design, rule engine, frontend, and integration work | 12,000-30,000 EUR |
| Testing and validation | QA, expert review, correction cycles, and pilot support | 2,000-6,000 EUR |
| Initial deployment | Hosting, domain, monitoring, storage, and basic security setup | 200-800 EUR / month |
| AI usage | Model/API calls for report generation and comparison | 100-1,000 EUR / month at low-to-moderate usage |

Estimated MVP build budget: 18,500-48,000 EUR.

For a more polished commercial version with stronger automation, better coverage, and ongoing content maintenance, the budget should be expected to rise further.

## Indicative Price Per Report

Based on the research, the tool should be priced well below human inspection-style services, which are often around 300 EUR per vehicle, while still leaving room to cover AI usage, support, and product maintenance.

The suggestion is a hybrid pricing model:
* **Occasional/private users:** 14.99-29.99 EUR per report, or 4.99-9.99 EUR per report if the report page includes advertising or sponsored placements
* **Dealerships:** 4.99-12.99 EUR per report at volume, or a monthly subscription for frequent use, at around 99.99 EUR
* Premium reports with deeper listing comparison or more detailed model coverage could be priced above this range

As a starting point, 19.99 EUR per report is a reasonable MVP price for private users without ads, because it is low enough to feel accessible but high enough to signal value and support operating costs.

## Assumptions

* The tool generates decision support, not a legally binding inspection or guarantee.
* The first release is English-only.
* A human review step is available during the pilot phase to catch bad recommendations early.
* The company is operating in Germany and therefore plans for GDPR-compliant storage, logging, and hosting in an EU region.

## Possible Next Steps

1. Validate the highest-value target segment: private buyers, dealerships, or both.
2. Define the MVP scope in detail, specially the report content and format.
3. Build a small prototype.
4. Test the output with real listings and compare recommendations against expert judgment.
5. Estimate monetization more precisely, especially subscription pricing for dealerships and per-report pricing for private users.
6. If the prototype performs well, prepare a pilot with a limited user group and measure conversion, usage, and trust.
