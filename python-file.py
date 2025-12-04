from openpyxl import Workbook
from datetime import datetime

def create_excel():
    # Get today's date and month
    today_date = datetime.now().strftime("%Y-%m-%d")
    current_month = datetime.now().strftime("%Y-%m")

    # Create a new workbook
    wb = Workbook()
    sheet = wb.active

    # Add some content
    sheet["A1"] = "Name"
    sheet["B1"] = "Age"

    sheet["A2"] = "Rohan"
    sheet["B2"] = 25

    sheet["A3"] = "Amit"
    sheet["B3"] = 30

    # Create file names
    file_with_date = f"example_{today_date}.xlsx"
    file_with_month = f"example_{current_month}.xlsx"

    # Save the files
    wb.save(file_with_date)
    wb.save(file_with_month)

    print(f"Excel files created:\n  {file_with_date}\n  {file_with_month}")

if __name__ == "__main__":
    create_excel()
