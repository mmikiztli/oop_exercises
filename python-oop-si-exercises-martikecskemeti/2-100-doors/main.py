from door import Door


# Generates as many Door instances in a list, as the given count said
# and takes care of assignnin.join(open_door_ids)g the correct id to the Door from 1
#
# Arg:
#   - count: integer - number of Door instances in the returned list (default=100)
# Return: List of Door object instances with defined id values
def generate_doors(count=100):
    return [Door(i) for i in range(1, count + 1)]


# Does the main 100 logic. Goes through all the Door instances by the rules of 100 Doors
#
# Arg:
#   - doors: list of Door objects
# Return: list of toggled Door instances
def toggle_doors(doors):
    for i in range(1, len(doors) + 1):
        for j in range(i, len(doors) + 1, i):
            if doors[j - 1].id == j:
                Door.toggle(doors[j - 1])
    return doors


# Collects the ids of the open Doors form the given Door list
#
# Arg:
#   - doors: list of (preferably toggled) Door objects
# Return: list of open Door ids as strings
def collect_open_doors(doors):
    return [str(door.id) for door in doors if door.is_open == True]


# Formats a string list into a printable string
#
# Arg:
#   - open_door_list: list of strings
# Return: string - comma separated values from the string list
def format_open_door_names(open_door_ids):
    return ", ".join(open_door_ids)


# Main logic of the 100doors example script
# This should only call lower level functions and print out the result
#
# Arg:
#   - door_count: Number of doors in the example (default=100)
def main(door_count=100):
    doors = generate_doors(door_count)
    toggled_doors = toggle_doors(doors)
    open_doors = collect_open_doors(toggled_doors)
    print("The following doors are left open: " +
          format_open_door_names(open_doors))

if __name__ == '__main__':
    main(100)
