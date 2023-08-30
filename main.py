def pal(word):
    count = 0
    for i in word:
        count += 1
    if count % 2 == 1:
        mid = count // 2 + 1
        count_2 = 0
        for i in word:
            count_2 += 1
            if count_2 == mid:
                b = i
        lst = []
        count_3 = 0
        for i in word:
            count_3 += 1
            if count_3 < mid:
                lst.append(i)
        count_3 = 0
        lst_2 = []
        for i in word:
            count_3 += 1
            if count_3 > mid:
                lst_2.append(i)
        lst_2.reverse()
        if lst == lst_2:
            print('True')
        else:
            print('False')
    else:
        mid = count // 2 + 1
        count_2 = 0
        for i in word:
            count_2 += 1
            if count_2 == mid:
                b = i
        lst = []
        count_3 = 0
        for i in word:
            count_3 += 1
            if count_3 < mid:
                lst.append(i)
        count_3 = 0
        lst_2 = []
        for i in word:
            count_3 += 1
            if count_3 > mid:
                lst_2.append(i)
        if lst[2] == b:
            lst.pop(2)
        lst_2.reverse()
        if lst == lst_2:
            print('True')
        else:
            print('False')

input_word = input("Слово: ")
pal(input_word)