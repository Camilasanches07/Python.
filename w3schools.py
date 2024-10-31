
#LISTA

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3]=["blackcurrant", "watermelon"] 
print(thislist)
#Para mudar itens na lista


lista1= ["arvore", "flores","terra", "areia" ]
lista1.insert (3, "mar")
print(lista1)
#Para adicionar itens na lista em um lugar específico = "insert"


lista2 = ["cachorro", "gato", "macaco", "tartaruga"]
lista2.append ("zebra")
print(lista2)
#Para adicionar itens no final = "append"



lista2 = ["cachorro", "gato", "macaco", "tartaruga"]
lista1.extend(lista2)
print(lista1)
#Para adicionar elementos de outra lista = "extended"


cidades=["Sao Paulo", "Belo Horizonte", "Rio De Janeiro"]
cidades.remove("Sao Paulo")
print(cidades)
#Para remover itens da lista = "remove"


cidades=["Sao Paulo", "Belo Horizonte", "Rio De Janeiro"]
cidades.pop(0)
print(cidades)
#Para remover um item específico da lista = "pop"


cidades=["Sao Paulo", "Belo Horizonte", "Rio De Janeiro"]
cidades.clear()
print(cidades)
#Para limpar a lista = "clear"


thislist = ["apple", "banana", "cherry"]
for item in thislist:
  print(item)
#Para passar 1 por 1 da lista = "for"


lista2 = ["cachorro", "gato", "macaco", "tartaruga"]
newlist=[]
for item in lista2:
  if "o" in item:
    newlist.append(item)

print(newlist)
#Criar uma nova lista com uma nova condição, por exemplo somente palavras com letra "o"


numeros=[10, 50, 70, 49, 30]
numeros.sort()
print(numeros)
#Para sortear numeros, paralvras, etc = "sort"


numeros=[10, 50, 70, 49, 30]
numeros.sort(reverse= True)
print(numeros)
#Para sortear numeros, palavras, etc, em ordem decrescente = "sort(reverse= True)"


numeros=[10, 50, 70, 49, 30]
numeros.reverse()
print(numeros)
#Para colocar os numeros reverso do que escreveu = "sort.reverse()"


lista1= ["arvore", "flores","terra", "areia" ]
mylist=lista1.copy()
print(mylist)
#Para copiar dados de outra lista = "copy"


lista1= ["arvore", "flores","terra", "areia" ]
lista2 = ["cachorro", "gato", "macaco", "tartaruga"]
lista3= lista1 + lista2
print(lista3)
#Juntar 2 listas = "+"


lista1= ["arvore", "flores","terra", "areia" ]
lista2 = ["cachorro", "gato", "macaco", "tartaruga"]
lista1.append(lista2)

print(lista1)
#Outro jeito de juntar 2 listas = "append()"


lista1= ["arvore", "flores","terra", "areia" ]
lista2 = ["cachorro", "gato", "macaco", "tartaruga"]
lista1.extend(lista2)

print(lista1)
#Adicionar lista no final de uma lista = "extended"


#-------------------------------------------------------//---------------------------------------------------------------------------

#DICIONÁRIO

thisdict= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))
#Quantos itens tem dentro do dicionário


thisdict= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x= thisdict ["model"]
print(x)
#Para acessar um dado específico do dicionário


thisdict= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"]= 1965
print(thisdict)
#Para mudar alguma informação


thisdict= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"]= "red"
print(thisdict)
#Para adicionar itens no Dicionário


thisdict= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("brand")
print(thisdict)
#Para apagar itens do dicionário = "pop"


thisdict= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
#Para apagar o último item do dicionário = "popitem"


thisdict= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict ["model"]
print(thisdict)
#Para remover um item de nome específico da lista = "del"
#Também pode excluir um dicionário inteiro = "del thisdict"


thisdict= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
#Para limpar o que tem dentro do dicionário = "clear"]


thisdict= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for item in thisdict:
    print(thisdict)
#Para mostrar item por item no dicionário = "for"



thisdict= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for item in thisdict:
   print(item)
#Para retornar os valores um po um 



thisdict= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for item in thisdict.values():
   print(item)
#Para retornar os valores do dicionário = "values"


thisdict= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict=thisdict.copy()
print(mydict)
#Para copiar um dicionário = "copy"

#---------------------------------------------------------//---------------------------------------------------------------------------

#IF ELIF ELSE

a=50
b=30
if a > b :
    print("a is bigger than b")

a = 20
b = 20
if a > b :
   print("a is bigger than b")
elif a == b :
   print("a is equal to b")

#Se a condição anterior não estiver correta, então tente essa = "elif"


a = 250
b = 100
if a < b :
   print("a é menor que b")
elif a == b:
   print("a é igual a b")
else:
    print("a é maior que b")
#Se não for nenhuma das opções = "else"

#-----------------------------------------//--------------------------------------------------------------------------------------------

#FUNCTION

def my_function():
   print("Hello function")

my_function()

   
def my_functionprint():
   print("-------------------------------")

my_functionprint()
print("Camila é estudante de computação")
my_functionprint()




















