#entrada de dados ==========================================================
ent_senha = input("digite a senha a ser avaliada: ")
list_carac = list(("!@#$%^&*()-+"))
cont_saida = 0
list_senha = list(ent_senha)
cont_req = 0
#===========================================================================

#estruturas para controle dos requisitos ja existentes na senha=============
if(any(ele.isupper() for ele in ent_senha)):#verificação caracter maiusculo
    cont_req+=1
if(any(ele.islower() for ele in ent_senha)):#verificação caracter minusculo
    cont_req+=1    
if(any(ele.isdigit() for ele in ent_senha)):#verificação de digito
    cont_req+=1
if set(list_carac).intersection(list_senha):#verificação caracter especial
    cont_req+=1
#===========================================================================

#estruturas de decisão e contagem ==========================================

#caso possua menos que 6 caracteres e atenda os 4 requisitos ===============
if(len(list_senha)<6):
    if(cont_req ==4 ):
        print(6-(len(list_senha)))
#===========================================================================
        
#caso possua menos que 6 caracteres e menos que 4 requisitos ===============        
    elif(cont_req < 4):
        
        caracter_falta =  4 - cont_req 
        teste_cont = caracter_falta + len(list_senha)
        sub_senha = 6 - teste_cont
        soma_final = sub_senha + caracter_falta
        print(soma_final)
        
        
        
#caso possua mais de 6 caracteres e menos que 4 requisitos==================   
elif(len(list_senha)>=6):
    if(cont_req < 4):
        caracter_falta = 4- cont_req 
        print(caracter_falta)
    
#fim do codigo =============================================================
















