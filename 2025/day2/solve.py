with open("2025\day2\input.txt") as f:
    lines = f.read()
    print(lines)
    products = lines.split(',')
    for product in products:
        print(product)



def part1():
    res = 0
    for product in products:
        firstId, lastId = product.split('-')
        for i in range(int(firstId), int(lastId)+1):
            str_i = str(i)
            length = len(str_i)
            if length % 2 == 0:
                half = length // 2
                if str_i[:half] == str_i[half:]:
                    print(f"Invalid ID found: {str_i}")
                    res += int(str_i)
    print(res)

def part2():
    res = 0
    for product in products:
        firstId, lastId = product.split('-')
        for i in range(int(firstId), int(lastId)+1):
            str_i = str(i)
            length = len(str_i)
            # ID is invalid if it is made only of some sequence of digits repeated at least twice
            # So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.
            for sub_len in range(1, length // 2 + 1):
                if length % sub_len == 0:
                    times = length // sub_len
                    substring = str_i[:sub_len]
                    if substring * times == str_i:
                        print(f"Invalid ID found: {str_i}")
                        res += int(str_i)
                        break
            
    print(res)   

if __name__ == '__main__':
    # part1()
    part2()