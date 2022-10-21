def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")