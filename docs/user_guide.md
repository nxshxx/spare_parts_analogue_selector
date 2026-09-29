# User Guide

## 1. Project Name

Spare Parts Analogue Selector

## 2. Purpose

This application helps users find an existing product that is similar to a new or low-history product.

The selected analogue can be used as a reference for demand planning and forecasting.

The application also provides confidence information, edge-case warnings, forecast validation, and workload safety checking.

## 3. Requirements

The system requires:

- Python 3.10 or above
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib

## 4. Running the Application

Open PowerShell in the project folder.

Activate the virtual environment:

.\venv\Scripts\Activate.ps1

Run the application:

streamlit run app.py

The application will open in a web browser.

## 5. Using the Application

Step 1:

Open the application.

Step 2:

Select a product from the product dropdown.

Step 3:

The system compares the selected product with other existing products.

Step 4:

The system selects the best analogue.

Step 5:

The system displays the similarity score.

Step 6:

The system displays the confidence level.

Step 7:

The system displays the similarity explanation.

Step 8:

The system displays the second-best analogue and score difference.

Step 9:

The system displays the six-month demand forecast.

Step 10:

The system displays the forecast as a line chart.

Step 11:

The user can enter current workload and new assignment hours.

Step 12:

The workload safety check determines whether the assignment is within the 8-hour limit.

## 6. Similarity Factors

The system compares products using:

- Product attributes
- Launch curve
- Category
- Failure behaviour
- Promotion conditions

The weights are:

Product attributes: 30%

Launch curve: 25%

Category: 20%

Failure behaviour: 15%

Promotion conditions: 10%

## 7. Confidence Levels

HIGH:

The similarity score is 80% or above.

MEDIUM:

The similarity score is between 60% and 79.99%.

LOW:

The similarity score is below 60%.

A LOW confidence result means that manual review is required.

Confidence can also be reduced when important information is missing.

## 8. Edge-Case Handling

### No Strong Analogue

If the similarity score is below 60%, the application displays a warning and recommends manual review.

### Near-Tied Analogues

The application compares the best and second-best analogue.

If the difference is 2 percentage points or less, a manual-review warning is displayed.

### Missing Information

The application detects missing important information.

Missing numerical values are handled using median values.

Missing promotion information is handled using default values.

Confidence is reduced when important information is missing.

## 9. Six-Month Demand Forecast

The application uses the historical demand pattern of the selected analogue.

The forecast contains:

- Month 1
- Month 2
- Month 3
- Month 4
- Month 5
- Month 6

The forecast is displayed as:

- A table
- A line chart

## 10. Forecast Accuracy Validation

A retrospective analogue-based validation experiment was performed.

Products tested:

30

Total demand values tested:

180

MAE:

4.51

RMSE:

6.09

Lower MAE and RMSE indicate smaller forecast errors.

These results are prototype validation measurements and do not guarantee future forecasting accuracy.

## 11. Workload Safety

The application uses an 8-hour maximum daily workload limit.

The total workload is calculated as:

Current workload + New assignment

Example:

Current workload: 4 hours

New assignment: 3 hours

Total workload: 7 hours

Result:

Assignment accepted.

If the total exceeds 8 hours, the assignment is rejected.

Example:

Current workload: 6 hours

New assignment: 3 hours

Total workload: 9 hours

Result:

Assignment rejected.

## 12. Baseline Comparison

The prototype was compared with a simple baseline.

The baseline uses:

- Product attributes
- Category

The prototype uses additional factors such as:

- Launch curves
- Failure behaviour
- Promotion conditions

The experiment tested 30 products.

The prototype and baseline selected the same analogue for 10 products.

Agreement:

33.33%

## 13. Example Output

The application may display:

Best Analogue: P021

Similarity: 99.76%

Confidence: HIGH

Second Best Analogue: P002

Second Similarity: 99.75%

Difference: 0.01 percentage points

A near-tie warning may be displayed when the two analogue candidates have very similar scores.

## 14. Important Note

The similarity score is a decision-support value.

The analogue-based forecast does not guarantee exactly the same future demand or failure behaviour.

Users should review LOW confidence and near-tied results before making important decisions.

The workload safety check is a constraint for the prototype and does not replace operational policies or human review.

## 15. Running Experiments

Forecast accuracy:

python experiments\forecast_accuracy.py

Workload safety:

python -m experiments.workload_test