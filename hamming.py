'''This code is going to demonstrate the working of
hamming similarity between 2 sentences. More information
about hamming similarity can be obtained from the package 
jellyfish'''

import jellyfish

def get_hamming_sim(str1, str2):
    a = set(str1.split())
    b = set(str2.split())
    c = jellyfish.hamming_distance(str(a),str(b))
    return float(c)


if __name__ == "__main__":
    sentence_1 = "This sentence is vague"
    sentence_2 = "This sentence is not clear"
    print(get_hamming_sim(sentence_1, sentence_2))