"""
Geek likes this girl Garima from his neighborhood, and wants to impress her so that she may go on a date with him. Garima is a Perfectionist and likes only PERFECT things .This makes Geek really nervous, and so Geek asks for your Help.!

Geek has baked a cake for Gerima, which is basically an array of Numbers. Garima will take only a Perfect Piece of the cake.

A Perfect Piece is defined as - a suharray such that the difference between the minimum and the maximum value in that range is at most 1. Now, Since garima just loves cake, She wants a Perfect Piece Of Maximum length possible. Help Geek go on a date.! 


Test Case : 

cake = 5 4 5 5 6 7 8 8 8 7 6
answer = 7 8 8 8 7

"""


def perfect_piece_of_cake(a):
    results = []
    t = None
    l = 0

    for i in range(len(a) - 1):
        if abs(a[i] - a[i + 1]) <= 1:
            if t:
                if a[i] in t and a[i + 1] in t:
                    l += 1
                    continue

            if l > 0:
                results.append((i - l + 1, l))

            # when "t" is not defined OR i & i+1 elements not in "t"
            t = set(a[i:i + 2])
            l = 2

            continue

        if l > 0:
            results.append((i - l + 1, l))
        t = None
        l = 0

    if l > 0:
        # to handle last piece of cake
        results.append((i - l + 2, l))

    if results:
        index, length = max(results, key=lambda x: x[1])
        return a[index:index + length]

    # when no perfect cake found
    return None

if __name__ == '__main__':
    test_cases = [
        "8 8 8 8",
        "1 2 3 3 2",
        "5 4 5 5 6 7 8 8 8 7 6"
    ]

    for test in test_cases:
        a = map(int, test.split(" "))
        print perfect_piece_of_cake(a)
