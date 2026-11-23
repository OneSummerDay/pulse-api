from pulse.http_status import is_successful_status_code


def test_is_successful_status_code() -> None:
    assert is_successful_status_code(200) == True
    assert is_successful_status_code(299) == True


def test_is_unsuccessful_status_code() -> None:
    assert is_successful_status_code(300) == False
    assert is_successful_status_code(199) == False
