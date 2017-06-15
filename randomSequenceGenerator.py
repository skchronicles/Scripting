#########################################################################################
# Skyler Kuhn
# BNFO 601: Integrative Bioinformatics
# This program will generate a random string of nucleotide of given A, T, C, G contents
#########################################################################################

import random

"""
def sequence_generator(aPercent,tPercent, cPercent, gPercent, length):
    a_amount = int(round(aPercent * length))
    t_amount = int(round(tPercent * length))
    c_amount = int(round(cPercent * length))
    g_amount = int(round(gPercent * length))
    if (a_amount + t_amount + c_amount + g_amount) < length:
        highest_occurence = max(a_amount, t_amount,  c_amount, g_amount)
        if a_amount == highest_occurence:
            a_amount += 1
        elif t_amount == highest_occurence:
            t_amount += 1
        elif c_amount == highest_occurence:
            c_amount += 1
        else:
            g_amount += 1
    if (a_amount + t_amount + c_amount + g_amount) > length:
        highest_occurence = max(a_amount, t_amount, c_amount, g_amount)
        if a_amount == highest_occurence:
            a_amount -= 1
        elif t_amount == highest_occurence:
            t_amount -= 1
        elif c_amount == highest_occurence:
            c_amount -= 1
        else:
            g_amount -= 1
    if (aPercent + tPercent + cPercent + gPercent) == 1.0 and (a_amount + t_amount + c_amount + g_amount) == length:
        sequence = (str('A')*a_amount) + (str('T')*t_amount) + (str('C')*c_amount) + (str('G')*g_amount)
        seq_list = []
        for base in sequence:
            seq_list.append(base)
        random.shuffle(seq_list)
        rand_seq = ""
        for base in seq_list:
            rand_seq += base
        return rand_seq
    else:
        print("A, T, C, G content does not add up to 100%. Please check nucleotide contents again!")

a = sequence_generator(0.25, 0.25, 0.25, 0.25, 100)
print(a)
print("Sequnce Length: " + str(len(a)))
"""

class Random_Sequence_Generator(object):
    """This class will generate a random string of nucleotides of a given length with pre-defined A,T,C,G contents."""
    def __init__(self, aContent, tContent, cContent, gContent, length):
        self.sequence = ""
        self.a = int(round(aContent*length))
        self.t = int(round(tContent*length))
        self.c = int(round(cContent*length))
        self.g = int(round(gContent*length))
        self.length = length

    def sequence_generator(self):
        if (self.a + self.t + self.c + self.g) < self.length:
            highest_occurence = max(self.a, self.t, self.c, self.g)
            if self.a is highest_occurence:
                self.a += 1
            elif self.t is highest_occurence:
                self.t += 1
            elif self.c is highest_occurence:
                self.c += 1
            else:
                self.g += 1
        if (self.a + self.t + self.c + self.g) > self.length:
            highest_occurence = max(self.a, self.t, self.c, self.g)
            if self.a is highest_occurence:
                self.a -= 1
            elif self.t is highest_occurence:
                self.t -= 1
            elif self.c is highest_occurence:
                self.c -= 1
            else:
                self.g -= 1
        if (self.a + self.t + self.c + self.g) == self.length:
            sequence = (str('A') * self.a) + (str('T') * self.t) + (str('C') * self.c) + (str('G') * self.g)
            seq_list = []
            for base in sequence:
                seq_list.append(base)
            random.shuffle(seq_list)
            rand_seq = ""
            for base in seq_list:
                rand_seq += base
            return rand_seq
        else:
            print("A, T, C, G content does not add up to 100%. Please check nucleotide contents again!")


if __name__ == '__main__':
    seq = Random_Sequence_Generator(0.25, 0.25, 0.25, 0.25, 10000)
    r1 = seq.sequence_generator()
    print(r1)



