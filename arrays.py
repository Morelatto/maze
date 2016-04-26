def average(array):
    a = sum(array)/len(array)
    return a


def change(array, x=20, y=20):
    for i, v in enumerate(array):
        if v > x:
            array[i] = y
    return array


def get_biggest_average(list_of_arrays):
    biggest_average = 0, []
    for array in list_of_arrays:
        new_array = change(array)
        array_average = average(new_array)
        if array_average > biggest_average[0]:
            biggest_average = array_average, array

    return biggest_average


def get_third_and_fifth_highest_number(array):
    sorted_array = sorted(array)
    return sorted_array[len(sorted_array) - 3], sorted_array[len(sorted_array) - 5]


def sum_by_remainder(array, x=4, n=6):
    result = 0
    for value in array:
        if value % n == x:
            result += value
    return result


def main():

    # 1
    list_of_arrays = [
        [12, 10, 8, 36, 12, 10, 0, 20, 0, 2],
        [28, 29, 11, 29, 2, 6, 4, 7, 13, 32],
        [21, 32, 32, 12, 31, 20, 16, 6, 7, 11],
        [32, 36, 17, 5, 10, 30, 20, 7, 33, 11],
        [28, 10, 21, 8, 15, 15, 38, 30, 13, 4],
        [16, 25, 15, 35, 4, 14, 22, 22, 39, 17],
        [18, 5, 11, 6, 34, 8, 21, 3, 19, 22],
        [1, 15, 38, 33, 17, 1, 3, 25, 22, 0],
        [31, 1, 6, 2, 2, 14, 37, 27, 14, 14],
        [2, 16, 2, 18, 16, 28, 25, 30, 8, 23]
    ]
    biggest_average = get_biggest_average(list_of_arrays)
    print(biggest_average[1], biggest_average[0], sep=" - ")

    # 2
    array = [20, 24, 22, 13, 34, 13, 14, 33, 41, 10,
             35, 1, 2, 24, 16, 20, 16, 23, 46, 41,
             31, 7, 49, 25, 34, 15, 17, 18, 1, 30,
             1, 17, 23, 43, 10, 4, 48, 44, 24, 23,
             30, 0, 34, 30, 33, 27, 20, 42, 25, 5]

    third = get_third_and_fifth_highest_number(array)
    result = sum(third)
    print(result)

    # 3

    array = [1, 28, 12, 31, 11, 5, 4, 30, 30, 8,
             9, 39, 2, 5, 33, 33, 37, 5, 12, 27,
             23, 39, 1, 36, 28, 33, 24, 5, 27, 36]

    result = sum_by_remainder(array)
    print(result)

main()
