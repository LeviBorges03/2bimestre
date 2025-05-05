def calculadora_imc(pessoa):
    imc= pessoa ["peso"]/pessoa["altura"]*pessoa["altura"]
    resultado = f"o IMC de {pessoa['nome']} é {imc:.2f}"
    #"comando ternario:"
    saudavel = imc < 18.5 and imc > 25
    print(saudavel)

    return{
        "nome": pessoa["nome"],
        "imc": imc,
        "resultado": resultado,
        "saudavel": saudavel
    }

pessoa1={
    
    "nome": "jose",
    "peso": 110,
    "altura": 1.75
}

print(calculadora_imc(pessoa1))


pessoa2={
    "nome": "Ana",
    "peso": 65,
    "altura": 1.63
}

print(calculadora_imc(pessoa2))