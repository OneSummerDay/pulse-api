import pytest
from pulse.http_status import is_successful_status


@pytest.mark.parametrize(
    ("status_code", "expected"),
    [
        (199, False),
        (200, True),
        (201, True),
        (204, True),
        (299, True),
        (300, False),
        (404, False),
        (500, False),
    ],
)
def test_http_status_classification(
    status_code: int,
    expected: bool,
) -> None:
    assert is_successful_status(status_code) is expected
