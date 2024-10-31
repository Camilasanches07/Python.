produtos_eletrodomesticos = [
    {"id": 1, "nome": "Geladeira", "quantidade_em_estoque": 10, "preço": 2500.00},
    {"id": 2, "nome": "Micro-ondas", "quantidade_em_estoque": 15, "preço": 800.00},
    {"id": 3, "nome": "Máquina de Lavar", "quantidade_em_estoque": 5, "preço": 1800.00},
    {"id": 4, "nome": "Fogão", "quantidade_em_estoque": 12, "preco": 1200.00},
    {"id": 5, "nome": "Aspirador de Pó", "quantidade_em_estoque": 20, "preço": 500.00},
    {"id": 6, "nome": "Ar-condicionado", "quantidade_em_estoque": 8, "preço": 3500.00},
    {"id": 7, "nome": "Geladeira", "quantidade_em_estoque": 20, "preço": 2590.00}
]

def create_new_product(nome, quantidade_em_estoque, preco):
    new_product = {"id": "", "nome": "", "quantidade_em_estoque": "", "preço": ""}
    new_id = produtos_eletrodomesticos[-1]["id"] + 1 

    new_product["id"] = new_id
    new_product["nome"] = nome
    new_product["quantidade_em_estoque"] = quantidade_em_estoque
    new_product["preço"] = preco

    produtos_eletrodomesticos.append(new_product)
    return "Produto criado com sucesso"

print(produtos_eletrodomesticos)

def get_product_by_id(id):
    for item in produtos_eletrodomesticos:
        if item["id"] == id:
            return item   
print(get_product_by_id(7))                    

def get_product_by_name(name):
    for item in produtos_eletrodomesticos:
        if item["nome"] == name:
            return name 