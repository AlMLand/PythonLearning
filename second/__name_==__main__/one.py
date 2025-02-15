from two import print_two


def print_one():
    print_two()


if __name__ == "__main__":
    print("ONE run directly")
else:
    print("ONE is imported")
