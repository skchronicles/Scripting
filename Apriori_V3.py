
def apriori_v3(q, insig, sex_file_dict, countries_list, age):
    """ This function implements a modified version of the apriori algorithm
        which can be used for speeding up an otherwise exhaustive high-
        performance computing problem. The apriori algorithm is commonly
        used in mining frequent itemsets for boolean association rules. 
        It uses anti-monotonic "bottom up" approach, where frequent subsets
        are extended one item at a time."""

    q = [[int(num)] for num in q]  # queue is formatted as a nested list
    insignificant = [[int(num)] for num in insig]
    significant = []

    #print("\nInsig", insignificant)
    #print("Sig", significant)
    #print("Queue\n", q)

    while len(q) > 0:
        element = q[0]
        obs_freqs = []

        for country in countries_list:
            icd_freq = 0
            for freq in element:
                icd_freq += round(float(sex_file_dict[country][age][str(freq)]) * 1000000)
            obs_freqs.append(icd_freq)

        chisq, pvalue = chisquare(obs_freqs)

        if pvalue >= 0.05:
            significant.append(element)

            for i in range(int(element[-1])+1,36):
                if [i] not in insignificant:
                    tentativeCandidate = sorted(list(element)+[i])  
                    # add the two lists together (element is a list)
                    if tentativeCandidate not in q and tentativeCandidate not in significant:
                        q.append(tentativeCandidate)   # then add it to the queue
            q.pop(0) #remove it from the queue after we have created all the tentativeCandidates

        else:        # when the p-value not significant
            q.pop(0)
            insignificant.append(element)
    return significant  # grab the last values before breaking out of the while loop
