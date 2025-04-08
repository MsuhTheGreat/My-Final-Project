from project import start_playing_quiz, start_using_world_clock, start_playing_old_games


def test_start_playing_quiz():
    result = start_playing_quiz()
    assert result == "Yeah! I am playing quiz!"


def test_start_using_world_clock():
    result = start_using_world_clock()
    assert result == "Oh! This world clock is very useful!"


def test_start_playing_old_games():
    result = start_playing_old_games()
    assert result == "Finally! Some good old games to play!"
