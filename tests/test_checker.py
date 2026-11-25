from unittest.mock import AsyncMock

import httpx

from pulse import checker


def test_main_reports_http_response(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        checker,
        "check_example",
        AsyncMock(return_value=500),
    )

    assert checker.main() == 0
    assert "HTTP status: 500" in capsys.readouterr().out


def test_main_handles_timeout(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        checker,
        "check_example",
        AsyncMock(side_effect=httpx.ReadTimeout("Read timed out")),
    )

    assert checker.main() == 1
    assert "ReadTimeout" in capsys.readouterr().err
