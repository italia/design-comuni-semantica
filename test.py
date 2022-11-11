from engines import test_engines
from termcolor import colored, cprint


def _render_report(report):
    color = "green" if report["passed"] == report["total"] else "red"
    cprint(
        f"Total tests: {report['total']} - Passed: {report['passed']} - Failed: {report['failed']}\n",
        color,
    )


failed_tests = 0

for test_engine in test_engines:
    cprint(f"🧪 Testing {test_engine.name} templates", "yellow")
    report = test_engine.run()
    failed_tests += report["failed"]
    _render_report(report)

if failed_tests > 0:
    exit(1)
else:
    exit(0)
