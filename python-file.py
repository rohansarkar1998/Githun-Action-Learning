from openpyxl import Workbook

def create_excel():
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

    # Save the file
    wb.save("example.xlsx")
    print("Excel file created successfully!")

if __name__ == "__main__":
    create_excel()
