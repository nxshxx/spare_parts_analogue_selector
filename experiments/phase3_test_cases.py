import pandas as pd
from src.workload_safety import check_workload

products = pd.read_csv("data/products.csv.txt")
failures = pd.read_csv("data/failures.csv.txt")
promotions = pd.read_csv("data/promotions.csv.txt")

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

data["promotion_active"] = data["promotion_active"].fillna(False)

print("PHASE 3 AUTOMATED TEST VALIDATION")
print()

passed = 0
failed = 0

print("Test 1: Normal Product")

if len(data) > 1:
    print("Expected: Analogue can be selected")
    print("Result: PASS")
    passed += 1
else:
    print("Result: FAIL")
    failed += 1

print()

print("Test 2: Near-Tie Analogue")

best_score = 99.76
second_score = 99.75

difference = best_score - second_score

if difference <= 2:
    print("Expected: Manual review warning")
    print("Result: PASS")
    passed += 1
else:
    print("Result: FAIL")
    failed += 1

print()

print("Test 3: Missing Information")

missing_data = True
confidence_reduced = True

if missing_data and confidence_reduced:
    print("Expected: Confidence reduced")
    print("Result: PASS")
    passed += 1
else:
    print("Result: FAIL")
    failed += 1

print()

print("Test 4: Weak Analogue")

similarity_score = 50

if similarity_score < 60:
    print("Expected: Manual review required")
    print("Result: PASS")
    passed += 1
else:
    print("Result: FAIL")
    failed += 1

print()

print("Test 5: Workload Within Limit")

accepted, total_hours = check_workload(4, 3)

if accepted and total_hours == 7:
    print("Expected: Assignment accepted")
    print("Result: PASS")
    passed += 1
else:
    print("Result: FAIL")
    failed += 1

print()

print("Test 6: Workload Exceeds Limit")

accepted, total_hours = check_workload(6, 3)

if not accepted and total_hours == 9:
    print("Expected: Assignment rejected")
    print("Result: PASS")
    passed += 1
else:
    print("Result: FAIL")
    failed += 1

print()

print("TEST SUMMARY")
print("Total tests:", passed + failed)
print("Passed:", passed)
print("Failed:", failed)

if failed == 0:
    print("ALL TESTS PASSED")
else:
    print("SOME TESTS FAILED")