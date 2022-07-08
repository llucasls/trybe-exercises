def max_stability_time(sample):
    streak = 0
    record = 0
    for value in sample:
        if value == 1:
            streak += 1
        else:
            streak = 0
        record = max(record, streak)
    return record
