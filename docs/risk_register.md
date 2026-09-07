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
Give a LOW confidence result and recommend manual review.

Status:
Open

## 3. Missing Data

Risk:
Some product information may be missing.

Impact:
Similarity calculation may become less reliable.

Mitigation:
Handle missing values and reduce confidence when important information is unavailable.

Status:
Open

## 4. Near-Tied Analogues

Risk:
Two existing products may have almost the same similarity score.

Impact:
The system may not clearly identify one best analogue.

Mitigation:
Show a review warning when multiple analogues have very similar scores.

Status:
Open

## 5. False Confidence

Risk:
A high similarity score may give users too much confidence in the result.

Impact:
Users may make incorrect planning decisions.

Mitigation:
Show confidence levels and explanations instead of presenting the result as guaranteed.

Status:
Open

## 6. Data Quality

Risk:
Incorrect or outdated product data may affect the result.

Impact:
The selected analogue may be inaccurate.

Mitigation:
Check product data before using it in the system.

Status:
Open

## 7. System Failure

Risk:
The application may fail while loading data or calculating similarity.

Impact:
Users may not receive a result.

Mitigation:
Use error handling and test the system with different input conditions.

Status:
Open