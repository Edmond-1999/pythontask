def most_occurring_count(my_list):

    count = 0

    for current_number in my_list:

        current_count = 0

        for number in my_list:
            if current_number == number:
                current_count += 1

        if current_count > count:
            count = current_count

    return count


my_list = [1, 5, 5, 6, 4]

print(most_occurring_count(my_list))
