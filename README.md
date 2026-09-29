# Spare Parts Analogue Selector

Decision-support system for selecting a similar existing spare-part product for new or low-history products.

## Project Overview

The Spare Parts Analogue Selector is a decision-support system that identifies a similar existing product for a new or low-history spare-part product.

The system compares product attributes, launch curves, category behaviour, failure behaviour, and promotional conditions.

It also provides similarity scores, confidence levels, edge-case warnings, analogue-based demand forecasting, forecast validation, and workload safety validation.

## Problem Statement

New spare-parts products often have little historical data.

Because of this, it can be difficult to estimate their demand and failure behaviour.

The system selects a similar existing product and provides an explanation of the similarity and confidence level.

The selected analogue can also be used as a reference for a six-month demand forecast.

## Objectives

- Select the best existing analogue for a product
- Compare multiple product characteristics
- Explain why an analogue was selected
- Provide a confidence level
- Detect near-tied analogue candidates
- Handle missing information
- Identify cases where no strong analogue exists
- Generate a six-month demand forecast
- Validate forecast error using MAE and RMSE
- Apply an 8-hour workload safety limit
- Compare the prototype with a simple baseline
- Perform automated validation checks
- Provide a professional decision-support dashboard

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib

## Project Structure

spare_parts_analogue_selector/

data/

Contains the project datasets.

src/

Contains forecasting and workload safety modules.

experiments/

Contains validation and testing experiments.

docs/

Contains project documentation.

app.py

Main Streamlit application.

requirements.txt

Contains the required Python libraries.

README.md

Project documentation.

## Datasets

The project uses four datasets:

- Products
- Failures
- Promotions
- Launch Curves

The datasets are connected using product_id.

## Analogue Selection

The prototype compares products using five factors:

- Product attributes: 30%
- Launch curve: 25%
- Category behaviour: 20%
- Failure behaviour: 15%
- Promotion conditions: 10%

The weighted similarity values are combined to select the best analogue.

## Confidence Levels

HIGH:

Similarity score is 80% or above.

MEDIUM:

Similarity score is between 60% and 79.99%.

LOW:

Similarity score is below 60%.

Low-confidence results require manual review.

Confidence can also be reduced when important information is missing.

## Edge-Case Handling

### No Strong Analogue

If the similarity score is below 60%, the system displays a warning and recommends manual review.

### Near-Tied Analogues

The system compares the best and second-best analogue.

If the difference is 2 percentage points or less, the system displays a manual-review warning.

### Missing Information

Missing numerical values are handled using median values.

Missing promotion information is handled using default values.

Missing information is detected before processing.

Confidence is reduced when important information is missing.

## Demand Forecast

The selected analogue's historical six-month demand pattern is displayed as an analogue-based forecast.

The forecast contains:

- Month 1
- Month 2
- Month 3
- Month 4
- Month 5
- Month 6

The Streamlit application displays the forecast as a table and line chart.

## Forecast Validation

A retrospective validation experiment was implemented to evaluate analogue-based demand transfer.

The validation excludes launch-curve demand from analogue selection and uses it only for retrospective forecast evaluation.

Results:

- Products tested: 30
- Total demand values tested: 180
- MAE: 4.13
- RMSE: 5.76

Lower MAE and RMSE indicate smaller forecast errors.

These measurements are prototype validation results and should not be interpreted as guaranteed future forecasting accuracy.

## Workload Safety

The system includes an 8-hour maximum daily workload limit.

Example:

Current workload: 4 hours

New assignment: 3 hours

Total workload: 7 hours

Result:

Assignment accepted.

If the total workload exceeds 8 hours, the assignment is rejected.

Example:

Current workload: 6 hours

New assignment: 3 hours

Total workload: 9 hours

Result:

Assignment rejected.

## Automated Validation

Phase 3 includes automated validation checks for important system rules.

The following six checks were implemented:

1. Normal Product
2. Near-Tie Analogue
3. Missing Information
4. Weak Analogue
5. Workload Within Limit
6. Workload Exceeds Limit

Validation result:

- Total tests: 6
- Passed: 6
- Failed: 0

The automated validation was executed using:

python -m experiments.phase3_test_cases

The workload safety validation was executed using:

python -m experiments.workload_test

## Baseline Comparison

A simple baseline was created for comparison.

The baseline uses product attributes and category.

The prototype uses additional factors such as launch curves, failure behaviour, and promotion conditions.

The earlier comparison tested 30 products.

Prototype and baseline selected the same analogue for 10 products.

Agreement:

33.33%

The baseline comparison is included as an initial prototype-level comparison.

## Dashboard

The Streamlit dashboard provides:

- Product selection
- Best analogue
- Similarity score
- Confidence level
- Second-best analogue
- Near-tie warning
- Similarity explanation
- Data quality check
- Six-month demand forecast
- Forecast chart
- Workload safety validation

Example dashboard output:

Selected Product: P001

Best Analogue: P021

Similarity: 99.76%

Confidence: HIGH

Second Best Analogue: P002

Second Similarity: 99.75%

Difference: 0.01 percentage points

Because the difference is below 2 percentage points, the dashboard displays a near-tie manual-review warning.

## Current Phase 3 Status

The Phase 3 prototype includes:

- Dataset integration
- Similarity calculation
- Analogue selection
- Confidence calculation
- Similarity explanation
- Near-tie detection
- Missing-data handling
- No-strong-analogue detection
- Six-month demand forecast
- Improved retrospective forecast validation
- MAE measurement
- RMSE measurement
- Workload safety validation
- Automated validation checks
- Forecast visualization
- Baseline comparison
- Risk identification
- User guide
- Professional Streamlit dashboard

## How to Run

Open PowerShell in the project folder.

Activate the virtual environment:

.\venv\Scripts\Activate.ps1

Run the application:

streamlit run app.py

The application opens in a web browser.

## Running Experiments

Improved forecast validation:

python experiments\improved_forecast_validation.py

Automated Phase 3 validation:

python -m experiments.phase3_test_cases

Workload safety test:

python -m experiments.workload_test

## Important Note

The system is a decision-support prototype.

Similarity scores and analogue-based forecasts do not guarantee future demand or failure behaviour.

Low-confidence, near-tied, and missing-data cases should be reviewed by a human.

Workload validation is intended as a safety constraint and should not replace operational policies or human review.

## Limitations

- The current dataset is a prototype dataset.
- Forecast validation is retrospective.
- The current validation does not represent guaranteed future forecasting performance.
- Some automated validation cases use controlled test values to verify system rules.
- Additional real-world data would be required for production deployment.
- Human review remains important for low-confidence and uncertain cases.

## Future Work

Future stages can include:

- More rigorous out-of-sample forecast validation
- Additional failure-case testing
- Improved confidence estimation
- More workload constraints
- More advanced forecasting models
- Additional real-world datasets
- Further model optimization
- Final stakeholder validation
- Production deployment considerations

## Project Status

Phase 3 development and validation are in progress.

The current prototype demonstrates analogue selection, confidence handling, demand forecasting, validation metrics, workload safety, automated testing, and a Streamlit decision-support dashboard.