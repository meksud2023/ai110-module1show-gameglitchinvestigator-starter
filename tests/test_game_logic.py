from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_too_high_hint():
    # A guess of 60 against a secret of 50 should be "Too High".
    assert check_guess(60, 50) == "Too High"


def test_hints_are_not_inverted():
    # Regression test for the bug we fixed: a guess ABOVE the secret must
    # report "Too High" and a guess BELOW must report "Too Low". The original
    # code returned these swapped, telling the player to go the wrong way.
    secret = 50
    for guess in (51, 75, 99):
        assert check_guess(guess, secret) == "Too High", (
            f"{guess} > {secret} should be 'Too High', not the inverted hint"
        )
    for guess in (1, 25, 49):
        assert check_guess(guess, secret) == "Too Low", (
            f"{guess} < {secret} should be 'Too Low', not the inverted hint"
        )


def test_check_guess_returns_plain_string():
    # The broken version returned an (outcome, message) tuple, which silently
    # broke comparisons elsewhere. Pin the contract: a single string.
    assert check_guess(50, 50) == "Win"
    assert isinstance(check_guess(50, 50), str)
