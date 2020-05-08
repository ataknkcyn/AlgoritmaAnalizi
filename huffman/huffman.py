from time import perf_counter
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
DEBUG = False




class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


def huffmanCodeTree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffmanCodeTree(l, True, binString + '0'))
    d.update(huffmanCodeTree(r, False, binString + '1'))
    return d

def main2(string):

    freq = {}
    for c in string:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)



    nodes = freq

    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))

        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    huffmanCode = huffmanCodeTree(nodes[0][0]) 
    print(' Char | Huffman code ')
    print('----------------------')
    for (char, frequency) in freq:
        print(' %-4r |%12s' % (char, huffmanCode[char]))


def main():
    f=open("oku01.txt", "r")
    f2=open("oku02.txt", "r")
    f3=open("oku03.txt", "r")
    txt1 = f.read()
    txt2 = f2.read()
    txt3 = f3.read()
    perf_counter()
    perf_counter()
    string= txt3
    sure1 =perf_counter()    
    main2(string)
    sure2 = perf_counter()
    ortlamaDurum = sure2-sure1
    
    string= txt1
    sure1 =perf_counter()    
    main2(string)
    sure2 = perf_counter()
    eniyiDurum = sure2-sure1
    
    
    
    string= txt2
    sure1 =perf_counter()
    
    main2(string)
    sure2 = perf_counter()
    enkotuDurum = sure2-sure1

    
    
        
    objects = ('n = '+str(len(txt1)), 'n = '+str(len(txt2)), 'n = '+str(len(txt3)))
    y_pos = np.arange(len(objects))
    performance = [eniyiDurum,enkotuDurum,ortlamaDurum]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Süre')
    plt.title('Zaman Karmaşıklığı (nlogn)')

    plt.show()
if __name__ == '__main__': 
    main()

