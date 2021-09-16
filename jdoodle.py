cod = 0
quant = 0
preco = 0     
preco_t = 0
desconto = 0
preco_f = 0
cod = int(input("Digite código do produto: "))
quant = int(input("Digite a quantidade de produtos:"))
if(cod == 1):
	preco = 9.00
	print("O preço unitário do produto 1 é de: R$",preco,"\n")                                 
elif(cod ==2):
	preco = 12.00
	print("O preço unitário do produto 2 é de: R$",preco,"\n")                              
elif(cod == 3):
	preco = 20.00
	print("O preço unitário do produto 3 é de: R$",preco,"\n")                           
elif(cod == 4):
	preco = 28.00
	print("O preço unitário do produto 4 é de: R$",preco,"\n")            
else:
	print("Código Inválido")    
preco_t = quant*preco
print("O preço bruto é de: ",preco_t,"\n")      
if(preco_t <= 150.00):
	desconto = 0.06*preco_t
	print("Desconto de 6%","\n")    
elif(preco_t > 150.00 and preco_t <= 500.00):              
	desconto = 0.12*preco_t
	print("Desconto de 12%","\n")
else:
	desconto = 0.15*preco_t
	print("Desconto de 15%","\n")
preco_f = preco_t - desconto
print("O preço final é de: R$",preco_f)
