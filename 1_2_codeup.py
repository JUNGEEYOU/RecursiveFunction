def count_down(num):
    """
    num 인자를 기준으로 카운트 다운 출력
    :param num:
    :return:
    """
    print(num)
    if (num <=1):
        return
    else:
        return count_down(num-1)

num = input()
count_down(int(num))