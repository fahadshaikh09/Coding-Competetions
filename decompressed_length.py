import re

######### PROBLEM STATMENT #########
# You are to implement a decompression algorithm given a compression algorithm.
# The compression algorithm takes a sequence of characters (whitespace is ignored). To indicate that some sequence should be repeated, a marker is added to the file, like (5x3). To decompress this marker, take the subsequent 5 characters (which may include characters from another marker as well - see below) and repeat them 3 times. For example:

# - HELLO becomes HELLO as there are no markers in this input.
# - (3x3)ADF becomes ADFADFADF.
# - S(7x2)(2x2)THCF becomes S(2x2)TH(2x2)THCF which then becomes STHTHTHTHCF.
# - (18x9)(3x2)YTQ(5x7)ABABA decompresses into a string with length 369


# Logic :
# 1 ) Check if marker is not present, return lenth else store string in "remaining_str"
# 2 ) if marker present, split on first marker only
# 3 ) extract limit specified in marker
# 4 ) store substring into "remaining" variable
# 5 ) recursively call that string
# 6 ) multiply returned value and add it into "l"
# 7 ) repeat step 2 to step 6 changing value of "remaining" variable
# 8 ) add last string length and return

# Notes to understand:
# if marker is in range of repeating_string then call recursively
# if marker not in range of repeating_string, go iteratively adding lengths


def decompress_len(s):
    remaining_str = s
    l = 0

    while True:
        regx = re.search(r"\((\d+)x(\d+)\)", remaining_str)
        if regx:
            repeat_len, repeat_times = map(int, regx.groups())
            start_str, remaining_tmp = re.split(
                r"\(\d+x\d+\)", remaining_str, maxsplit=1)

            l += len(start_str)  # increment l for start of string

            repeat_str = remaining_tmp[:repeat_len]
            remaining_str = remaining_tmp[repeat_len:]

            l += repeat_times * decompress_len(repeat_str)

        else:
            # if str had some markers which are decompressed now
            l += len(remaining_str)
            return l

if __name__ == '__main__':

    test_cases = [
        "HELLO",
        "(3x3)ADF",
        "S(7x2)(2x2)THCF",
        "(18x9)(3x2)YTQ(5x7)ABABA",
        "(8x9)(3x2)YTQ(5x7)ABABA"
    ]

    for test in test_cases:
        print test, "\t", decompress_len(test)
