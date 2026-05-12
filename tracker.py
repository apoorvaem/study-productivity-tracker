def add_entry(file_name, task, hours, priority, productivity):
    
    priority = priority.lower()
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
        print("No entries yet.")

def search_entries(file_name, keyword):

    file_handle = open(file_name, "r")

    keyword = keyword.lower()
    found = False

    print("\n--- Search Results ---")

    for line in file_handle:
        if keyword in line.lower():
            print(line)
            found = True

    file_handle.close()

    if found == False:
        print("Entry not found.")

def delete_entry(file_name, keyword):

    file_handle = open(file_name, "r")

    lines = file_handle.readlines()
    file_handle.close()

    keyword = keyword.lower()

    new_lines = []
    found = False

    for line in lines:
        if keyword not in line.lower():
            new_lines.append(line)
        else:
            found = True

    file_handle = open(file_name, "w")

    for line in new_lines:
        file_handle.write(line)

    file_handle.close()

    if found:
        print("Entry deleted.")
    else:
        print("Entry not found.")
