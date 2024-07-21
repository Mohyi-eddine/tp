import pytest
import rock_paper_scissors

main = rock_paper_scissors


@pytest.mark.parametrize("choice1,choice2,expected", [
    ("paper", "rock", True),
    ("rock", "scissors", True),
    ("scissors", "paper", True),
    ("scissors", "scissors", False),
    ("paper", "paper", False),
])
def test_players_proposition(choice1, choice2, expected):
    assert main.winning_answer(choice1, choice2) == expected


@pytest.mark.parametrize("choice,expected", [
    ("paper", True),
    ("rock", True),
    ("scissors", True),
    ("scissrs", False),
    ("papers", False),
])
def test_choice_check(choice, expected):
    assert main.choice_check(choice) == expected


@pytest.mark.parametrize("choice1,choice2,expected", [
    ("paper", "paper", True),
    ("rock", "rock", True),
    ("scissors", "scissors", True),
    ("scissrs", "papers", False),
    ("papers", "scissrs", False),
])
def test_check_tie(choice1, choice2, expected):
    assert main.check_tie(choice1, choice2) == expected
