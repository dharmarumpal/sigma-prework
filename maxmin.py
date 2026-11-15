

# RETURN HIGHEST AND LOWEST NUMBERS IN A LIST OF INTEGERS WITHOUT USING MAX OR MIN

def min_max_from_list(list_of_integers):
    list_of_integers = sorted(list_of_integers)
    final_list = []
    final_list.append(list_of_integers[0])
    final_list.append(list_of_integers[-1])
    return final_list


def generate_list_of_integers():
    list_of_integers = []
    i = 0

    num_of_integers = int(
        input("How many numbers would you like to input into the list? "))

    for i in range(num_of_integers):
        list_of_integers.append(int(input("Please enter a number: ")))
    return list_of_integers


integers = generate_list_of_integers()
print("Here is the lowest and highest integer in the list: ")
print(min_max_from_list(integers))
