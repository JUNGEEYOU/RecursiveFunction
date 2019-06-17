import sys
def sum_integer(end):
    """
    1~ end 값 합
    :param end:
    :return:
    """
    if(end==0):
        return 0
    else:
        return end + sum_integer(end-1)

sys.setrecursionlimit(50000)   # RecursionError: maximum recursion depth exceeded in comparison 에러로 인해 추가
a = input()
print(sum_integer(int(a)))