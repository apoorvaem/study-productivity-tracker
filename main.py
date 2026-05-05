import tracker

file_name = "data.txt"

while True:
    print("\nStudy Productivity Tracker")
    print("1. Add entry")
    print("2. View entries")
    print("3. Exit")

    option = input("Enter option: ")

    if option == "1":
        task = input("Task: ")
        hours = input("Hours: ")
        priority = input("Priority (low/medium/high): ")
        productivity = input("Productivity (1-5): ")

        tracker.add_entry(file_name, task, hours, priority, productivity)
    
    elif option == "2":
        tracker.view_entries(file_name)

    elif option == "3":
        break