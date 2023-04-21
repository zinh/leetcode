def is_permutation_of(self, a: str, b: str):
        '''
        check of a is a permitation of b
        '''
        a_h, b_h = {}, {}
        for c in a:
            if c not in a_h:
                a_h[c] = 1
            else:
                a_h[c] += 1
        for f in b:
            if c not in b_h:
                b_h[c] = 1
            else:
                b_h[c] += 1

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pass
