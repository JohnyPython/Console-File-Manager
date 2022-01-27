from built_in_functions import find_numbers_fun, string_to_int, miles_to_kilometers, sorted_football_tams, math_sqrt_fun
from built_in_functions import math_pow_fun, math_hypot_fun, math_pi_fun
import math


# filter() testing


def test_filter_fun():
    mixed_list = [11, 12, 15, 17]
    assert find_numbers_fun(mixed_list, 11) == [11]


def test_filter_fun_two():
    mixed_list = [11, 12, 15, 17, 11, 11]
    assert len(find_numbers_fun(mixed_list, 11)) == 3


def test_filter_fun_three():
    mixed_list = [11, 12, 15, 17, 11, 11]
    assert type(find_numbers_fun(mixed_list, 11)) == list


# map() tasting


def test_map_function_one():
    int_list = ['1', '2', '3', '4', '5', '6', '7']
    assert sum(string_to_int(int_list)) == 28


def test_map_function_two():
    int_list = ['1', '2', '3', '4', '5', '6', '7']
    assert type(sum(string_to_int(int_list))) == int


def test_map_function_three():
    miles = [1.6, 4.5, 7.8, 9.9]
    assert sum(miles_to_kilometers(miles)) > sum(miles)


# sorted

def test_sorted_fun_one():
    teams = ['Chelsea', 'Tottenham', 'Manchester', 'Lester', 'Arsenal']
    assert sorted_football_tams(teams)[0] == 'Arsenal'


def test_sorted_fun_two():
    teams = ['Chelsea', 'Tottenham', 'Manchester', 'Lester', 'Arsenal']
    assert sorted_football_tams(teams)[-1] == 'Tottenham'


# math


def test_math_sqrt():
    assert math_sqrt_fun(4) == 2


def test_math_pow():
    assert math_pow_fun(3, 2) == 9


def test_math_hypot():
    # формула вычисляет гипотенузу треугольника с катетами X и Y (math.sqrt(x * x + y * y)).
    assert round(math_hypot_fun(3, 3), 5) == round((math.sqrt(3 * 3 + 3 * 3)), 5)


def test_pi_round():
    assert math_pi_fun(100) == 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679


