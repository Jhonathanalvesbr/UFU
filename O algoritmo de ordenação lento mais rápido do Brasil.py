import random                                           #

def desornenar(arr):                                    #Desordenar String
    for x in range(0, len(arr)):                        #n
        for y in range(0, len(arr)+1):                  #n+1
            for z in range(0, len(arr)):                #n
                r = int(random.uniform(x,y));           #
                if(r <= len(arr)):                      #n*(n+1)*n
                    aux = arr[z]                        #
                    arr[z] = arr[r]                     #
                    arr[r] = aux                        #
    return arr                                          #(n^2)*(n+1)

def insertionSort(arr):                                 #Ordenar String - Insertion Sort
    arr = desornenar(arr)                               #(n^2)*(n+1)
    for i in range(1, len(arr)):                        #   
        key = arr[i]                                    #
        j = i-1                                         #
        while j >=0 and key < arr[j]:                   #(n-1)
            arr[j+1] = arr[j]                           #
            j -= 1                                      #
        arr[j+1] = key                                  #
    return arr                                          #(n^2)*(n+1) + (n-1)

arr = []                                                #
while(True):                                            #
    try:                                                #
        dados = input()                                 #
        arr.append(int(dados))                          #
    except EOFError:                                    #
        arr = insertionSort(arr)                        #(n^2)*(n+1) + (n-1)
        for k in arr:                                   #
            print(k)                                    #
        break                                           #
    except:                                             #
        arr.append(dados)                               #
    
