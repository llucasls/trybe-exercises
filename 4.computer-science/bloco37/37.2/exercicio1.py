def max_stability_time(sample):
    sample = [str(value) for value in sample]
    result = "".join(sample).split('0')
    result.sort()
    return len(result[-1])
