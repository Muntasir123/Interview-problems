# Check if the letters a-z are in any given sentence (pangram)
import string
def ispangram(str,alphabet = string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str.lower)

