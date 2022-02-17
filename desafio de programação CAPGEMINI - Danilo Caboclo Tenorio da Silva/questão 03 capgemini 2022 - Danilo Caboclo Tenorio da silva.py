#entrada de dados =======================================
anag_entr = input("digite a palavra: ")
anag_list = list(anag_entr) #mudança da string para lista, para facilitar manipulação
tam_list = len(anag_list)
#contador================================================
cont_anag = 0
#laços para controle ====================================
for h in range(0,tam_list-1):
    for i in range(0,tam_list-1-h):          
        for j in range(i+1, tam_list-h):            
            if(sorted(anag_list[i:i+h+1])== sorted(anag_list[j:j+h+1])):                   
                cont_anag+=1
print(cont_anag)
    
