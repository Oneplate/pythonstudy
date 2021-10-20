newEngland = [["Massachusetts", 6692824], ["Connecticut", 3596080],
              ["Maine", 1328302], ["New Hampshire", 1323459],
              ["Rhode Island", 1051511], ["Vermont", 62630]]
"""

# What is the first item of newEngland?
print(newEngland[0])

# What is the second item?
print(newEngland[1])

# What is the name of the state in the second element? How do we get that?
print(newEngland[1][0])

# What is the population of the state in the second element?
print(newEngland[1][1])

"""

"""
def report1(state_data):
    print("Population, State")
    for state_item in state_data:
        print(state_item[1], state_item[0])

report1(newEngland)
"""

def report2(state_data):
    print("Population, State")
    for i in range(0, len(state_data)):
        print(state_data[i][1], state_data[i][0])

report2(newEngland)

def population(state_data):
    tot = 0
    num_states = len(state_data)
    for i in range(0, num_states):
        one_state = state_data[i]
        pop = one_state[1]
        tot = tot+pop
    print("The total population of this list of states is", tot)
    print("There are", num_states, "states in this list of states.")

population(newEngland)

