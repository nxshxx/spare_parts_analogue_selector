import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_absolute_error, mean_squared_error

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

actual_values = []
forecast_values = []
tested_products = []

for selected_index in range(len(data)):

    scores = overall_similarity[selected_index].copy()

    scores[selected_index] = -1

    best_index = scores.argmax()

    actual = data.iloc[selected_index][
        launch_columns
    ].values.astype(float)

    forecast = data.iloc[best_index][
        launch_columns
    ].values.astype(float)

    actual_values.extend(actual)

    forecast_values.extend(forecast)

    tested_products.append(
        data.iloc[selected_index]["product_id"]
    )

mae = mean_absolute_error(
    actual_values,
    forecast_values
)

rmse = np.sqrt(
    mean_squared_error(
        actual_values,
        forecast_values
    )
)

print("FORECAST ACCURACY")

print()

print(
    "Products tested:",
    len(tested_products)
)

print(
    "Total demand values tested:",
    len(actual_values)
)

print(
    "MAE:",
    round(mae, 2)
)

print(
    "RMSE:",
    round(rmse, 2)
)

print()

print(
    "Lower MAE and RMSE indicate smaller "
    "forecast errors."
)