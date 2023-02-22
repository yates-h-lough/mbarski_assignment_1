import pattern_search
import random
import input_generator

def stress_test(max_N, alphabet):
    N = random.randint(10, max_N)
    rand_string = input_generator.get_rand_string (N, alphabet)

    rand_pattern_start = random.randint(0, N-1)
    rand_pattern_len = random.randint(2, 15)

    rand_pattern = rand_string[rand_pattern_start:rand_pattern_start+rand_pattern_len+1]

    matches1 = pattern_search.naive_search(rand_string, rand_pattern)
    matches2 = pattern_search.kmp_search(rand_string, rand_pattern)
    if matches1 != matches2:
        print(rand_string)
        print(rand_pattern)
        print (matches1, matches2)
        return False

    return True

if __name__ == "__main__":
    passed = True
    while passed:
        passed = stress_test(100, ['a', 'b'])
