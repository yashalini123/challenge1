def third_highest_frequency(numbers):
    # Create a dictionary to store the frequency of each number
    frequency = {}

    # Count the frequency of each number in the list
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    # Sort the dictionary by values (frequency) in descending order
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    # Find the key (number) corresponding to the third highest frequency
    if len(sorted_frequency) >= 3:
        third_highest = sorted_frequency[2][0]
        return third_highest
    else:
        return None  # Return None if there are less than three unique numbers in the list


# Example usage:
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
result = third_highest_frequency(numbers)
if result is not None:
    print(f"The integer with the third highest frequency is: {result}")
else:
    print("There are less than three unique numbers in the list.")