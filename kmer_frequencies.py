
sequence = "AAACCCTTTGGGGGG"
kmerlength = 5
kmer_dict = {}

for pos in range(0,len(sequence),1):
    kmer = sequence[pos:pos+kmerlength]
    if len(kmer) == kmerlength:
        print(kmer)
        if kmer not in kmer_dict:
            kmer_dict[kmer] = 1
        else:
            kmer_dict[kmer] += 1

print(kmer_dict)

kmername= str
low = -666
for kmer, freq in kmer_dict.items():
    if freq > low:
        low = freq
        kmername = kmer

print("\nThe most frequent k-mer in the Sequence is '{}'".format(kmername))
print("'{}' occurs {} times in the sequence".format(kmername,low))

