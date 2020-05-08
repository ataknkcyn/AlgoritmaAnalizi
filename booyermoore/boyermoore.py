from time import perf_counter
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

NO_OF_CHARS = 256
performance = []
def badCharHeuristic(string, size):  
     
    badChar = [-1]*NO_OF_CHARS   
    
    for i in range(size): 
        badChar[ord(string[i])] = i;   
     
    return badChar 
  
def search(txt, pat): 
    m = len(pat) 
    n = len(txt)  
    badChar = badCharHeuristic(pat, m) 
    
    s = 0
    while(s <= n-m): 
        j = m-1
  
        
        while j>=0 and pat[j] == txt[s+j]: 
            j -= 1
  
        if j<0:            
            return
        else: 
            s += max(1, j-badChar[ord(txt[s+j])]) 
  
  

def main():
    pat = "ATAKAN"
    f=open("oku.txt", "r")
    f2=open("oku2.txt", "r")
    f3=open("oku3.txt", "r")
    txt1 = f.read()
    txt2 = f2.read()
    txt3 = f3.read()
    perf_counter()
    sure1 =perf_counter()  
    search(txt1, pat) 
    sure2 = perf_counter()
    eniyiDurum = sure2-sure1
    
    sure1 =perf_counter()  
    search(txt2, pat) 
    sure2 = perf_counter()
    ortlamaDurum = sure2-sure1
    
    sure1 =perf_counter()  
    search(txt3, pat) 
    sure2 = perf_counter()
    enkotuDurum = sure2-sure1
    
    
    
    objects = ('En iyi Durum\n O(m)', 'En Kötü Durum \n O(n*m)', 'Ortalama Durum\n O(n/m)')
    y_pos = np.arange(len(objects))
    performance = [eniyiDurum,enkotuDurum,ortlamaDurum]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Süre')
    plt.title('Zaman Karmaşıklığı')

    plt.show()
if __name__ == '__main__': 
    main() 
  
