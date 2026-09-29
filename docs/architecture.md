# System Architecture

## 1. Project Name

Spare Parts Analogue Selector

## 2. Project Purpose

The system helps select an existing spare-parts product that is similar to a new or low-history product.

The selected product is used as an analogue for planning and demand estimation.

## 3. System Flow

The system follows this process:

Dataset
↓
Data Processing
↓
Feature Preparation
↓
Similarity Calculation
↓
Analogue Selection
↓
Confidence Calculation
↓
Demand Forecast
↓
Forecast Validation
↓
Workload Safety Check
↓
Result and Explanation

## 4. Input Data

The system uses four datasets:

1. Products
2. Failures
3. Promotions
4. Launch Curves

All datasets are connected using product_id.

## 5. Data Processing

The datasets are merged using product_id.

Missing numerical values are handled using median values.

Missing promotion information is handled using default values.

Missing category information is replaced with "Unknown".

Important missing information is detected before processing so that confidence can be reduced when required.

## 6. Analogue Selection

The system compares the selected product with existing products.

Five factors are used:

- Product attributes
- Launch curve
- Category
- Failure behaviour
- Promotion conditions

The factors are given different weights.

## 7. Similarity Weights

Product attributes: 30%

Launch curve: 25%

Category: 20%

Failure behaviour: 15%

Promotion conditions: 10%

The weighted values are combined to calculate the overall similarity score.

## 8. Confidence

The system converts the similarity score into a confidence level.

HIGH:

80% or above

MEDIUM:

60% to 79.99%

LOW:

Below 60%

Confidence can also be reduced when important information is missing.

## 9. Edge-Case Handling

The system checks for important analogue-selection conditions.

### No Strong Analogue

If the similarity score is below 60%, the system recommends manual review.

### Near-Tied Analogues

The best and second-best analogue scores are compared.

If the difference is 2 percentage points or less, the system displays a manual-review warning.

### Missing Data

The system handles missing information and reduces confidence when important information is unavailable.

## 10. Demand Forecast

After selecting an analogue, the system retrieves its six-month historical demand pattern.

The forecast contains:

- Month 1
- Month 2
- Month 3
- Month 4
- Month 5
- Month 6

The Streamlit application displays the forecast as a table and line chart.

## 11. Forecast Validation

A retrospective analogue-based validation experiment was created.

The experiment tested 30 products and 180 demand values.

Measured results:

MAE: 4.51

RMSE: 6.09

These measurements represent prototype validation of analogue-based demand transfer.

They should not be interpreted as guaranteed future forecasting accuracy.

## 12. Workload Safety

The system includes a maximum daily workload limit of 8 hours.

The workload module calculates:

Current workload + New assignment = Total workload

If the total is 8 hours or less, the assignment is accepted.

If the total exceeds 8 hours, the assignment is rejected.

Example:

4 hours + 3 hours = 7 hours

Assignment accepted.

6 hours + 3 hours = 9 hours

Assignment rejected.

## 13. Output

The system displays:

- Selected product
- Best analogue
- Similarity score
- Confidence level
- Second-best analogue
- Similarity explanation
- Data quality information
- Analogue comparison
- Six-month demand forecast
- Forecast chart
- Workload safety status

## 14. Technology Used

Python is used for the main development.

Pandas is used for data processing.

NumPy is used for numerical operations.

Scikit-learn is used for normalization and similarity calculation.

Streamlit is used to create the web application.

Matplotlib is available for data visualization and experiments.

## 15. Baseline

A simple baseline method is used for comparison.

The baseline uses:

- Product attributes
- Category

The prototype uses additional information such as:

- Launch curves
- Failure behaviour
- Promotion conditions

The prototype and baseline were tested using 30 products.

The same analogue was selected for 10 products.

The measured agreement was 33.33%.

## 16. Project Scope for Phase 2

The current prototype demonstrates:

- Dataset integration
- Data processing
- Similarity calculation
- Analogue selection
- Confidence calculation
- Similarity explanation
- Edge-case handling
- Missing-data handling
- Demand forecasting
- Forecast accuracy validation
- Workload safety validation
- Forecast visualization
- Baseline comparison
- Risk identification
- User guide

Advanced forecasting validation, improved confidence estimation, additional safety constraints, and final stakeholder validation can be completed in later project stages.