# Data Schema

## 1. Products Dataset

File: products.csv.txt

This dataset contains the basic information about each spare part product.

| Column | Description |
|---|---|
| product_id | Unique ID of the product |
| category | Product category |
| engine_power_kw | Engine power in kilowatts |
| weight_kg | Product weight in kilograms |
| price_usd | Product price in USD |
| launch_month | Month in which the product was launched |

## 2. Failures Dataset

File: failures.csv.txt

This dataset contains information about product failure behaviour.

| Column | Description |
|---|---|
| product_id | Unique ID of the product |
| avg_failure_rate | Average failure rate |
| critical_failures | Number of critical failures |
| common_spare_part | Common spare part used for the product |

## 3. Promotions Dataset

File: promotions.csv.txt

This dataset contains information about promotional conditions.

| Column | Description |
|---|---|
| product_id | Unique ID of the product |
| promotion_active | Shows whether promotion is active |
| discount_percent | Discount percentage |
| promotion_type | Type of promotion |

## 4. Launch Curves Dataset

File: launch_curves.csv.txt

This dataset contains product demand during the first six months after launch.

| Column | Description |
|---|---|
| product_id | Unique ID of the product |
| month_1_demand | Demand during month 1 |
| month_2_demand | Demand during month 2 |
| month_3_demand | Demand during month 3 |
| month_4_demand | Demand during month 4 |
| month_5_demand | Demand during month 5 |
| month_6_demand | Demand during month 6 |

## 5. Data Relationship

All four datasets are connected using:

product_id

The product_id acts as the common key.

## 6. Data Processing

The datasets are merged using product_id.

Missing promotion type values are replaced with "None".

Numerical values are normalized before calculating similarity.

## 7. Similarity Factors

The prototype uses five main factors:

1. Product attributes - 30%
2. Launch curve - 25%
3. Category behaviour - 20%
4. Failure behaviour - 15%
5. Promotion conditions - 10%

The final similarity score is calculated using these weighted factors.

## 8. Output

The system provides:

- Selected product
- Best analogue product
- Similarity score
- Confidence level
- Similarity explanation

Confidence levels are:

HIGH - similarity is 80% or above

MEDIUM - similarity is between 60% and 79.99%

LOW - similarity is below 60%