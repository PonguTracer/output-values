def get_user_values(nums):

    while True:
        # Get user input
        user_input = input()
        # Split the string into a list of strings
        user_input = user_input.split()
        # Convert the list of strings into a list of integers
        if user_input[0] == '-1':
            break

        for i in user_input:
            nums.append(int(i))


def output_ints_less_than_or_equal_to_threshold(nums, threshold):
    # Iterate through the list
    for i in nums:
        # Check if the current list element is less than or equal to the threshold
        if i <= threshold:
            # If so, print it
            print(i)

threshold = int(input())
nums = []

get_user_values(nums)
output_ints_less_than_or_equal_to_threshold(nums, threshold)
