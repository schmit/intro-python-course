from primes import is_prime

def test_is_zero_prime():
    assert not is_prime(0)

def test_is_one_prime():
    assert not is_prime(1)

def test_is_two_prime():
    assert is_prime(2)

def test_is_three_prime():
    assert is_prime(3)

def test_is_four_prime():
    assert not is_prime(4)


