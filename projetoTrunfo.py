import random
series_info = [
    {
        "nome": "Breaking Bad",
        "temporadas": 5,
        "episodios": 62,
        "popularidade": 9.5,
        "ano_de_lancamento": 2008
    },
    {
        "nome": "Game of Thrones",
        "temporadas": 8,
        "episodios": 73,
        "popularidade": 9.3,
        "ano_de_lancamento": 2011
    },
    {
        "nome": "Stranger Things",
        "temporadas": 4,
        "episodios": 34,
        "popularidade": 8.7,
        "ano_de_lancamento": 2016
    },
    {
        "nome": "The Mandalorian",
        "temporadas": 3,
        "episodios": 24,
        "popularidade": 8.8,
        "ano_de_lancamento": 2019
    },
    {
        "nome": "The Office",
        "temporadas": 9,
        "episodios": 201,
        "popularidade": 8.9,
        "ano_de_lancamento": 2005
    },
    {
        "nome": "Friends",
        "temporadas": 10,
        "episodios": 236,
        "popularidade": 8.9,
        "ano_de_lancamento": 1994
    },
    {
        "nome": "The Witcher",
        "temporadas": 3,
        "episodios": 24,
        "popularidade": 8.2,
        "ano_de_lancamento": 2019
    },
    {
        "nome": "The Crown",
        "temporadas": 6,
        "episodios": 60,
        "popularidade": 8.6,
        "ano_de_lancamento": 2016
    },
    {
        "nome": "The Boys",
        "temporadas": 3,
        "episodios": 24,
        "popularidade": 8.7,
        "ano_de_lancamento": 2019
    },
    {
        "nome": "The Umbrella Academy",
        "temporadas": 3,
        "episodios": 30,
        "popularidade": 8.0,
        "ano_de_lancamento": 2019
    },
    {
        "nome": "Sherlock",
        "temporadas": 4,
        "episodios": 13,
        "popularidade": 9.1,
        "ano_de_lancamento": 2010
    },
    {
        "nome": "Peaky Blinders",
        "temporadas": 6,
        "episodios": 36,
        "popularidade": 8.8,
        "ano_de_lancamento": 2013
    },
    {
        "nome": "Narcos",
        "temporadas": 3,
        "episodios": 30,
        "popularidade": 8.8,
        "ano_de_lancamento": 2015
    },
    {
        "nome": "Black Mirror",
        "temporadas": 6,
        "episodios": 27,
        "popularidade": 8.8,
        "ano_de_lancamento": 2011
    },
    {
        "nome": "Rick and Morty",
        "temporadas": 6,
        "episodios": 61,
        "popularidade": 9.1,
        "ano_de_lancamento": 2013
    },
]
    
resultado_usuario = ""
resultado_maquina = "" 
usuario_valor = 0
maquina_valor = 0
atributo_escolhido = ""
zero_ou_um = random.randint(0,1)
if zero_ou_um == 0:
    print("Você começa")
else:
    print("Máquina começa")
while True:
    if usuario_valor == 1:        
        print("estou aqui", resultado_usuario)
        break
    if zero_ou_um == 0:
        usuario_carta = random.choice(series_info)
        maquina_carta = random.choice(series_info)

        if usuario_carta == maquina_carta:
            while usuario_carta == maquina_carta:
                usuario_carta = random.choice(series_info)
                                        
        print("Carta do usuário: ", usuario_carta)
        print("Carta da máquina", maquina_carta)
        print()

        print("Escolha um atributo para jogar: ")
        print("[1] - Temporadas")
        print("[2] - Episodios")
        print("[3] - Popularidade")
        print("[4] - Ano de Lançamento")
        entrada = input("Opção: ") 
    
        if entrada == "1":
            print(usuario_carta["temporadas"])
            print(maquina_carta["temporadas"])
            resultado_usuario = usuario_carta["temporadas"]
            resultado_maquina = maquina_carta["temporadas"]
            atributo_escolhido = "temporadas"
        if entrada == "2":
            print(usuario_carta["episodios"])
            print(maquina_carta["episodios"])
            resultado_usuario = usuario_carta["episodios"]
            resultado_maquina = maquina_carta["episodios"]
            atributo_escolhido= "episodios"
        if entrada == "3":
            print(usuario_carta["popularidade"])
            print(maquina_carta["popularidade"])
            resultado_usuario = usuario_carta["popularidade"]
            resultado_maquina = maquina_carta["popularidade"]
            atributo_escolhido = "popularidade"
        if entrada == "4":
            print(usuario_carta["ano_de_lancamento"])
            print(maquina_carta["ano_de_lancamento"])  
            resultado_usuario = usuario_carta["ano_de_lancamento"]
            resultado_maquina = maquina_carta["ano_de_lancamento"] 
            atributo_escolhido = "ano_de_lancamento"

        print("Vencedor do Atributo: ", atributo_escolhido)
        if resultado_usuario > resultado_maquina:
            usuario_valor +=1             
            print("Usuário", usuario_valor)
            zero_ou_um = 0 
        elif resultado_usuario < resultado_maquina:
            maquina_valor +=1
            print("Máquina", maquina_valor)
            zero_ou_um = 1
        else:
            zero_ou_um = 0                 

    else:
        print("Meu atributo escolhido é: ")
        maquina_carta = random.choice(series_info)#Escolher uma carta aleatória da maquina
        usuario_carta = random.choice(series_info)#Escolher a carta aleatoria do usuario
        atributo_escolhido =random.choice(["temporadas" , "episodios" , "popularidade" , "ano_de_lancamento"]) # Criei uma variável para escolher 
        #aleatoriamente entre os atributos possiveis
        resultado_maquina = maquina_carta[atributo_escolhido] #Para escolher um atributo aleatório da maquina
        resultado_usuario = usuario_carta[atributo_escolhido] #Para escolher um atrivuto aleatório do usuario
        print(maquina_carta)
        print(usuario_carta)
        print(resultado_maquina)
        print(resultado_usuario)

        if resultado_maquina > resultado_usuario : #Condição para ver quem venceu
            maquina_valor +=1
            print("Maquina", maquina_valor) 
            zero_ou_um = 1
        elif resultado_maquina < resultado_usuario:
            usuario_valor +=1  
            print("Usuário", usuario_valor)
            zero_ou_um = 0 
        else: 
            zero_ou_um = 1    