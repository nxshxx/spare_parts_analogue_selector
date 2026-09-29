# Risk Register

## 1. Poor Analogue Selection

Risk:

The system may select an unsuitable existing product as the analogue.

Impact:

Forecasts based on the wrong analogue may be inaccurate.

Mitigation:

Use multiple similarity factors instead of depending on only one product attribute.

Status:

Open

## 2. No Strong Analogue

Risk:

A new product may not have a sufficiently similar existing product.

Impact:

The forecast may have low reliability.

Mitigation:

If similarity is below 60%, display LOW confidence and recommend manual review.

Status:

Handled

## 3. Missing Data

Risk:

Some product information may be missing.

Impact:

Similarity calculation may become less reliable.

Mitigation:

Handle missing values and reduce confidence when important information is unavailable.

Status:

Handled

## 4. Near-Tied Analogues

Risk:

Two existing products may have almost the same similarity score.

Impact:

The system may not clearly identify one best analogue.

Mitigation:

Compare the best and second-best analogue. If the difference is 2 percentage points or less, display a manual-review warning.

Status:

Handled

## 5. False Confidence

Risk:

A high similarity score may give users too much confidence in the result.

Impact:

Users may make incorrect planning decisions.

Mitigation:

Show confidence levels, similarity factors, and explanations instead of presenting the result as guaranteed.

Status:

Open

## 6. Data Quality

Risk:

Incorrect or outdated product data may affect the result.

Impact:

The selected analogue may be inaccurate.

Mitigation:

Check important product information before similarity calculation and display data-quality warnings when information is missing.

Status:

Handled

## 7. System Failure

Risk:

The application may fail while loading data or calculating similarity.

Impact:

Users may not receive a result.

Mitigation:

Test the application using different products and experiment scripts.

Status:

Open

## 8. Forecast Error

Risk:

The selected analogue may not accurately represent the future demand pattern of a new product.

Impact:

The analogue-based forecast may contain significant demand errors.

Mitigation:

Measure forecast error using MAE and RMSE and clearly communicate that the forecast is a decision-support estimate.

Status:

Handled

## 9. Workload Overload

Risk:

A new assignment may cause a worker's total workload to exceed the daily safety limit.

Impact:

The assignment may create excessive workload.

Mitigation:

Use an 8-hour maximum workload limit. Reject assignments when the total workload exceeds 8 hours.

Status:

Handled

## 10. Forecast Validation Limitation

Risk:

The current forecast validation uses historical analogue demand and does not represent a fully out-of-sample future forecast.

Impact:

The measured error may not represent real future forecasting performance.

Mitigation:

Treat the current MAE and RMSE as prototype validation results and improve the validation methodology in later project stages.

Status:

Open