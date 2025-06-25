from times import time_range, compute_overlap_time

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    
    assert result == expected

def test_no_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-13 10:30:00", "2010-01-13 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = []
    
    assert result == expected

def test_multi_intervals():
    large = time_range("2025-01-01 00:00:00", "2025-01-01 00:11:00", 2, 60)
    short = time_range("2025-01-01 00:02:00", "2025-01-01 00:12:00", 4, 120)
    result = compute_overlap_time(large, short)
    print(result)
    expected = [('2025-01-01 00:02:00', '2025-01-01 00:03:00'),
                ('2025-01-01 00:08:00', '2025-01-01 00:09:00')] 
    assert result == expected

def test_edge_case():
    first = time_range("2025-06-25 00:00:00", "2025-06-25 00:11:00")
    second = time_range("2025-06-25 00:11:00", "2025-06-25 00:22:00")
    result = compute_overlap_time(first, second)
    expected = []
    assert result == expected