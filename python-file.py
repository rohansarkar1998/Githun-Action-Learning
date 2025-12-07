from openpyxl import Workbook

files = {
    "datafile-01-12-25 - 07-12-25-AWS.xlsx": [
        ["ResourceID", "Name", "Type", "Region"],
        ["aws-001", "EC2-Server-1", "EC2", "us-east-1"],
        ["aws-002", "S3-Bucket-Logs", "S3", "us-east-1"],
    ],
    "datafile-01-12-25 - 07-12-25-Azure.xlsx": [
        ["ResourceID", "Name", "Type", "Region"],
        ["az-001", "VM-Prod-1", "VirtualMachine", "East US"],
        ["az-002", "Storage-Acc-01", "StorageAccount", "East US"],
    ],
    "12-2025-AWS-data.xlsx": [
        ["ResourceType", "Count"],
        ["EC2", 5],
        ["S3", 12],
        ["Lambda", 7],
    ],
    "12-2025-Azure-data.xlsx": [
        ["ResourceType", "Count"],
        ["VirtualMachine", 9],
        ["StorageAccount", 4],
        ["Functions", 3],
    ],
}

for filename, rows in files.items():
    wb = Workbook()
    ws = wb.active
    for row in rows:
        ws.append(row)
    wb.save(filename)

print("Files created successfully!")
