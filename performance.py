import timeit
import random
import input_generator
import pattern_search


def function_wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def performance_test(T, num_tests, min_M, max_M, step):
    print ("Input  \t Naive \t KMP \t Ratio")

    N = len(T)
    # The test is over the same N, we only vary the pattern length M

    for M in range (min_M, max_M+step, step):
        # take a random substring from T num_tests times
        naive_time = 0
        kmp_time = 0
        for i in range(num_tests):
            
            rand_pattern_start = random.randint(0, N - M)
            P = T[rand_pattern_start:rand_pattern_start + M]

            # Get time from 1 repetition of the algorithms
            func_naive = function_wrapper(pattern_search.naive_search, T, P)
            naive_time += timeit.timeit(func_naive, number=1) # This takes a really long time.
            func_fast = function_wrapper(pattern_search.kmp_search, T, P)
            kmp_time += timeit.timeit(func_fast, number=1)
        # produce average running time
        naive_time = naive_time/num_tests
        kmp_time = kmp_time/num_tests

        # Print input size, times, the speedup of kmp over naive
        print("{0:d} \t {1:7.6f} \t {2:7.6f} \t{3:10.3f}".format(M, naive_time, kmp_time, naive_time/kmp_time))


if __name__ == "__main__":
    N = 1000000

    alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet = ['a','b']
    T = open('SRR001520.txt','r').read()
    num_tests = 20
    min_M = 5
    max_M = 125
    step = 20

    print("Performance test for string over alphabet of size", len(alphabet))
    performance_test(T, num_tests, min_M, max_M, step)