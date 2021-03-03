from agregacao import Cliente,Conta

c1 = Cliente("Madruga","4002-8922","123.123.321-60","Rua das patativas 35, Bairro ilhinha")
account = Conta(123,c1,1100,2000)

print(f"\n\nO Cliente {account.cliente.nome} \nPossui um saldo de:{account.saldo} \nReside no endereço {account.cliente.endereco}\nclSeu telefone é:{account.cliente.telefone}\n\n")