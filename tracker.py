"""
Study Productivity Tracker - Functions

Author: Apoorva Eswara Murthi

Description:
    This file contains all main functionality for the Study Productivity Tracker.
    It handles file operations and data processing including:

        - Adding study entries
        - Viewing entries
        - Searching entries
        - Deleting entries
        - Generating productivity summary

    This module is used by main.py to manage all data operations.
"""

def add_entry(file_name, task, hours, priority, productivity):
    """
    PURPOSE:
        Adds a study session entry to the data file.

    PARAMETERS:
        file_name - file where entries are stored
        task - name of the task completed
        hours - number of hours spent
        priority - importance level (low/medium/high)
        productivity - productivity rating (1-5)

    RETURNS:
        None
    """
    
    # Convert priority input to lowercase.
    priority = priority.lower()

    # Open file in append mode.
    file_handle = open(file_name, "a")

    # Create entry line.
    entry = task + " | " + str(hours) + " hour(s) | " + priority + " | " + str(productivity) + "/5\n"
    
    # Write entry.
    file_handle.write(entry)

    # Close file.
    file_handle.close()

def view_entries(file_name):
    """
    PURPOSE:
        Displays all stored study session entries.

    PARAMETERS:
        file_name - file where entries are stored

    RETURNS:
        None
    """

    # Open file in read mode.
    file_handle = open(file_name, "r")

    # Print each entry.
    for line in file_handle:
        # Strip newline characters for cleaner display.
        print(line.strip())

    # Close file.
    file_handle.close()

def show_summary(file_name):
    """
    PURPOSE:
        Calculates and displays productivity statistics. This includes the total number of entries and the average productivity across all entries.
    
    PARAMETERS:
        file_name - file where entries are stored

    RETURNS:
        None
    """

    # Open file in read mode.
    file_handle = open(file_name, "r")

    total = 0
    count = 0

    # Process each entry
    for line in file_handle:
        # Split entry into respective components.
        parts = line.split("|")

        # Get productivity score.
        productivity_part = parts[3]
        score = productivity_part.split("/")[0].strip()

        total = total + int(score)
        count = count + 1

    # Close file.
    file_handle.close()

    # Display results.
    if count > 0:
        avg_productivity = round((total / count), 1)

        print("\n--- Summary ---")
        print("Total entries:", count)
        print("Average productivity:", str(avg_productivity) + "/5")
    else:
        print("No entries yet.")

def search_entries(file_name, keyword):
    """
    PURPOSE:
        Searches study session entries using a keyword.

    PARAMETERS:
        file_name - file where entries are stored
        keyword - word(s) to search for

    RETURNS:
        None
    """

    # Open file in read mode.
    file_handle = open(file_name, "r")

    keyword = keyword.lower()
    found = False

    print("\n--- Search Results ---")

    # Search through entries for keyword.
    for line in file_handle:
        if keyword in line.lower():
            # Remove trailing whitespace from file output.
            print(line.strip())
            found = True

    # Close File.
    file_handle.close()

    # Inform user if keyword is not found.
    if not found:
        print("Entry not found.")

def delete_entry(file_name, keyword):
    """
    PURPOSE:
        Delete study session entries that match the keyword from the file.

    PARAMETERS:
        file_name - file where entries are stored
        keyword - word(s) to find entries to delete.

    RETURNS:
        None
    """

    # Open file in read mode.
    file_handle = open(file_name, "r")

    # Read all lines in file.
    lines = file_handle.readlines()

    # Close file.
    file_handle.close()

    keyword = keyword.lower()

    new_lines = []
    found = False

    # Filter out entries that contain the keyword.
    for line in lines:
        if keyword not in line.lower():
            new_lines.append(line)
        else:
            found = True

    # Rewrite file without the entries containing the keyword.
    file_handle = open(file_name, "w")

    for line in new_lines:
        file_handle.write(line)

    # Close file.
    file_handle.close()

    # Inform user if entry is deleted or not found.
    if found:
        print("Entry deleted.")
    else:
        print("Entry not found.")
