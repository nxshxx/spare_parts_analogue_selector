import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

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

data = products.merge(failures, on="product_id", how="inner")
data = data.merge(promotions, on="product_id", how="inner")
data = data.merge(launch_curves, on="product_id", how="inner")

data["promotion_type"] = data["promotion_type"].fillna("None")

attribute_columns = [
    "engine_power_kw",
    "weight_kg",
    "price_usd"
]

scaler = MinMaxScaler()

attribute_scores = scaler.fit_transform(
    data[attribute_columns]
)

attribute_similarity = cosine_similarity(
    attribute_scores
)

category_similarity = (
    data["category"].values[:, None] ==
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
    data["promotion_active"].values[:, None] ==
    data["promotion_active"].values[None, :]
).astype(float)

overall_similarity = (
    0.30 * attribute_similarity +
    0.25 * launch_similarity +
    0.20 * category_similarity +
    0.15 * failure_similarity +
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

best_index = scores.argmax()

best_product = data.iloc[best_index]["product_id"]

similarity_score = scores[best_index] * 100

if similarity_score >= 80:
    confidence = "HIGH"
elif similarity_score >= 60:
    confidence = "MEDIUM"
else:
    confidence = "LOW"

st.subheader("Analogue Result")

st.write("Best Analogue:", best_product)
st.write(
    "Similarity:",
    round(similarity_score, 2),
    "%"
)
st.write("Confidence:", confidence)

st.subheader("Similarity Explanation")

st.write(
    "Product Attribute Similarity:",
    round(
        attribute_similarity[selected_index, best_index] * 100,
        2
    ),
    "%"
)

st.write(
    "Launch Curve Similarity:",
    round(
        launch_similarity[selected_index, best_index] * 100,
        2
    ),
    "%"
)

st.write(
    "Category Similarity:",
    round(
        category_similarity[selected_index, best_index] * 100,
        2
    ),
    "%"
)

st.write(
    "Failure Behaviour Similarity:",
    round(
        failure_similarity[selected_index, best_index] * 100,
        2
    ),
    "%"
)

st.write(
    "Promotion Similarity:",
    round(
        promotion_similarity[selected_index, best_index] * 100,
        2
    ),
    "%"
)

if confidence == "LOW":
    st.warning(
        "No strong analogue found. Manual review is required."
    )
elif confidence == "MEDIUM":
    st.warning(
        "Similarity is moderate. Manual review is recommended."
    )
else:
    st.success(
        "A strong analogue was found."
    )