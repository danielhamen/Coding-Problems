def count_substring(string, sub_string):
    count = 0
    for char in range(len(string)):
        if string[char:char + len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)