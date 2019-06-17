def odd_num(start, end):
    """
    인자 start, end 값 사이의 홀수 값 출력하기
    :param start:
    :param end:
    :return:
    """
    if (start > end):
        return
    else:
        if (start % 2 == 1):
            print(start)
        return odd_num(start + 1,end)

a, b = input().split()
odd_num(int(a), int(b))


