import pytest
from times import time_range, compute_overlap_time


@pytest.mark.parametrize(
    "test_input1, test_input2, expected",
    [
        pytest.param(
            time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
            time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
            [
                ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
                ("2010-01-12 10:38:00", "2010-01-12 10:45:00"),
            ],
            id="given input",
        ),
        pytest.param(
            time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
            time_range("2010-01-13 10:30:00", "2010-01-13 10:45:00", 2, 60),
            [],
            id="no overlap",
        ),
        pytest.param(
            time_range("2025-01-01 00:00:00", "2025-01-01 00:11:00", 2, 60),
            time_range("2025-01-01 00:02:00", "2025-01-01 00:12:00", 4, 120),
            [
                ("2025-01-01 00:02:00", "2025-01-01 00:03:00"),
                ("2025-01-01 00:08:00", "2025-01-01 00:09:00"),
            ],
            id="multiple intervals",
        ),
        pytest.param(
            time_range("2025-06-25 00:00:00", "2025-06-25 00:11:00"),
            time_range("2025-06-25 00:11:00", "2025-06-25 00:22:00"),
            [],
            id="edge case",
        ),
    ],
)
def test_eval(test_input1, test_input2, expected):
    assert compute_overlap_time(test_input1, test_input2) == expected
