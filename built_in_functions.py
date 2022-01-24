# filter(func, iterable)
import math


def find_numbers_fun(mixed_list, find_num):
    return list(filter(lambda x: x == find_num, mixed_list))


# map


def string_to_int(string_list):
    return list(map(int, string_list))


def miles_to_kilometers(miles):
    return list(map(lambda x: x * 1.6, miles))


# sorted()

def sorted_football_tams(teams):
    return sorted(teams)


# math.sqrt


def math_sqrt_fun(a):
    return math.sqrt(a)


# math.pow


def math_pow_fun(x, y):
    return math.pow(x, y)


# math.hypot


def math_hypot_fun(x, y):
    return math.hypot(x, y)


# math.pi

def math_pi_fun(round_points):
    return round(math.pi, round_points)
