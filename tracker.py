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

def show_summary(file_name):

    file_handle = open(file_name, "r")

    total = 0
    count = 0

    for line in file_handle:
        parts = line.split("|")

        productivity_part = parts[3]
        score = productivity_part.split("/")[0].strip()

        total = total + int(score)
        count = count + 1

    file_handle.close()

    if count > 0:
        avg_productivity = round((total / count), 1)

        print("\n--- Summary ---")
        print("Total entries:", count)
        print("Average productivity:", str(avg_productivity) + "/5")
    else:
        print("No entries yet")