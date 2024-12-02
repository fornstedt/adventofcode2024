import numpy as np

def count_safe_reports(reports: list, check_function) -> int:
    return [check_function(list(map(int, x))) for x in reports].count(True)

def is_report_safe(report: list) -> bool:
    diff = list(np.diff(report))
    return sum(x > 0 and x <  4 for x in diff) == len(diff) or \
           sum(x < 0 and x > -4 for x in diff) == len(diff)

def is_report_safe_damper(report: list) -> bool:
    is_safe = False

    for i in range(len(report)):
        damped_report = report.copy()
        del damped_report[i]
        if is_report_safe(damped_report):
            is_safe = True
            break

    return is_safe

def main():
    # Get data
    example_data = [values.split() for values in open('example.txt', 'r').readlines()]
    real_data = [values.split() for values in open('input.txt', 'r').readlines()]

    # Part 1
    nof_safe_reports = count_safe_reports(example_data, is_report_safe)
    assert nof_safe_reports == 2, f"Expected 2, but was {nof_safe_reports}"

    nof_safe_reports = count_safe_reports(real_data, is_report_safe)
    print(f"Part 1: The number of safe reports is {nof_safe_reports}")

    # Part 2
    nof_safe_reports = count_safe_reports(example_data, is_report_safe_damper)
    assert nof_safe_reports == 4, f"Expected 4, but was {nof_safe_reports}"

    nof_safe_reports = count_safe_reports(real_data, is_report_safe_damper)
    print(f"Part 2: The number of safe reports is {nof_safe_reports}")


if __name__ == "__main__":
    main()
