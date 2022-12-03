import fileinput
def n_gram(n):
    freq_count = {}
    alphabet = set([chr(i) for i in range(97,123)])
    total_count = 0
    for line in fileinput.input():
        i = 0
        while i < len(line):
            n_token = ""
            for j in range(i,i+n):
                if j < len(line) and line[j] in alphabet: 
                    n_token += line[j]
                else:
                    break
                if len(n_token) == n:
                    freq_count[n_token] = freq_count.get(n_token, 0) + 1
                    total_count += 1
            i += 1
    #order = ""
    for k,v in sorted(freq_count.items(), key=lambda item:item[1], reverse=True):
        print(k+":{:.2f}".format(v/float(total_count)*100))
    print(freq_count)
    #    order += k
    # print(alphabet)

def main(n):
    n_gram(n)

if __name__ == '__main__':
    main(1)