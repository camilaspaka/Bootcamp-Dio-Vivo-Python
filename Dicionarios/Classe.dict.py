#{}.clear
contatos = {
    "camilaspaka@gmail.com": {"nome": "Camila", "telefone": "1111-2222"},
    "mariliaspaka@gmail.com": {"nome": "Marilia", "telefone": "2222-3333"},"extra": {"a": 1},
}

contatos.clear()
print(contatos)

#{}.copy
contatos = {
    "camilaspaka@gmail.com": {"nome": "Camila", "telefone": "1111-2222"},
    "mariliaspaka@gmail.com": {"nome": "Marilia", "telefone": "2222-3333"},"extra": {"a": 1},
}
copia = contatos.copy
#copia["camilaspaka@gmail.com"] = {"nome": "Cah"}

#{}.fromkeys
dict.fromkeys(["nome", "telefone"])
dict.fromkeys(["nome", "telefone"], "vazio")

#{}.get
contatos = {
    "camilaspaka@gmail.com": {"nome": "Camila", "telefone": "1111-2222"},
    "mariliaspaka@gmail.com": {"nome": "Marilia", "telefone": "2222-3333"},"extra": {"a": 1},
}
contatos["chave"]
contatos.get("chave")
contatos.get("chave", {})
contatos.get("guilherme@gmail.com", {})

#{}.items
contatos = {
    "camilaspaka@gmail.com": {"nome": "Camila", "telefone": "1111-2222"},
    "mariliaspaka@gmail.com": {"nome": "Marilia", "telefone": "2222-3333"},"extra": {"a": 1},
}
contatos.items

#{}.key
contatos = {
    "camilaspaka@gmail.com": {"nome": "Camila", "telefone": "1111-2222"},
    "mariliaspaka@gmail.com": {"nome": "Marilia", "telefone": "2222-3333"},"extra": {"a": 1},
}

contatos.keys()

#{}.pop
contatos = {
    "camilaspaka@gmail.com": {"nome": "Camila", "telefone": "1111-2222"},
    "mariliaspaka@gmail.com": {"nome": "Marilia", "telefone": "2222-3333"},"extra": {"a": 1},
}

contatos.pop("camilaspaka@gmail.com")
contatos.pop("camilaspaka@gmail.com", {})

#{}.popitem
contatos = {
    "camilaspaka@gmail.com": {"nome": "Camila", "telefone": "1111-2222"},
    "mariliaspaka@gmail.com": {"nome": "Marilia", "telefone": "2222-3333"},"extra": {"a": 1},
}
contatos.popitem()
contatos.popitem()

#{}.setdefault
contatos = {
    "camilaspaka@gmail.com": {"nome": "Camila", "telefone": "1111-2222"},
    "mariliaspaka@gmail.com": {"nome": "Marilia", "telefone": "2222-3333"},"extra": {"a": 1},
}
contatos.setdefault("nome", "Marilia")
print(contatos)
contatos.setdefault("idade", 29)
print(contatos)

#{}.update
contatos = {
    "camilaspaka@gmail.com": {"nome": "Camila", "telefone": "1111-2222"},
    "mariliaspaka@gmail.com": {"nome": "Marilia", "telefone": "2222-3333"},"extra": {"a": 1},
}
contatos.update({"camilaspaka@gmail.com": {"nome": "Cah"}})
print(contatos)
contatos.update({"renatospaka@gmail.com": {"nome": "Renato", "telefone": "2222"}})

#{}.values
contatos = {
    "camilaspaka@gmail.com": {"nome": "Camila", "telefone": "1111-2222"},
    "mariliaspaka@gmail.com": {"nome": "Marilia", "telefone": "2222-3333"},"extra": {"a": 1},
}
contatos.values()

#in
contatos = {
    "camilaspaka@gmail.com": {"nome": "Camila", "telefone": "1111-2222"},
    "mariliaspaka@gmail.com": {"nome": "Marilia", "telefone": "2222-3333"},"extra": {"a": 1},
}
"camilaspaka@gmail.com" in contatos
"mariliaspaka@gmail.com" in contatos
"idade" in contatos["mariliaspaka@gmail.com"]

#del
contatos = {
    "camilaspaka@gmail.com": {"nome": "Camila", "telefone": "1111-2222"},
    "mariliaspaka@gmail.com": {"nome": "Marilia", "telefone": "2222-3333"},"extra": {"a": 1},
}

del contatos["camilaspaka@gmail.com"]["telefone"]