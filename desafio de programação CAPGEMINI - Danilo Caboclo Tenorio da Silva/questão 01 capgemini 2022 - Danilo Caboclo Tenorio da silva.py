
num_list = int(input("digite o tamanho da lista: ")) #entrada da quantidade de degraus
new_list = []#criação de uma lista vazia para montagem da escada
#================================================================================================
for i in range(0,num_list):
    new_list.append(" ")
    if(len(new_list) == num_list):
        for i in range(0,len(new_list)):#laço para preenchimento dos degraus usando "*"
            new_list.pop(0)
            new_list.append("*")
            print(''.join(new_list))#demonstração do resultado
           























   
