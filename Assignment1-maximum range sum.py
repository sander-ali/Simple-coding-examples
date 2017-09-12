def find_max_sum_range(in_list):
    if len(in_list) == 0:
        raise Exception("List Empty") #List should not be empty

    temp_sum = max_sum = in_list[0]
    a = 0
    start_list = 0
    end_list = 0

    if any(x < 0 for x in in_list):
        for b in range(1, len(in_list)):
            if in_list[b] > (temp_sum + in_list[b]):
                temp_sum = in_list[b]
                a = b
            else:
                temp_sum += in_list[b]

            if temp_sum > max_sum:
                max_sum = temp_sum
                start_list = a
                end_list = b
        print ('maximum sum =', max_sum)
        print ('starting index = ', start_list, 'ending index =', end_list)
    else:
        max_sum = sum(in_list)
        print ('maximum sum =', max_sum)
        print ('starting index =', 0, 'ending index =', len(in_list))

find_max_sum_range([14, 14, 2, 11, -10, -20, 15, 6,-16, 10, -5, 2, -5, 4, -16, -8, -13, -1, 15, 8, 4, -9, -15, 16, -12, 14, 15, -2, 2, 9, 2, 0, 1 ])