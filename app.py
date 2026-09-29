import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
from src.forecast import get_forecast
from src.workload_safety import check_workload

st.set_page_config(
    page_title="Spare Parts Analogue Selector",
    page_icon="🔧",
    layout="wide"
)

st.title("Spare Parts Analogue Selector")
st.write("Find the most similar existing product for a new product.")

products = pd.read_csv("data/products.csv.txt")
failures = pd.read_csv("data/failures.csv.txt")
promotions = pd.read_csv("data/promotions.csv.txt")
launch_curves = pd.read_csv("data/launch_curves.csv.txt")

data = products.merge(
    failures,
    on="product_id",
    how="inner"
)

data = data.merge(
    promotions,
    on="product_id",
    how="inner"
)

data = data.merge(
    launch_curves,
    on="product_id",
    how="inner"
)

important_columns = [
    "engine_power_kw",
    "weight_kg",
    "price_usd",
    "avg_failure_rate",
    "critical_failures",
    "month_1_demand",
    "month_2_demand",
    "month_3_demand",
    "month_4_demand",
    "month_5_demand",
    "month_6_demand",
    "promotion_active",
    "category"
]

missing_before_processing = data[important_columns].isna()

numeric_columns = [
    "engine_power_kw",
    "weight_kg",
    "price_usd",
    "avg_failure_rate",
    "critical_failures",
    "month_1_demand",
    "month_2_demand",
    "month_3_demand",
    "month_4_demand",
    "month_5_demand",
    "month_6_demand"
]

for column in numeric_columns:
    data[column] = data[column].fillna(
        data[column].median()
    )

data["promotion_active"] = data["promotion_active"].fillna(False)

data["promotion_type"] = data["promotion_type"].fillna(
    "None"
)

data["category"] = data["category"].fillna(
    "Unknown"
)

attribute_columns = [
    "engine_power_kw",
    "weight_kg",
    "price_usd"
]

attribute_scaler = MinMaxScaler()

attribute_scores = attribute_scaler.fit_transform(
    data[attribute_columns]
)

attribute_similarity = cosine_similarity(
    attribute_scores
)

category_similarity = (
    data["category"].values[:, None]
    ==
    data["category"].values[None, :]
).astype(float)

failure_columns = [
    "avg_failure_rate",
    "critical_failures"
]

failure_scaler = MinMaxScaler()

failure_scores = failure_scaler.fit_transform(
    data[failure_columns]
)

failure_similarity = cosine_similarity(
    failure_scores
)

launch_columns = [
    "month_1_demand",
    "month_2_demand",
    "month_3_demand",
    "month_4_demand",
    "month_5_demand",
    "month_6_demand"
]

launch_scaler = MinMaxScaler()

launch_scores = launch_scaler.fit_transform(
    data[launch_columns]
)

launch_similarity = cosine_similarity(
    launch_scores
)

promotion_similarity = (
    data["promotion_active"].values[:, None]
    ==
    data["promotion_active"].values[None, :]
).astype(float)

overall_similarity = (
    0.30 * attribute_similarity
    +
    0.25 * launch_similarity
    +
    0.20 * category_similarity
    +
    0.15 * failure_similarity
    +
    0.10 * promotion_similarity
)

product_ids = data["product_id"].tolist()

selected_product = st.selectbox(
    "Select a product",
    product_ids
)

selected_index = data.index[
    data["product_id"] == selected_product
][0]

scores = overall_similarity[selected_index].copy()

scores[selected_index] = -1

sorted_indices = np.argsort(scores)[::-1]

best_index = sorted_indices[0]

second_index = sorted_indices[1]

best_product = data.iloc[best_index]["product_id"]

second_product = data.iloc[second_index]["product_id"]

similarity_score = scores[best_index] * 100

second_similarity_score = scores[second_index] * 100

difference = (
    similarity_score
    -
    second_similarity_score
)

selected_missing_columns = (
    missing_before_processing.iloc[selected_index]
)

analogue_missing_columns = (
    missing_before_processing.iloc[best_index]
)

missing_selected = (
    selected_missing_columns[
        selected_missing_columns
    ].index.tolist()
)

missing_analogue = (
    analogue_missing_columns[
        analogue_missing_columns
    ].index.tolist()
)

missing_data_found = (
    len(missing_selected) > 0
    or
    len(missing_analogue) > 0
)

