from src.real_estate_broker import real_estate_broker

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])
    m = int(nm[1])

    clients = []
    for _ in range(n):
        clients.append(list(map(int, input().rstrip().split())))

    houses = []
    for _ in range(m):
        houses.append(list(map(int, input().rstrip().split())))

    result = real_estate_broker(clients, houses)

    print(result)