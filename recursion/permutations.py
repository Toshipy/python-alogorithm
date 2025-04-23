# from itertools import permutations
#
# for r in  permutations([1, 2, 3]):
#     print(r)

from typing import List

def all_perms(elements: List[int]) -> List[List[int]]:
    result = []
    # first = elements[0:1] #[1]
    rest = elements[1:] #[2, 3]

    if len(elements) <= 1:
        return [elements]

    for perm in all_perms(elements[1:]):
        for i in range(len(elements)):
            result.append(rest[:i] + elements[0:1] + rest[i:])
            # i=0 -> rest[:0]=[], first=[1], rest[0:]=[2,3] -> [1,2,3]
            # i=1 -> rest[:1]=[2], first=[1], rest[1:]=[3] -> [2,1,3]
            # i=2 -> rest[:2]=[2,3], first=[1], rest[2:]=[] -> [2,3,1]
    return result


if __name__ == '__main__':
    # all_perms([1, 2, 3])
    for p in all_perms([1, 2, 3]):
        print(p)

