from math import sqrt


def length(v):
    return sqrt(v[0] ** 2 + v[1] ** 2)


def subtract(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1])


def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])


def translate(translation, vectors):
    """向量平移"""
    return [add(translation, v) for v in vectors]
