"""
This module contains tests for the real_estate_broker function from the real_estate_broker module,
testing various scenarios to ensure correct behavior across typical, boundary, and edge cases.
"""
from src.real_estate_broker import real_estate_broker


# from pytest import mark  # Uncomment if specific pytest decorators are needed

def test_basic_matching():
    """
    Test that two houses perfectly matching the requirements of two clients result in two matches.
    """
    clients = [(1, 100), (2, 200)]
    houses = [(3, 99), (4, 199)]
    assert real_estate_broker(clients, houses) == 2


def test_no_matching():
    """
    Test that no houses meet the clients' requirements resulting in zero matches.
    """
    clients = [(1, 100), (2, 200)]
    houses = [(1, 101), (2, 201)]
    assert real_estate_broker(clients, houses) == 0


def test_partial_matching():
    """
    Test that out of three clients, only two can be matched based on their house requirements.
    """
    clients = [(1, 100), (2, 200), (3, 300)]
    houses = [(2, 99), (3, 199), (4, 299)]
    assert real_estate_broker(clients, houses) == 2


def test_all_houses_cheaper():
    """
    Test that all houses are cheaper than the max price and satisfy the area requirement,
    resulting in matches for all clients.
    """
    clients = [(1, 100), (2, 200)]
    houses = [(2, 50), (2, 150)]
    assert real_estate_broker(clients, houses) == 2


def test_all_houses_expensive():
    """
    Test that all houses are too expensive for any client to afford, resulting in zero matches.
    """
    clients = [(1, 100), (2, 200)]
    houses = [(2, 300), (2, 400)]
    assert real_estate_broker(clients, houses) == 0


def test_clients_high_demand_low_budget():
    """
    Test that clients with high area demands but low budgets cannot be matched to any houses.
    """
    clients = [(10, 10), (20, 20)]
    houses = [(5, 15), (15, 25)]
    assert real_estate_broker(clients, houses) == 0


def test_edge_cases():
    """
    Test edge cases where the client's requirement exactly matches a house's specifications.
    In this scenario, the house does not strictly exceed the area requirement, thus no match.
    """
    clients = [(1, 100)]
    houses = [(1, 100)]
    assert real_estate_broker(clients, houses) == 0


def test_empty_lists():
    """
    Test the scenario where there are no clients or houses, expecting zero matches.
    """
    clients = []
    houses = []
    assert real_estate_broker(clients, houses) == 0


def test_houses_just_right():
    """
    Test that all clients can be matched with houses that exactly meet their area requirements and are within budget.
    """
    clients = [(1, 100), (2, 200), (3, 300)]
    houses = [(2, 100), (3, 200), (4, 300)]
    assert real_estate_broker(clients, houses) == 3
