def generate_plan(subjects, hours):
    plan = {}
    time_per_subject = hours // len(subjects)

    for subject in subjects:
        plan[subject] = f"{time_per_subject} hours"

    return plan