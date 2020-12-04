with open("day2-input.txt") as f:
    lines = f.readlines()
    word = []
    for line in lines:

        word += line.split()

if __name__ == '__main__':
    print(word)
    j = 1
    k = 2

    res = 0
    for i in range(0, len(word), 3):
        pos1, pos2 = word[i].split('-')
        char, temp2 = word[j].split(':')
        count = 0
        password = word[k]

        if password[int(pos1) - 1] == char:
            count += 1
        if password[int(pos2) - 1] == char:
            count += 1
        if count == 1:
            res += 1
        j += 3
        k += 3
    print(res)
    # for i in range(0, len(word), 3):
    #     low, high = word[i].split('-')
    #     char, temp2 = word[j].split(':')
    #
    #     password = word[k]
    #     print(low, high, char, password, password.count(char))
    #     if int(low) <= password.count(char) <= int(high):
    #         count += 1
    #     j += 3
    #     k += 3
    # print(count)