import sys

# general computation of an overlap function
def overlap_function(P):
    M =  len(P)
    of_table = [0] * M

    for pos in range (1, M): # first is always zero, we start from 1
        prev_overlap = of_table[pos - 1]

        if P[pos] == P[prev_overlap]:
            of_table[pos] = prev_overlap + 1
        else:
            while P[pos]!=P[prev_overlap] and prev_overlap >= 1:
                # try extend a smaller prefix - based on P [of_table[pos-1]]
                prev_overlap = of_table[prev_overlap - 1]

            if P[pos] == P[prev_overlap]:
                of_table[pos] = prev_overlap + 1
    return of_table


def naive_search (T, P):
    matches = []
    M = len(P)
    N = len(T)

    #naive algorithm
    for i in range (N - M + 1):
        j = 0
        while j < M and P[j] == T[i+j]:
            j += 1
            
        if j == M:
            matches.append(i)
        
    return matches


def kmp_search(T, P):
  of_list = overlap_function(P)
  M = len(P)
  N = len(T)
  matches = []
  shift = 0
  i = 0
  while i < N:
    if T[i] == P[i-shift]:
    # If characters match, then increment i.
      i += 1
      if i-shift == M:
        # We've found a match.
        matches.append(shift)
        shift = i - of_list[M-1]
        # Hence we add 'shift' to our matches,
        # and then we increment it.
    else:
      if i-shift == 0:
        #increment shift by one and i by one
        i += 1
        shift += 1
      else:
        shift = i-of_list[i-shift-1]
        
        
    # If characters don't match, then increment shift (by a variable amount)
  return matches


if __name__ == "__main__":
    # default demo values
    T = 'tictictictacicac'
    P = 'tictic'

    if len(sys.argv) > 2:
        T = sys.argv[1]
        P = sys.argv[2]

    of_list = overlap_function(P)
    print (of_list)

    matches = kmp_search(T, P)
    print("Search for pattern '" + P + "': results")
    print("KMP matches at position(s):", matches) # should be [0,3]

    matches = naive_search(T, P)
    print("Naive matches at position(s):", matches) # should be [0,3]