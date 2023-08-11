from datetime import datetime
from inspect import getmembers, isfunction
from os import makedirs, path
from testing import auth_tests, core_tests, db_tests
from typing import Callable, Any, List


def get_callables_from_module(module: Any) -> List[Callable]:
    """
    Gets all the callables from a module.

    args:
        - module: The module to get the callables from.

    returns:
        - A list of callables.
    """
    callables = []
    for obj in getmembers(module):
        if obj[0].startswith("test_"):
            if isfunction(obj[1]):
                callables.append(obj[1])
    print(callables)
    return callables


def run_tests(test_type: str, test_funcs: List[Callable], report_file_path: str) -> int:
    """
    Runs all tests for a given set of test functions.

    args:
        - test_funcs: a list of test functions to run.
        - report_file_path: the path to the report file, where the results of the tests will be written.

    returns:
        - the number of failed tests as an integer.

    output:
        - Prints the results of failed tests.
    """
    failed_tests = 0
    with open(report_file_path, "a") as report_file:
        for test in test_funcs:
            print(f"Running {test.__name__}...")
            result, error = test()
            if not result:
                report_file.write(f"{error}\n")
                failed_tests += 1
        report_file.write(f"{test_type} tests complete.\n")
        report_file.write(
            f"{len(test_funcs) - failed_tests} out of {len(test_funcs)} tests passed.\n")


def create_report_folder() -> str:
    """
    Creates a folder for the test reports.

    args:
        - None

    returns:
        - a unique, identifiable folder path for the reports as a string.
    """
    copy_flag = 0
    current_date = datetime.now().strftime("%Y-%m-%d")
    report_folder_path = f"testing/reports/{current_date}_{copy_flag}"
    while path.exists(report_folder_path):
        copy_flag += 1
        report_folder_path = f"testing/reports/{current_date}_{copy_flag}"
    makedirs(report_folder_path)
    return report_folder_path


def create_report_file(report_folder_path: str, test_type: str) -> str:
    """
    Creates a report file for a given test type.

    args:
        - report_folder_path: the path to the folder where the reports will be stored.
        - test_type: the type of tests being run.

    returns:
        - the path to the report file as a string.
    """
    report_file_path = f"{report_folder_path}/{test_type}_report.txt"
    with open(report_file_path, "w") as report_file:
        report_file.write(f"Test report for {test_type} tests.\n")
    return report_file_path


def main() -> None:
    """
    Runs all tests for the application.
    """
    report_folder_path = create_report_folder()

    test_functions = {"authentication": get_callables_from_module(auth_tests),
                      "core": get_callables_from_module(core_tests),
                      "database": get_callables_from_module(db_tests)}
    for test_type, test_funcs in test_functions.items():
        print(f"Running {test_type} tests...")
        report_file_path = create_report_file(report_folder_path, test_type)
        run_tests(test_type, test_funcs, report_file_path)


if __name__ == "__main__":
    main()
