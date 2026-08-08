"""
Basic list operations
"""


def append(list1:list, list2:list) -> list:
    for item in list2:
        list1.append(item)
        
    return list1


def concat(lists: list[list]) -> list:
    
    concat_list = []
    for list_item in lists:
        concat_list.extend(list_item)
    
    return concat_list
    
    
def filter(function, list: list) -> list:
    
    if not list:
        return []

    filter_list = []
    for item in list:
        if function(item):
            filter_list.append(item)
            
    return filter_list


def length(list: list) -> int:
    count = 0
    for _ in list:
        count += 1
        
    return count 


def map(function, list: list) -> list:
    
    mapped_list = []
    for item in list:
        mapping = function(item)
        mapped_list.append(mapping)
        
    return mapped_list


def foldl(function, list: list, initial: int) -> int:
    
    in_accumulator = initial
    
    for item in list:
        in_accumulator = function(in_accumulator, item)
        
    return in_accumulator


def foldr(function, list: list, initial: int) -> int:
    
    in_accumulator = initial
    
    for item in list[::-1]:
        in_accumulator = function(in_accumulator, item)
        
    return in_accumulator


def reverse(list: list) -> list:
    
    reversed_list = []
    
    for item in list[::-1]:
        reversed_list.append(item)
        
    return reversed_list
