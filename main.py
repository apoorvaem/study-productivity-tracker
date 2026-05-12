"""
Study Productivity Tracker - Main Program

Author: Apoorva Eswara Murthi

Description:
    This file contains the user interface for the Study Productivity Tracker.
    It uses a menu-driven system that allows users to:
    
        - Add study entries
        - View all entries
        - Search entries
        - Delete entries
        - View productivity summary

    This file handles user input and connects to tracker.py for data processing.
"""

import tracker

file_name = "data.txt"

while True:
    # Display menu options.
    print("\nStudy Productivity Tracker")
    print("1. Add entry")
    print("2. View entries")
    print("3. Search entries")
    print("4. Delete entry")
    print("5. Show summary")
    print("6. Exit")

    option = input("Enter option: ")

    # Add entry.
    if option == "1":
        task = input("Task: ")

        # Validate hours input.
        while True:
            hours = input("Hours: ")
            try:
                float(hours)
                break
            except:
                print("Invalid input. Please enter a number.")

        # Validate priority input.
        while True:
            priority = input("Priority (low/medium/high): ").lower()

            if priority == "low" or priority == "medium" or priority == "high":
                break
            else:
                print("Invalid input. Please enter low, medium, or high.")

        # Validate productivity input.
        while True:
            productivity = input("Productivity (1-5): ")

            if productivity.isdigit():
                value = int(productivity)

                if value >= 1 and value <= 5:
                    break

            print("Invalid input. Please enter an integer between 1 and 5.")

        tracker.add_entry(file_name, task, hours, priority, productivity)
    
    # View entries.
    elif option == "2":
        tracker.view_entries(file_name)

    # Search entries.
    elif option == "3":
        keyword = input("Enter keyword to search: ")
        tracker.search_entries(file_name, keyword)

    # Delete entry.
    elif option == "4":
        keyword = input("Enter keyword to delete: ")
        tracker.delete_entry(file_name, keyword)

    # Show summary.
    elif option == "5":
        tracker.show_summary(file_name)

    # Exit program.
    elif option == "6":
        break