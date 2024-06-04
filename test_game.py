import pytest
from game import BowlingGame

@pytest.fixture
def game():
    return BowlingGame()

def test_it_gives_0_score_for_new_game(game):
    assert game.total_score == 0

def test_it_starts_with_10_frames(game):
    assert len(game.frames) == 10
    
def test_it_starts_with_empty_frames(game):
    assert not any(game.frames)

def test_it_updates_the_score_after_a_gutter_roll(game):
    game.roll()

    assert game.total_score == 0

def test_it_updates_the_score_after_a_points_roll(game):
    game.roll(7)

    assert game.total_score == 7

def test_it_only_allows_positive_rolls(game):
    with pytest.raises(ValueError, match='invalid amount of pins'):
        game.roll(-1)

def test_it_adds_rolls_to_current_score(game):
    game.roll(1)
    game.roll(2)

    assert game.total_score == 3

def test_it_only_allows_rolls_up_to_ten(game):
    with pytest.raises(ValueError, match='invalid amount of pins'):
        game.roll(11)

def test_it_only_allows_frames_with_first_non_ten_roll_second_roll_can_not_exceed_ten(game):
    game.roll(9)
    with pytest.raises(ValueError, match='frame roll can\'t exceed 10'):
        game.roll(3)

def test_it_adds_score_to_a_frame(game):
    game.roll(0)
    assert game.frames[0] == 0

def test_it_adds_two_scores_to_a_frame(game):
    game.roll(1)
    game.roll(2)
    assert game.frames[0] == 3