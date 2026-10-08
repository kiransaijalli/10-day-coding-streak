# Day 7:Check Placement Eligibility

name = input("Enter Student Name: ")
cgpa = float(input("Enter CGPA: "))
attendance = float(input("Enter Attendance Percentage: "))
backlogs = int(input("Enter Number of Backlogs: "))
# Check eligibility
if cgpa >= 7.0 and attendance >= 75 and backlogs == 0:
    print("\n----- Placement Eligibility -----")
    print("Student Name:", name) 
    print("Status: Eligible for Placement")
else:
    print("\n----- Placement Eligibility -----")
    print("Student Name:", name) 
    print("Status: Not Eligible for Placement")