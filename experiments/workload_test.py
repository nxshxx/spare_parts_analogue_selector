from src.workload_safety import check_workload

current_hours = 4
new_assignment_hours = 3

accepted, total_hours = check_workload(
    current_hours,
    new_assignment_hours
)

print("Current workload:", current_hours, "hours")
print("New assignment:", new_assignment_hours, "hours")
print("Total workload:", total_hours, "hours")

if accepted:
    print("Assignment accepted")
else:
    print("Assignment rejected")