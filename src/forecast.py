import pandas as pd

launch_curves = pd.read_csv("data/launch_curves.csv.txt")

def get_forecast(product_id):

    product_data = launch_curves[
        launch_curves["product_id"] == product_id
    ]

    if product_data.empty:
        return None

    forecast = {
        "Month 1": product_data.iloc[0]["month_1_demand"],
        "Month 2": product_data.iloc[0]["month_2_demand"],
        "Month 3": product_data.iloc[0]["month_3_demand"],
        "Month 4": product_data.iloc[0]["month_4_demand"],
        "Month 5": product_data.iloc[0]["month_5_demand"],
        "Month 6": product_data.iloc[0]["month_6_demand"]
    }

    return forecast