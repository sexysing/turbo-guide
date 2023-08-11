def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
def test_factorial():
    assert factorial(5) == 120
    assert factorial(4) == 24
    assert factorial(0) == 1
    assert factorial(1) == 1
    print("Everything passed")
test_factorial()