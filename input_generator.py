import math
import random

'''
Generates a random string with N total characters
where symbols are randomly drawn from a supplied
alphabet, which must be an array of strings
'''
def get_rand_string(N, alphabet):
    t = []
    for i in range(N):
        c = random.choice(alphabet)
        t.append(c)

    result = "".join(t)
    return result[:N]


'''
Generates a Fibonacci string with N total characters
where the first 2 elements are x and y
and each next element of the sequence is a concatenation of two previous substrings
'''
def get_fib_string(N, x, y):
    if N == 1:
        return x[:1]
    if N == 2:
        return x[:1]+ y[:1]

    t = [""]*2*math.ceil(math.log2(N))
    t[0] = x
    t[1] = y
    for i in range(2, 2*math.ceil(math.log2(N))):
        t[i] = t[i - 2] + t[i - 1]

    result = "".join(t)
    # print(len(result))
    return result[:N]


if __name__ == "__main__":
    s = get_rand_string(20, ['a', 'b'])
    print("Random string of len ",len(s))
    print(s)

    s = get_fib_string(20, 'ab', 'cd')
    print("Fibonacci string of len ",len(s))
    print(s)