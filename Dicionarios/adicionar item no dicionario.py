lucro_tri1 = {'janeiro':10000,'fevereiro':12000,'março':90000}
lucro_tri2 = {'abril':88000,'maio':59000,'junho':120000}

#lucro_tri1['abril'] = 88000
#print(lucro_tri1)

lucro_tri1.update(lucro_tri2)
print(lucro_tri1)

lucro_tri1['janeiro'] = 88000
print(lucro_tri1['janeiro'])
#se quiser remover um item do dicinoario basta utilizar o comando del
del lucro_tri1['junho']
print(lucro_tri1)
#se quiser tirar um item da lista e utiliza-lo depois, utilize o metodo pop
lucro_maio = lucro_tri1.pop('maio')
print(lucro_maio)
print(lucro_tri1)