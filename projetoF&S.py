filmes_e_series= [
    { 
        "nome": "The Walking Dead",
        "genero": "Drama e Pós Apocaliptica",
        "pontuacao": 8.1, 
        "tipo": "Série",
        "temporadas": 11,
        "episodios": 117,
        "cartaz": True,
    },
    {
        "nome": "breaking bad",
        "genero": "Drama e Crime",
        "pontuacao": 9.5 ,
        "tipo":"Série",
        "temporadas": 5,
        "episodios": 62,
        "cartaz": False, 
    },
    {
        "nome": "A Culpa É Das Estrelas",
        "genero": "Romance e Drama",
        "pontuacao": 7.7,
        "tipo": "filme",
        "duracao": "2 horas e 8 minutos",
        "cartaz": True,
    },
    {
        "nome": "Velozes e Furiosos",
        "genero": "Ação e Crime",
        "pontuacao": 7.0,
        "tipo": "filme",
        "duracao": "1 hora e 47 minutos",
        "cartaz": True,
    },
    {
        "nome": "O Poderoso Chefão",
        "genero": "Drama e Crime",
        "pontuacao": 9.2,
        "tipo": "filme",
        "duracao": "2 horas e 55 minutos",
        "cartaz": False,
    },
    {
        "nome": "Se Beber, Não Case!",
        "genero": "Comédia",
        "pontuacao": 7.7,
        "tipo": "filme",
        "duracao": "1 hora e 40 minutos",
        "cartaz": False,
    },
    {
        "nome": "Belo Desastre",
        "genero": "Romance e Drama",
        "pontuacao": 5.3,
        "tipo": "filme",
        "duracao": "1 hora e 45 minutos",
        "cartaz": True,
    },
    {
        "nome": "Procurando Nemo",
        "genero": "Animação e Aventura",
        "pontuacao": 8.1,
        "tipo": "filme",
        "duracao": "1 hora e 40 minutos",
        "cartaz": False,
    },
    {
        "nome": "Vikings",
        "genero": "História e Ação",
        "pontuacao": 8.5,  
        "tipo": "Série",
        "temporadas": 6,
        "episodios": 89,
        "cartaz": False,
    },
    {
        "nome": "Vis a Vis",
        "genero": "Drama e Suspense",
        "pontuacao": 8.2,  
        "tipo": "Série",
        "temporadas": 4,
        "episodios": 40,
        "cartaz": False,
    },
    {
        "nome": "Arrow",
        "genero": "Ação e Super-herói",
        "pontuacao": 7.5,  
        "tipo": "Série",
        "temporadas": 8,
        "episodios": 170,
        "cartaz": False,
    },
    {
        "nome": "La Casa de Papel",
        "genero": "Crime e Suspense",
        "pontuacao": 8.2,  
        "tipo": "Série",
        "temporadas": 5,
        "episodios": 41,
        "cartaz": False,
    },
    {
        "nome": "Peaky Blinders",
        "genero": "Drama e Crime",
        "pontuacao": 8.8,  
        "tipo": "Série",
        "temporadas": 6,
        "episodios": 36,
        "cartaz": False,
    },
]  
start= True
n=0 
filme= None

while start == True:
    print("Escolha uma das opções abaixo: ")
    print("[1] - Filmes")
    print("[2] - Séries")
    print("[0] - Encerrar")
    entrada= input("Opção: ")

    if entrada == "0":
        start = False

    if entrada == "1":
        print("Digite uma das opções abaixo: ")
        print("[1] - Filme em cartaz" )
        print("[2] - Filme com a melhor avaliação")
        print("[3] - Filme por gênero") 
        print("[4] - Buscar um filme")   
        entrada= input("Opção: ")
        if entrada == "1":
            for item in filmes_e_series:
                if item["cartaz"] == True and item["tipo"] == "filme": 
                    print(item["nome"])
                
        if entrada == "2":
            for item in filmes_e_series:       
                if item["pontuacao"] > n and item["tipo"] == "filme":
                    n = item["pontuacao"]
                    filme = item["nome"]
            print(filme)           

        if entrada == "3":
            print("[1] - Romance e Drama")
            print("[2] - Acão e Crime")
            print("[3] - Drama e Crime")
            print("[4] - Comédia")
            print("[5] - Animação e Aventura" )
            enter=input("Escolha uma opção de gênero: ")

            if enter == "1":
                for item in filmes_e_series:
                    if item["genero"] == "Romance e Drama" and item["tipo"] == "filme":
                        print(item) 
            if enter == "2":            
                for item in filmes_e_series:             
                    if item["genero"] == "Ação e Crime" and item["tipo"] == "filme":
                         print(item)
            if enter == "3":             
                for item in filmes_e_series:         
                    if item["genero"] == "Drama e Crime" and item["tipo"] == "filme":
                        print(item)
            if enter == "4":   
                for item in filmes_e_series:             
                    if item["genero"] == "Comédia" and item["tipo"] == "filme":
                        print(item)
            if enter == "5":
                for item in filmes_e_series:    
                    if item["genero"] == "Animação e Aventura" and item["tipo"] == "filme":
                        print(item)
   
        if entrada == "4":
            entrada =input("Digite um filme: ")            
            for item in filmes_e_series:
                if item["nome"] == entrada:
                    print(item)

    if entrada == "2":
        print("Digite uma das opções abaixo: ")
        print("[1] - Series em cartaz")
        print("[2] - Séries com a melhor avaliação")
        print("[3] - Séries por gênero")
        print("[4] - Buscar séries")
        entrada = input("Opção: ")
        if entrada == "1":
            for item in filmes_e_series:
                if item["cartaz"] == True and item["tipo"] =="Série": 
                    print(item["nome"])

        if entrada == "2":
            for item in filmes_e_series:
                if item["pontuacao"] > n and item ["tipo"] == "Série":
                        n=item["pontuacao"]
                        filme=item
            print(filme["nome"])

        if entrada == "3":
            print("[1] - Drama e Pós Apocaliptica")
            print("[2] - Drama e Crime")
            print("[3] - História e Ação")
            print("[4] - Drama e Suspense")
            print("[5] - Ação e Súper-Herói")
            print("[6] - Crime e Suspense")
            entrada == input("Escolha uma opção de gênero: ")

            if entrada =="1":
                for item in filmes_e_series:
                    if item["genero"] == "Drama e Pós Apocaliptica" and item["tipo"] == "Série":
                        print(item)
            if entrada == "2":
                for item in filmes_e_series:
                    if item["genero"] == "Drama e Crime" and item["tipo"] == "Série":
                        print(item)
            if entrada == "3":
                for item in filmes_e_series:
                    if item["genero"] == "História e Ação"and item["tipo"] == "Série":
                        print(item)
            if entrada == "4":
                for item in filmes_e_series:
                    if item["genero"] == "Drama e Suspense"and item["tipo"] == "Série":
                        print(item)
            if entrada =="5":
                for item in filmes_e_series:
                    if item["genero"] == "Ação e Súper-Herói"and item["tipo"] == "Série":
                        print(item)
            if entrada == "6":
                for item in filmes_e_series:
                    print(item)

        if entrada == "4":
            entrada =input("Digite uma série: ")            
            for item in filmes_e_series:
                if item["nome"] == entrada:
                    print(item)