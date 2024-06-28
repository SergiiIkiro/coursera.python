# Assign `username_list` to the list of usernames who are allowed to access the device

username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]

# Display the initial `username_list`
print(username_list)

# Assign `username_list` to the updated list of usernames who are allowed to access the device
username_list = ["madebowa", "jnguyen",
                 "tbecker", "nhersh", "redwards", "lpope"]

# Display the updated `username_list`
print(username_list)
# Assign `max_logins` to the value 3
max_logins = 3

# Assign `max_logins_type` to the data type of `max_logins`
max_logins_type = type(max_logins)

# Display `max_logins_type`
print(max_logins_type)

username = ["elarson", "bmoreno", "tshah"]

data_type = type(username)

print(data_type)

# Iterative statement using `for`, `range()`, and a loop variable of `i`
# Display "Connection could not be established." three times

for i in range(3):
    print("Connection could not be established.")


username = "elarson"


def identify_user():
    print(username)


identify_user()
