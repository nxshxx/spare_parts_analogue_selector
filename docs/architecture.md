# System Architecture

## 1. Project Name

Spare Parts Analogue Selector

## 2. Project Purpose

The system helps select an existing spare-parts product that is similar to a new product.

The selected product is used as an analogue for planning and forecasting.

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

Missing promotion type values are handled by replacing them with "None".

Numerical product information is normalized before similarity calculation.

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

Category behaviour: 20%

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

LOW confidence results are recommended for manual review.

## 9. Output

The system displays:

- Selected product
- Best analogue
- Similarity score
- Confidence level
- Individual similarity factors
- Review warning when confidence is low or moderate

## 10. Technology Used

Python is used for the main development.

Pandas is used for data processing.

NumPy is used for numerical operations.

Scikit-learn is used for normalization and similarity calculation.

Streamlit is used to create the web application.

Matplotlib is available for data visualization and experiments.

## 11. Baseline

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

## 12. Project Scope for Review 1

The current prototype demonstrates:

- Dataset integration
- Data processing
- Similarity calculation
- Analogue selection
- Confidence level
- Similarity explanation
- Baseline comparison
- Basic risk identification
- User guide

Advanced forecasting validation, workload safety validation, and further optimization can be completed in later project stages.