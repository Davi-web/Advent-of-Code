# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

with open("input.txt") as f:
    lines = f.readlines()
    num = []
    for line in lines:
        num += line.split()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(num)
    for i in num:
        for j in num:
            for k in num:
                if int(i) != int(j) != int(k) and int(i) + int(j) + int(k) == 2020:
                    print(int(i) * int(j) * int(k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
