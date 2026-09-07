import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

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

baseline_similarity = (
    0.70 * attribute_similarity +
    0.30 * category_similarity
)

prototype_matches = []
baseline_matches = []

for i in range(len(data)):
    prototype_scores = overall_similarity[i].copy()
    baseline_scores = baseline_similarity[i].copy()

    prototype_scores[i] = -1
    baseline_scores[i] = -1

    prototype_index = prototype_scores.argmax()
    baseline_index = baseline_scores.argmax()

    prototype_matches.append(
        data.iloc[prototype_index]["product_id"]
    )

    baseline_matches.append(
        data.iloc[baseline_index]["product_id"]
    )

comparison = pd.DataFrame({
    "Product": data["product_id"],
    "Prototype Analogue": prototype_matches,
    "Baseline Analogue": baseline_matches
})

comparison["Same Analogue"] = (
    comparison["Prototype Analogue"] ==
    comparison["Baseline Analogue"]
)

same_count = comparison["Same Analogue"].sum()
total_count = len(comparison)

agreement = (same_count / total_count) * 100

print("BASELINE COMPARISON")
print()
print(comparison.to_string(index=False))
print()
print("Total products tested:", total_count)
print("Same analogue selected:", same_count)
print("Agreement:", round(agreement, 2), "%")