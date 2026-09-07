# Spare Parts Analogue Selector

## Project Overview

The Spare Parts Analogue Selector is a decision-support system for selecting a similar existing product for a new or low-history product.

The system helps users identify a suitable analogue by comparing product attributes, launch curves, category behaviour, failure behaviour, and promotional conditions.

## Problem Statement

New spare-parts products often have little historical data.

Because of this, it is difficult to predict their demand and failure behaviour.

The system selects a similar existing product and provides a similarity score and confidence level.

## Objectives

- Select the best existing analogue for a product
- Use multiple product characteristics for comparison
- Explain why an analogue was selected
- Show confidence in the result
- Handle cases where no strong analogue exists
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

Contains the main processing and analogue selection code.

experiments/

Contains baseline comparison experiments.

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
- Category: 20%
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

## Baseline Comparison

A simple baseline was created for comparison.

The baseline uses product attributes and category.

The prototype uses additional factors such as launch curves, failure behaviour, and promotion conditions.

The experiment tested 30 products.

Prototype and baseline selected the same analogue for 10 products.

Agreement:

33.33%

## Current Project Status

The Review 1 prototype includes:

- Dataset integration
- Data processing
- Similarity calculation
- Analogue selection
- Confidence calculation
- Similarity explanation
- Baseline comparison
- Architecture documentation
- Data schema documentation
- Risk register
- User guide

## How to Run

Open PowerShell in the project folder.

Activate the virtual environment:

.\venv\Scripts\Activate.ps1

Run the application:

streamlit run app.py

The application opens in a web browser.

## Future Work

Future stages can include:

- Forecast accuracy validation
- More failure-case testing
- Workload safety validation
- Improved confidence estimation
- Further model optimization
- Final stakeholder validation