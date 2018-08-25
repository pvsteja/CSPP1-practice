'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
	# freqs: dictionary (element_type -> int)
    freq = {}
    for i in sequence:
        freq[i] = freq.get(i, 0) + 1
    return freq

def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()


