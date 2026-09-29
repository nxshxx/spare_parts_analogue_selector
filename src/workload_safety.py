def check_workload(current_hours, new_assignment_hours, maximum_hours=8):
    
    total_hours = current_hours + new_assignment_hours

    if total_hours <= maximum_hours:
        return True, total_hours

    return False, total_hours