if similarity_score >= 80:
    confidence = "HIGH"
elif similarity_score >= 60:
    confidence = "MEDIUM"
else:
    confidence = "LOW"

if difference <= 2:
    near_tie = True
else:
    near_tie = False

if missing_data_found:

    if confidence == "HIGH":
        confidence = "MEDIUM"

    elif confidence == "MEDIUM":
        confidence = "LOW"

st.subheader("Analogue Result")

st.write(
    "Best Analogue:",
    best_product
)

st.write(
    "Similarity:",
    round(similarity_score, 2),
    "%"
)

st.write(
    "Confidence:",
    confidence
)

st.write(
    "Second Best Analogue:",
    second_product
)

st.write(
    "Second Similarity:",
    round(second_similarity_score, 2),
    "%"
)

st.subheader("Similarity Explanation")

st.write(
    "Product Attribute Similarity:",
    round(
        attribute_similarity[
            selected_index,
            best_index
        ] * 100,
        2
    ),
    "%"
)

st.write(
    "Launch Curve Similarity:",
    round(
        launch_similarity[
            selected_index,
            best_index
        ] * 100,
        2
    ),
    "%"
)

st.write(
    "Category Similarity:",
    round(
        category_similarity[
            selected_index,
            best_index
        ] * 100,
        2
    ),
    "%"
)

st.write(
    "Failure Behaviour Similarity:",
    round(
        failure_similarity[
            selected_index,
            best_index
        ] * 100,
        2
    ),
    "%"
)

st.write(
    "Promotion Similarity:",
    round(
        promotion_similarity[
            selected_index,
            best_index
        ] * 100,
        2
    ),
    "%"
)

st.subheader("Data Quality Check")

if missing_data_found:

    st.warning(
        "Missing information was detected. "
        "Confidence has been reduced."
    )

    if len(missing_selected) > 0:

        st.write(
            "Missing data for selected product:",
            ", ".join(missing_selected)
        )

    if len(missing_analogue) > 0:

        st.write(
            "Missing data for selected analogue:",
            ", ".join(missing_analogue)
        )

else:

    st.success(
        "All important information is available."
    )

st.subheader("Analogue Comparison")

st.write(
    "Best Analogue:",
    best_product,
    "→",
    round(similarity_score, 2),
    "%"
)

st.write(
    "Second Best:",
    second_product,
    "→",
    round(second_similarity_score, 2),
    "%"
)

st.write(
    "Difference:",
    round(difference, 2),
    "percentage points"
)

if similarity_score < 60:

    st.warning(
        "No strong analogue found. "
        "Manual review is required."
    )

elif near_tie:

    st.warning(
        "Two analogue candidates have very similar "
        "scores. Manual review is recommended."
    )

elif confidence == "LOW":

    st.warning(
        "Confidence is LOW. Manual review is required."
    )

elif confidence == "MEDIUM":

    st.warning(
        "Similarity is moderate. "
        "Manual review is recommended."
    )

else:

    st.success(
        "A strong analogue was found."
    )

st.subheader("6-Month Demand Forecast")

forecast = get_forecast(best_product)

if forecast is not None:

    forecast_table = pd.DataFrame(
        {
            "Month": list(forecast.keys()),
            "Forecast Demand": list(forecast.values())
        }
    )

    st.table(forecast_table)

    st.write(
        "The forecast uses the historical demand "
        "pattern of the selected analogue."
    )

    st.line_chart(
        forecast_table.set_index("Month")["Forecast Demand"]
    )

else:

    st.warning(
        "Forecast data is not available "
        "for the selected analogue."
    )

st.subheader("Workload Safety Check")

current_hours = st.number_input(
    "Current Workload (hours)",
    min_value=0.0,
    max_value=24.0,
    value=4.0,
    step=1.0
)

new_assignment_hours = st.number_input(
    "New Assignment (hours)",
    min_value=0.0,
    max_value=24.0,
    value=3.0,
    step=1.0
)

accepted, total_hours = check_workload(
    current_hours,
    new_assignment_hours
)

st.write(
    "Total Workload:",
    total_hours,
    "hours"
)

if accepted:

    st.success(
        "Assignment accepted. Workload is within the 8-hour limit."
    )

else:

    st.error(
        "Assignment rejected. Workload exceeds the 8-hour limit."
    )