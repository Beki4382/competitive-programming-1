import textwrap

def wrap(string, max_width):
    res= []
    for i in range(0, len(string), max_width):
        res.append(string[i:i+max_width] + '\n')
    return ''.join(res)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)