########################################################
# Skyler Kuhn
# Markov Chain Prose Generator
# Bringing Back Dead Poets with Science
########################################################
import random


def transition(filename):
    fH = open(filename)
    transitions = {}
    for line in fH:
        lineList = line.split(" ")
        for index in range(len(lineList)-2):
                w1, w2, w3 = lineList[index:index+3]
                try:
                    transitions[w1][w2].append(w3)
                except KeyError:
                    if w1 not in transitions:
                        transitions[w1] = {}
                    if w2 not in transitions[w1]:
                            transitions[w1][w2] = [w3]
    return transitions


def createPoem(wordCount, chainDict):
    def setseed():
        seedtuple = random.choice(list(chainDict.items()))
        seed = seedtuple[0]
        w1 = random.choice(list(seedtuple[1].keys()))
        w2 = random.choice(chainDict[seed][w1])
        return seed, w1, w2

    seed, w1, w2 = setseed()
    prose = ""
    for i in range(wordCount):
        if "\n" in w2:
            prose += w2
        else:
            prose += w2 + " "
        try:
            seed, w1, w2 = w1, w2, random.choice(chainDict[w1][w2])
        except KeyError:
            seed, w1, w2 = setseed()
    print(prose)


if __name__ == "__main__":
    markov_chain = transition("edgarAllanPoe.txt")
    createPoem(70, markov_chain)

