#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：test
@File    ：review.py
@IDE     ：PyCharm
@Author  ：shiqinqin
@Date    ：2024/6/4 13:36
"""


# Review 1

# def add_to_list(value, my_list=[]):
#
#     my_list.append(value)
#
#     return my_list

# solution
def add_to_list(value, my_list=None):
    if my_list is None:
        return [value]
    my_list.append(value)
    return my_list

# Review 2

# def format_greeting(name, age):
#
#     return "Hello, my name is {name} and I am {age} years old."

# solution

def format_greeting(name, age):

    return f"Hello, my name is {name} and I am {age} years old."  # use format


# Review 3

# class Counter:
#     count = 0
#
#     def __init__(self):
#         self.count += 1
#
#     def get_count(self):
#         return self.count

# solution

class Counter:

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count


# Review 4

# import threading
#
#
# class SafeCounter:
#
#     def __init__(self):
#         self.count = 0
#
#     def increment(self):
#         self.count += 1
#
#
# def worker(counter):
#     for _ in range(1000):
#         counter.increment()
#
#
# counter = SafeCounter()
#
# threads = []
#
# for _ in range(10):
#     t = threading.Thread(target=worker, args=(counter,))
#
#     t.start()
#
#     threads.append(t)
#
# for t in threads:
#     t.join()


# solution
import threading


class SafeCounter:

    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:  # use thread lock
            self.count += 1


# Review 5

# def count_occurrences(lst):
#     counts = {}
#
#     for item in lst:
#
#         if item in counts:
#
#             counts[item] = + 1
#
#         else:
#
#             counts[item] = 1
#
#     return counts

# solution

def count_occurrences(lst):
    counts = {}

    for item in lst:

        if item in counts:

            counts[item] += 1  # = +  ---> +=

        else:

            counts[item] = 1

    return counts






