"""Module to match clients with houses based on requirements using the real_estate_broker function."""

from src.real_estate_broker import real_estate_broker


def main():
    """
    Main function to read client and house data, compute matches, and print the result.
    :return: None
    :rtype: None
    """
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    clients = []
    for _ in range(n):
        clients.append(list(map(int, input().rstrip().split())))

    houses = []
    for _ in range(m):
        houses.append(list(map(int, input().rstrip().split())))

    # Result is not a constant, it's a variable holding the function output, naming it in lower case is appropriate
    result = real_estate_broker(clients, houses)
    print(result)


if __name__ == '__main__':
    main()
