## Meta-Analysis Agent

### 1. Refine user'sresearch question

Many questions will be too vague or difficult to study using a meta-analysis.
In this step, the agent will help the user to make the research question specific and feasible. We need to be clear about:

* the relationship in question
* populations, interventions, comparators, outcomes (PICO framework?)
* develop testable hypothesis
* moderators

### 2. Develop a protocol

Before data collection, the agent will make sure we follow a protocol like [PRISMA](https://www.prisma-statement.org/), then define ..
* ... inclusion/exclusion criteria
    * e.g. type of study, type of statistic reported, sample size etc.
* ... how the effect size will be quantified \
+optionally with user feedback

### 3. Literature search

* initially just ArXive, Google Scholar, open access journals?
* define search strings
* criteria, e.g. pre-prints, theses, conference proceedings?
* documentation
    * date of search
    * exact search terms
    * filters
    * number of results from each database

### 4. Study selection

* first pass: screen titles and abstracts against inclusion/exclusion criteria
* second pass: screen full texts 
* create a PRISMA flow diagram
* inclusion criteria:
    * study design requirements
    * population characteristics
    * required statistical information
    * publication time frame
    * methodological quality thresholds?

### 5. Data extraction

Extract relevant data into tabular format
* study metadata (authors, year, journal, title, etc.)
* study design and methodology
* sample size and characteristics
* effect size + CI, p-value
* statistical tests / models used
    * outcome measures and their operationalisation
* moderators (e.g. type of study, setting, etc.)

### 6. Effect size calculation

* transform into common effect size metric (cohens d, odds ratio, risk ratio, correlation coefficient, b/beta, etc.)
* apply necessary transformations for analysis
* document conversion formulas / calculations
* handle dependent effect sizes appropriately (through moderators?)
* document all methods in detail for reproducibility

### 7. Assess study quality and risk of bias

Evaluate methodological quality:
* sample size adequate?
* blinding procedures when relevant?
* control for confounders?
* appropriate statistical analysis?
* are there standardised tools / checklists?

Assess publication bias:
* funnel plot
* egger's regression
* fail-safe N
* p-curve
* comparison of published and unpublished studies

### 8. Meta-analysis

* multilevel model
* moderator analyses using meta-regression
* sensitivity analyses
* chose software (python vs r?)

### 9. Reporting

* forest plots
* summary tables
* funnel plots
* meta-regression plots

### 10. Discussion

### 11. Transparency and reproducibility

* dataset and code
* acknowledge limitations
* PRISMA guidelines