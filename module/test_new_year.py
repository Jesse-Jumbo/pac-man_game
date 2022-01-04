this_year = {"fortune": "", "body": "", "life": ""}


def is_good_luck(fortune):
    for chance in fortune:
        if "un" in chance:
            continue
        this_year["fortune"] = chance
        if this_year["fortune"] == "good_luck":
            return True
        else:
            return False


def is_healthy(body):
    for today in body:
        if "un" in today:
            continue
        this_year["body"] = today
        if this_year["body"] == "healthy":
            return True
        else:
            return False


def is_happy(life):
    for today in life:
        if "un" in today:
            continue
        this_year["life"] = today
        if this_year["life"] == "happy":
            return True
        else:
            return False


def is_unluck(fortune):
    for chance in fortune:
        if "un" in str(chance):
            return False


def is_unhealthy(body):
    for today in body:
        if "un" in today:
            return False


def is_unhappy(life):
    for today in life:
        if "un" in today:
            return False


def test_new_year_fortune():
    new_year = {"fortune": ["good_luck", "unlucky"]}
    assert is_good_luck(new_year["fortune"]) == True
    assert is_unluck(new_year["fortune"]) == False


def test_new_year_body():
    new_year = {"body": ["healthy", "unhealthy"]}
    assert is_healthy(new_year["body"]) == True
    assert is_unhealthy(new_year["body"]) == False


def test_new_year_life():
    new_year = {"life": ["happy", "unhappy"]}
    assert is_happy(new_year["life"]) == True
    assert is_unhappy(new_year["life"]) == False


def test_this_year():
    assert this_year == {"fortune": "good_luck", "body": "healthy", "life": "happy"}
