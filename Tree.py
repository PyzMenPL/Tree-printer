def tree():
    amount_of_segments = input("Tree segments: ")

    # Validation
    if amount_of_segments.isdigit():
        amount_of_segments = int(amount_of_segments)
    else:
        print("Given input is not a number!")
        return

    if not amount_of_segments:
        print("Given number is too low!")
        return

    # Variables
    layer = 0
    leafs = 1
    offset = 5 + amount_of_segments * 4
    segments_to_go = amount_of_segments

    # Main loop
    while segments_to_go:
        print((" " * offset) + ("*" * leafs))
        leafs += 2
        offset -= 1
        layer += 1

        if layer % 5 == 0:
            layer = 0
            leafs -= 6
            offset += 3
            segments_to_go -= 1

    print(((" " * (offset + (2 * amount_of_segments) - 1)) + "***\n") * 3)


if __name__ == "__main__":
    while True:
        tree()
