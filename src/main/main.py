import csv
import sqlite3

# Connect to the SQLite in-memory database
conn = sqlite3.connect(':memory:')

# A cursor object to execute SQL commands
cursor = conn.cursor()


def main():

    # users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        userId INTEGER PRIMARY KEY,
                        firstName TEXT,
                        lastName TEXT
                      )'''
                   )

    # callLogs table (with FK to users table)
    cursor.execute('''CREATE TABLE IF NOT EXISTS callLogs (
        callId INTEGER PRIMARY KEY,
        phoneNumber TEXT,
        startTime INTEGER,
        endTime INTEGER,
        direction TEXT,
        userId INTEGER,
        FOREIGN KEY (userId) REFERENCES users(userId)
    )''')

    # You will implement these methods below. They just print TO-DO messages for now.
    load_and_clean_users('../../resources/users.csv')
    load_and_clean_call_logs('../../resources/callLogs.csv')
    write_user_analytics('../../resources/userAnalytics.csv')
    write_ordered_calls('../../resources/orderedCalls.csv')

    # Helper method that prints the contents of the users and callLogs tables. Uncomment to see data.
    # select_from_users_and_call_logs()

    # Close the cursor and connection. main function ends here.
    cursor.close()
    conn.close()


# TODO: Implement the following 4 functions. The functions must pass the unit tests to complete the project.


# This function will load the users.csv file into the users table, discarding any records with incomplete data

def load_and_clean_users(file_path):

    # load file
    with open(file_path, "r") as user_data:
        next(user_data) # skip header row
        
        with open(file_path, "r") as call_logs:
        next(call_logs)
        
        for user in user_data:
            values = get_values(user, 2)
            if values is None:
                continue
            cursor.execute("INSERT INTO users (firstName, lastName) VALUES (?,?)", (first_name, last_name))
        conn.commit()

    print("TODO: load_users") Dont Need anymore


# - Load the callLogs.csv file found in /resources into the callLogs table 
# - Clean the data before insertion. In this project, you just have to leave out any records with missing values or too many values.
# - HINT: For every record in callLogs.csv, make sure it has the correct number of fields and no empty values before inserting into the Database.

# This function will load the callLogs.csv file into the callLogs table, discarding any records with incomplete data
def load_and_clean_call_logs(file_path):
    with open(file_path, "r") as call_logs:
        next(call_logs)
        
        for call in call_logs:
            values = get_values(call, 5)
            if values is None:
                continue
            cursor.execute("INSERT INTO callLogs (phoneNumber, startTime, endTime, direction, userId) VALUES (?,?,?,?,?)", values)
        conn.commit()
    print("TODO: load_call_logs")

def get_values(row, num_of_values):
    # pulls data from a row and returns None if not validated or a list if validated
    values = row.strip().split(",")

    if len(values) != num_of_values:
        return None

    for index in range(len(values)): 
        values[index] = values[index].strip()
        if values[index] == "":
            return None

    return values

# - Save analytic data for users into a csv file. The file must be named userAnalytics.csv, and it must be in the /resources folder
# - Records must include userId, avgDuration, numCalls. Example:
#   ```
#   userId,avgDuration,numCalls
#   1,105.0,4
#   ```
# - HINT: This data will be selected from the callLogs table.
# - HINT 2: Dictionaries will be very helpful for matching data with userIds. Consider one for {userId, average call duration} and one for {userId, number of calls}. 

# This function will write analytics data to testUserAnalytics.csv - average call time, and number of calls per user.
# You must save records consisting of each userId, avgDuration, and numCalls
# example: 1,105.0,4 - where 1 is the userId, 105.0 is the avgDuration, and 4 is the numCalls.
def write_user_analytics(csv_file_path):

    print("TODO: write_user_analytics")



# - Save call logs into csv files, ordered by userId, then start time. The file must be named orderedCallLogs.csv
# - HINT: This data will be selected from the callLogs table.
# - HINT 2: You can make use of ORDER BY to greatly simplify your python logic

# *General note - each of these functions take a "file_path" parameter. You will not need to edit this variable, but it will be used to accomplish each implementation. See main() for an example of the function invocations with file paths from /resources.

# This function will write the callLogs ordered by userId, then start time.
# Then, write the ordered callLogs to orderedCalls.csv
def write_ordered_calls(csv_file_path):

    print("TODO: write_ordered_calls")



# No need to touch the functions below!------------------------------------------

# This function is for debugs/validation - uncomment the function invocation in main() to see the data in the database.
def select_from_users_and_call_logs():

    print()
    print("PRINTING DATA FROM USERS")
    print("-------------------------")

    # Select and print users data
    cursor.execute('''SELECT * FROM users''')
    for row in cursor:
        print(row)

    # new line
    print()
    print("PRINTING DATA FROM CALLLOGS")
    print("-------------------------")

    # Select and print callLogs data
    cursor.execute('''SELECT * FROM callLogs''')
    for row in cursor:
        print(row)


def return_cursor():
    return cursor


if __name__ == '__main__':
    main()
