# User Guide

## 1. Project Name

Spare Parts Analogue Selector

## 2. Purpose

This application helps users find an existing product that is similar to a new or low-history product.

The selected analogue can be used as a reference for planning and forecasting.

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

## 6. Similarity Factors

The system compares products using:

- Product attributes
- Launch curve
- Category
- Failure behaviour
- Promotion conditions

## 7. Confidence Levels

HIGH:

The similarity score is 80% or above.

MEDIUM:

The similarity score is between 60% and 79.99%.

LOW:

The similarity score is below 60%.

A LOW confidence result means that manual review is recommended.

## 8. Example Output

The application may display:

Best Analogue: P021

Similarity: 99.76%

Confidence: HIGH

It also shows the similarity of individual factors.

## 9. Important Note

The similarity score is a decision-support value.

It does not guarantee that the selected product will have exactly the same future demand or failure behaviour.

Users should review LOW confidence results before making important decisions.

## 10. Baseline Comparison

The prototype was compared with a simple baseline method.

The baseline uses product attributes and category.

The prototype uses additional factors such as launch curves, failure behaviour, and promotion conditions.

The experiment tested 30 products.

The prototype and baseline selected the same analogue for 10 products.

Agreement:

33.33%

This result provides a measurable comparison between the prototype and the simple baseline.