def find_most_frequent(a_list):

    counts = {}
    for num in a_list:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    most_occuring = []
    highest_count = 0

    for num in counts:
        if counts[num] > highest_count:
            highest_count = counts[num]
            most_occuring = [num]
        elif counts[num] == highest_count:
            most_occuring.append(num)

    return most_occuring


my_list = [2, 1, 2, 5, 4]
result = find_most_frequent(my_list)
print(result)


#def find_most_frequent(a_list):
#    most_occuring = []
#    highest_count = 0
#    
#    # We use a set just to avoid checking the same number twice
#    # (Optional, but makes it much faster)
#    checked_numbers = []
#
#    for num in a_list:
#        # Skip if we already counted this specific number
#        if num in checked_numbers:
#            continue
#        
#        # 1. Count appearances of 'num' manually
#        current_count = 0
#        for x in a_list:
#            if x == num:
#                current_count += 1
#        
#        # 2. Track it as we did before
#        if current_count > highest_count:
#            highest_count = current_count
#            most_occuring = [num]
#        elif current_count == highest_count:
#            most_occuring.append(num)
#            
#        checked_numbers.append(num)
#
#    return most_occuring
#
#my_list = [2, 1, 2, 5, 4]
#print(find_most_frequent(my_list))


