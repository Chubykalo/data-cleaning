import csv

# Set up the CSV file
csvfile = open('SLE-15-GA.csv', 'w', newline='')
fieldnames = ['package', 'bugowner', 'email', 'first_manager', 'second_manager']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

# Parse the input text and write the rows to the CSV file
with open('SLE-15-GA.txt', 'r', encoding='utf-8') as input_file:
    for line in input_file:
        # Extract the package name
        package = line.split(' {')[0].strip()

        # Extract the data from the line
        data = line.split('{')[1].split('}')[0]

        # Split the data into a dictionary
        data_dict = {}

        for item in data.split('-'):

            if ':' not in item:
                continue

            key, value = item.strip().split(':', 1)
            data_dict[key.strip()] = value.strip()

        # Extract relevant data from the dictionary.

        # .get method dhecks for 'bugowner' key in the dictionary. Sets the variable to the dictionary value, and if it does not find it,
        # it sets an empty string.
        bugowner_data = data_dict.get("'bugowner'", '')
        if 'login: ' in bugowner_data:
            bugowner = bugowner_data.split('login: ')[1].strip()
        else:
            bugowner = bugowner_data.strip()

        email = data_dict.get('email', '')
        first_manager = data_dict.get('1st manager', '')
        second_manager = data_dict.get('2nd manager', '')

        # Strip any leading or trailing apostrophes from the 'bugowner' and 'second_manager' fields

        # ----------  I would like to refrain from using this piece of code, but I can't figure out a better way.
        bugowner = bugowner.strip("'")
        second_manager = second_manager.strip("'")
        # ----------

        # Write the data to the CSV file
        writer.writerow({
            'package': package,
            'bugowner': bugowner,
            'email': email,
            'first_manager': first_manager,
            'second_manager': second_manager,
        })

# Close the CSV file
csvfile.close()

print(data)
print(data_dict)