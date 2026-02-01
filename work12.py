# Independent report generation functions
def sales_report():
    print("Generating Sales Report...")


def inventory_report():
    print("Generating Inventory Report...")


def employee_report():
    print("Generating Employee Report...")


# Central function to call reports
def generate_report(report_name, report_functions):
    if report_name in report_functions:
        report_functions[report_name]()
    else:
        print("Report not found")


# Main program
reports = {
    "sales": sales_report,
    "inventory": inventory_report,
    "employee": employee_report
}

print("Available Reports: sales, inventory, employee")
choice = input("Enter report name: ").lower()

generate_report(choice, reports)