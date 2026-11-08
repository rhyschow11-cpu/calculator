from calculator import add, subtract, multiply, divide

def test_add():
	assert add(2, 3) == 5

def test_divide():
	assert divide(6, 2) == 3

def test_subtract():
	assert subtract(8, 6) == 2

def test_multiply():
	assert multiply(2, 3) == 6 

def test_negative():
	assert add(2, -4) == -2
