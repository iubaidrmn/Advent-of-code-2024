def is_safe(report):
    """
    Determines if a report is safe based on the rules provided.
    """
    for i in range(len(report) - 1):
        diff = report[i+1] - report[i]
        if diff == 0 or abs(diff) > 3:
            return False
    return True

def analyze_reports(filename):
    """
    Reads reports from the input file and counts how many are safe.
    """
    with open(filename, 'r') as file:
        reports = file.readlines()
    
    safe_count = 0
    for report in reports:
        levels = list(map(int, report.strip().split()))
        if is_safe(levels):
            safe_count += 1

    return safe_count

if __name__ == "__main__":
    # Input file name
    input_file = "input.txt"
    # Analyze reports and print the number of safe ones
    safe_reports = analyze_reports(input_file)
    print(f"Number of safe reports: {safe_reports}")
