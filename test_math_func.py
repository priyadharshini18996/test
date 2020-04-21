import math_func

def test_add():
    assert math_func.add(7,3)==10
    assert math_func.add(7)==9
    assert math_func.add(5)==7

def test_product():
    assert math_func.product(5,5)==25
    assert math_func.product(5)==10
    assert math_func.product(7)==14

def test_add_strings():
    result=math_func.add('helo',' world')
    assert result == 'helo world'
    assert type(result) is str
    assert 'helo' in result

def test_product_strings():
    assert math_func.product('helo ',3) == 'helo helo helo '
    result = math_func.product('helo ')
    assert result =='helo helo '
    assert type(result) is str
    assert 'helo' in result