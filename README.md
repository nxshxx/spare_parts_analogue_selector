# Spare Parts Analogue Selector

## Project Overview

The Spare Parts Analogue Selector is a decision-support system for selecting a similar existing product for a new or low-history product.

The system compares product attributes, launch curves, category behaviour, failure behaviour, and promotional conditions to identify a suitable analogue.

The system also provides confidence information, edge-case warnings, analogue-based demand forecasting, forecast error measurements, and workload safety validation.

## Problem Statement

New spare-parts products often have little historical data.

Because of this, it is difficult to estimate their demand and failure behaviour.

The system selects a similar existing product and provides a similarity score and confidence level.

The selected analogue can also be used as a reference for a six-month demand forecast.

## Objectives

- Select the best existing analogue for a product
- Use multiple product characteristics for comparison
- Explain why an analogue was selected
- Show confidence in the result
- Detect near-tied analogue candidates
- Handle missing information
- Identify cases where no strong analogue exists
- Generate an analogue-based six-month demand forecast
- Measure forecast error using MAE and RMSE
- Apply a workload safety limit
- Compare the prototype with a simple baseline

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

Contains the main processing, forecasting, and workload safety code.

experiments/

Contains baseline comparison, forecast accuracy, and workload testing experiments.

docs/

Contains project documentation.

app.py

Main Streamlit application.

requirements.txt

Contains the required Python libraries.

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

LOW confidence results require manual review.

The system can also reduce confidence when important information is missing.

## Edge-Case Handling

The system handles several important cases.

### No Strong Analogue

If the similarity score is below 60%, the system displays a warning and recommends manual review.

### Near-Tied Analogues

The system compares the best and second-best analogue.

If the difference is 2 percentage points or less, the system displays a manual-review warning.

### Missing Information

Missing numerical values are handled using median values.

Missing promotion information is handled using default values.

The system records missing information before processing and reduces confidence when important information is missing.

## Demand Forecast

The selected analogue's historical six-month demand pattern is displayed as an analogue-based forecast.

The forecast contains:

- Month 1
- Month 2
- Month 3
- Month 4
- Month 5
- Month 6

The Streamlit application displays the forecast as both a table and a line chart.

## Forecast Accuracy Validation

A retrospective analogue-based validation experiment was created.

The experiment tested:

Products tested: 30

Total demand values tested: 180

MAE: 4.51

RMSE: 6.09

MAE and RMSE are used to measure the difference between the target product demand values and the demand values transferred from the selected analogue.

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

## Baseline Comparison

A simple baseline was created for comparison.

The baseline uses product attributes and category.

The prototype uses additional factors such as launch curves, failure behaviour, and promotion conditions.

The experiment tested 30 products.

Prototype and baseline selected the same analogue for 10 products.

Agreement:

33.33%

## Current Phase 2 Status

The Phase 2 prototype includes:

- Dataset integration
- Similarity calculation
- Analogue selection
- Confidence calculation
- Similarity explanation
- Near-tie detection
- Missing-data handling
- No-strong-analogue detection
- Six-month demand forecast
- Forecast accuracy validation
- MAE measurement
- RMSE measurement
- Workload safety validation
- Forecast visualization
- Baseline comparison
- Risk identification
- User guide

## How to Run

Open PowerShell in the project folder.

Activate the virtual environment:

.\venv\Scripts\Activate.ps1

Run the application:

streamlit run app.py

The application opens in a web browser.

## Running Experiments

Forecast accuracy:

python experiments\forecast_accuracy.py

Workload safety test:

python -m experiments.workload_test

## Important Note

The system is a decision-support prototype.

Similarity scores and analogue-based forecasts do not guarantee future demand or failure behaviour.

Low-confidence and near-tied results should be reviewed manually.

Workload validation is intended as a safety constraint and should not replace operational policies or human review.

## Future Work

Future stages can include:

- Improved out-of-sample forecast validation
- More failure-case testing
- Improved confidence estimation
- Additional workload constraints
- More advanced forecasting models
- Further model optimization
- Final stakeholder validation