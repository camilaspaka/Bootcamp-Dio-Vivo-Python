pessoa = {"nome": "Camila Pinho Spakauskas", "idade": 29}
pessoa = dict(nome="Camila", idade=29)
pessoa["telefone"] = "1111-2222"
print(pessoa)

dados = {"nome": "Camila","idade": 29, "telefone": "6666-6666"}

dados["nome"]
dados["idade"]
dados["telefone"]

dados["nome"] = "Marilia"
dados["idade"] = 32
dados["telefone"] = "1111-2222"
print(dados)

contatos = {
    "camilaspaka@gmail.com": {"nome": "Camila", "telefone": "1111-2222"},
    "mariliaspaka@gmail.com": {"nome": "Marilia", "telefone": "2222-3333"},"extra": {"a": 1},
}
telefone = contatos["camilaspaka@gmail.com"]["telefone"]
print(telefone)
extra = contatos["camilaspaka@gmail.com"]
print(extra)

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

