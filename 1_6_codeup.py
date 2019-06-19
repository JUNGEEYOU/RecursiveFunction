
"""
    문제: 피보나치 수열이란 앞의 두 수를 더하여 나오는 수열이다.
    입력: 자연수 N이 입력된다. (N은 20보다 같거나 작다.)
    출력: 피보나치 수 출력
"""
def get_fibonacci_num(sel_index):
    """
    :param sel_index:
    :return:
    """
    if(sel_index < 3):
        return 1
    else:
        return get_fibonacci_num(sel_index -1) + get_fibonacci_num(sel_index-2)

num = input()
print(get_fibonacci_num(int(num)))