from student_solution import determine_number_category

def test_case_1():
    assert determine_number_category(42) == 'Positive (Small)'

def test_case_2():
    assert determine_number_category(100) == 'Positive (Large)'

def test_case_3():
    assert determine_number_category(0) == 'Zero'

def test_case_4():
    assert determine_number_category(-3) == 'Negative'
