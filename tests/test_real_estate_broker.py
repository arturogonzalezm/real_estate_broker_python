"""
This module contains tests for the real_estate_broker function from the real_estate_broker module,
testing various scenarios to ensure correct behavior across typical, boundary, and edge cases.
"""
from src.real_estate_broker import real_estate_broker


# from pytest import mark  # Uncomment if specific pytest decorators are needed

def test_basic_matching():
    """
    Tests that the correct number of matches are found when there are ideal conditions.
    """
    clients = [(1, 100), (2, 200)]
    houses = [(3, 99), (4, 199)]
    assert real_estate_broker(clients, houses) == 2


def test_no_matching():
    """
    Tests that no matches are made when no houses meet the clients' requirements.
    """
    clients = [(1, 100), (2, 200)]
    houses = [(1, 101), (2, 201)]
    assert real_estate_broker(clients, houses) == 0


def test_partial_matching():
    """
    Tests that matches are made when houses meet the requirements of clients.
    Adjusted to reflect that all clients find suitable houses.
    """
    clients = [(1, 100), (2, 200), (3, 300)]
    houses = [(2, 99), (3, 199), (4, 299)]
    assert real_estate_broker(clients, houses) == 3  # Adjusted expected result to 3


def test_all_houses_cheaper():
    """
    Tests that all clients can be matched when all houses are within the budget and area requirements.
    """
    clients = [(1, 100), (2, 200)]
    houses = [(2, 50), (3, 150)]
    assert real_estate_broker(clients, houses) == 2


def test_all_houses_expensive():
    """
    Tests that no clients are matched when all houses are out of budget.
    """
    clients = [(1, 100), (2, 200)]
    houses = [(2, 300), (2, 400)]
    assert real_estate_broker(clients, houses) == 0


def test_clients_high_demand_low_budget():
    """
    Tests that no matches are made when clients have high demands but low budgets.
    """
    clients = [(10, 10), (20, 20)]
    houses = [(5, 15), (15, 25)]
    assert real_estate_broker(clients, houses) == 0


def test_edge_cases():
    """
    Tests edge cases where exact matches do not count as valid.
    """
    clients = [(1, 100)]
    houses = [(1, 100)]
    assert real_estate_broker(clients, houses) == 0


def test_empty_lists():
    """
    Tests that no matches are found when there are no clients or houses.
    """
    clients = []
    houses = []
    assert real_estate_broker(clients, houses) == 0


def test_houses_just_right():
    """
    Tests that all clients are matched when houses exactly meet their specifications.
    """
    clients = [(1, 100), (2, 200), (3, 300)]
    houses = [(2, 100), (3, 200), (4, 300)]
    assert real_estate_broker(clients, houses) == 3
