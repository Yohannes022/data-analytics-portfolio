## Research Design, Methodology, and Data-Use Considerations

### 1. Initial Research Plan

The original objective of this project was to investigate Ethiopia's export performance and understand how its export composition and international trading relationships have evolved over time.

The initial research plan focused on answering five questions:

1. How has the value of Ethiopia's merchandise exports changed over time?
2. Which product categories contribute most to export earnings?
3. Which destination markets account for the largest shares of exports?
4. How concentrated or diversified are Ethiopia's export products and destination markets?
5. What historical patterns, risks, and potential opportunities can be identified from the available trade data?

The initial plan proposed using UN Comtrade as the primary source because it provides internationally reported merchandise trade statistics organized by reporting country, trading partner, product classification, trade flow, and reporting period.

### 2. Proposed Analytical Methods

The following methods define the intended analytical framework. They are planned methods, not completed findings.

| Analytical area | Proposed methods |
|---|---|
| Data understanding | Source inspection, metadata review, data dictionaries, classification checks |
| Data validation | Missing-value analysis, duplicate detection, range checks, consistency checks |
| Data preparation | Filtering, data type conversion, aggregation, harmonization of product classifications |
| Export trends | Annual export values, year-over-year growth, compound annual growth rate |
| Product analysis | Product contribution, product shares, top-product analysis |
| Market analysis | Destination-market shares, leading trading partners, market changes |
| Concentration | Herfindahl-Hirschman Index (HHI), top-N product and destination shares |
| Diversification | Product and destination distribution, changes in concentration over time |
| Volatility | Annual changes and variability in export values |
| Visualization | Time-series charts, rankings, composition charts, concentration trends |
| Interpretation | Evidence-based findings, limitations, risks, and potential opportunities |

The calculations and analytical methods will be selected and documented according to the structure, coverage, and quality of the data actually obtained.

### 3. Data Source Review and Restrictions

Before collecting the dataset, the project reviewed the official UN Comtrade documentation, API documentation, subscription information, and license agreement.

This review identified two important considerations.

**API access and technical restrictions**

UN Comtrade provides different API services with different access requirements and limits.

- The Public API provides data previews of up to 500 rows without a subscription key.
- Other API services require a subscription key.
- Registered free accounts have access to additional services subject to published request, record, and rate limits.
- Larger-scale downloads, background processing, and bulk files have additional subscription requirements.

These restrictions must be considered when selecting the data extraction strategy and defining the research period and level of detail.

**Licensing and redistribution restrictions**

The UN Comtrade license agreement states that its content may be protected by copyright and restricts copying, downloading, redistribution, publication, and commercial exploitation without prior written permission, except where expressly permitted by applicable law.

Consequently:

- Public accessibility does not automatically mean unrestricted redistribution.
- Downloading data for analysis does not automatically grant permission to publish the downloaded files.
- Transforming data does not automatically establish permission to redistribute the resulting dataset or analytical outputs.
- Attribution alone does not replace the need for permission where permission is required.

Official references:

- [UN Comtrade License Agreement](https://comtradeplus.un.org/LicenseAgreement)
- [UN Comtrade API Documentation](https://comtradeplus.un.org/en/api-docs)
- [UN Comtrade Subscription and Access Limits](https://comtradeplus.un.org/en/subscriptions)

### 4. Revised Research and Implementation Plan

Following the source review, the project will use a source-first approach rather than proceeding directly to bulk data collection.

The revised implementation plan is:

**Step 1 — Confirm data availability**

- Investigate Ethiopia's available export reporting periods.
- Examine available product classifications and their editions.
- Identify the available partner, product, trade-value, and quantity fields.
- Determine whether the required level of detail can be accessed through the available API services.

**Step 2 — Confirm permitted data use**

- Review the applicable license terms before downloading data.
- Determine whether the intended research, analytical outputs, and public GitHub presentation are permitted.
- Seek clarification or written permission from the relevant data provider where necessary.
- Record the applicable conditions and any restrictions.

**Step 3 — Select the appropriate data strategy**

If the required access and publication permissions are confirmed, UN Comtrade may be used as the primary source.

If the restrictions prevent the intended use, alternative sources will be evaluated. Any replacement source must have verifiable provenance, sufficient coverage, suitable metadata, and licensing conditions compatible with the project's intended publication.

Potential alternatives will be assessed individually rather than assumed to be unrestricted.

**Step 4 — Implement a reproducible analytical workflow**

Once a suitable source is confirmed, implement the data acquisition, validation, preparation, analysis, and visualization stages using Python.

The project will keep data retrieval separate from analytical processing so that the workflow can be reproduced without unnecessarily distributing source data.

### 5. Data Management and Publication Policy

The project will distinguish between source data, analytical code, and research outputs.

| Material | Publication approach |
|---|---|
| Original downloaded data | Keep private unless redistribution is expressly permitted |
| Processed copies of source records | Do not publish without confirming permission |
| API keys and credentials | Never commit to GitHub |
| Data retrieval scripts | Publish where permitted, without embedded credentials |
| Data dictionaries and methodology | Publish where permitted |
| Analytical code and calculations | Publish, subject to applicable source restrictions |
| Charts, tables, and derived indicators | Publish only after confirming the applicable permissions |
| Research findings and interpretation | Publish with appropriate attribution and qualifications |

The repository will not contain restricted raw data, unauthorized extracts, API credentials, or other material that cannot lawfully be shared.

Where source data cannot be redistributed, the project will document the source, retrieval procedure, relevant metadata, and the steps needed for an authorized user to reproduce the analysis.

### 6. Research Integrity and Limitations

The analysis will avoid assuming that export concentration, diversification, growth, or decline exists before examining the evidence.

The project will also account for potential limitations, including:

- Differences in reporting practices between countries.
- Missing or revised trade records.
- Changes in product classification systems.
- Differences between reported exports and partner-reported imports.
- Confidential or aggregated trade records.
- Differences in valuation, currency, and quantity units.
- Incomplete reporting periods and changes in source coverage.

All findings will be interpreted in the context of the available data and its limitations.

### 7. Current Project Status

**Current phase: Research design and source validation.**

The repository structure and Python analysis environment have been established. The project has identified its initial research questions, proposed analytical methods, and reviewed the primary source's access and licensing conditions.

Data collection and statistical analysis have not yet been completed.

The next milestone is to confirm a suitable data source and its permitted use before beginning the actual data acquisition and analysis workflow.