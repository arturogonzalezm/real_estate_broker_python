import pytest

from src.real_estate_broker import real_estate_broker


def test_basic_matching():
    clients = [(1, 100), (2, 200)]
    houses = [(3, 99), (4, 199)]
    assert real_estate_broker(clients, houses) == 2


def test_no_matching():
    clients = [(1, 100), (2, 200)]
    houses = [(1, 101), (2, 201)]
    assert real_estate_broker(clients, houses) == 0


def test_partial_matching():
    clients = [(1, 100), (2, 200), (3, 300)]
    houses = [(2, 99), (3, 199), (4, 299)]
    assert real_estate_broker(clients, houses) == 2


def test_all_houses_cheaper():
    clients = [(1, 100), (2, 200)]
    houses = [(2, 50), (2, 150)]
    assert real_estate_broker(clients, houses) == 2


def test_all_houses_expensive():
    clients = [(1, 100), (2, 200)]
    houses = [(2, 300), (2, 400)]
    assert real_estate_broker(clients, houses) == 0


def test_clients_high_demand_low_budget():
    clients = [(10, 10), (20, 20)]
    houses = [(5, 15), (15, 25)]
    assert real_estate_broker(clients, houses) == 0


def test_edge_cases():
    clients = [(1, 100)]
    houses = [(1, 100)]
    assert real_estate_broker(clients, houses) == 0


def test_empty_lists():
    clients = []
    houses = []
    assert real_estate_broker(clients, houses) == 0


def test_houses_just_right():
    clients = [(1, 100), (2, 200), (3, 300)]
    houses = [(2, 100), (3, 200), (4, 300)]
    assert real_estate_broker(clients, houses) == 3
