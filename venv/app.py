def solution(number):
    binary_form = bin(number)[2:]  # binary format starts with "0b...", so the first 2 chars are removed

    print(binary_form)

    longest_gap = 0
    index = 0

    while index != -1:
        index = binary_form.find("1")  # if "1" is not found then it returns -1, terminates while loop

        if index > longest_gap:
            longest_gap = index

        binary_form = binary_form[index + 1:]

    return longest_gap
