from typing import Union
import re


def get_filter(data: list, value: str) -> list:
    check_type(data)
    if not isinstance(value, str):
        raise TypeError
    return list(filter(lambda line: value in line.lower(), data))


def get_map(data: list, val: Union[int, str]) -> list:
    check_type(data)
    try:
        value = int(val)
    except Exception:
        raise TypeError
    return list(map(lambda line: parse_string(line)[value - 1] + '\n', data))


def get_unique(data: list, value=None) -> list:
    check_type(data)
    return list(set(data))


def get_sort(data: list, value: str) -> list:
    check_type(data)
    if value not in ['asc', 'decs']:
        raise ValueError
    return sorted(data, reverse=(value == 'desc'))


def get_limit(data: list, value: Union[str, int]) -> list:
    check_type(data)
    try:
        value = int(value)
    except Exception:
        raise TypeError
    return data[:value]


def get_regexp(data: list, value: str) -> list:
    check_type(data)
    return list(filter(lambda rec: re.search(value, rec), data))


def parse_string(string: str) -> list:
    return string.split()


def check_type(data) -> None:
    if not isinstance(data, list):
        raise TypeError
