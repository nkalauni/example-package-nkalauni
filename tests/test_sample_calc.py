import sample_calc as sc

def test_func_for_positive_int():
    input_value = 3                     # 1. test input
    func_output = sc.func(input_value)  # 2. call function
    assert func_output == 4             # 3. compare output with expected

def test_func_for_negative_int():
    input_value = -5
    func_output = sc.func(input_value)
    assert func_output == -4

def test_func_for_zero():
    input_value = 0
    func_output = sc.func(input_value)
    assert func_output == 1