the_list = [2, 5, 7, 9, 20]
length_of_list = len(the_list)


def finding_the_largest(the_list):
    largest = the_list[0]

    for index in range(1, length_of_list):
        if the_list[index] > largest:
            largest = the_list[index]

    return largest

def finding_the_smallest(the_list):
    smallest = the_list[0]

    for index in range(1, length_of_list):
        if the_list[index] < smallest:
            smallest = the_list[index]

    return smallest

def calculating_the_range():
    largest_number = finding_the_largest(the_list)
    smallest_number = finding_the_smallest(the_list)

    the_range = largest_number - smallest_number

    return the_range

print(calculating_the_range())
