def add_entry(file_name, task, hours, priority, productivity):
    
    priority = priority.lower()

    if priority == "low":
        priority_value = 1
    elif priority == "medium":
        priority_value = 2
    elif priority == "high":
        priority_value = 3
    
    file_handle = open(file_name, "a")

    entry = task + " | " + str(hours) + " hour(s) | " + priority + " | " + str(productivity) + "/5\n"
    file_handle.write(entry)

    file_handle.close()

def view_entries(file_name):
    file_handle = open(file_name, "r")

    for line in file_handle:
        print(line)

    file_handle.close()