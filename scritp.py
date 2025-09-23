print("Olá, Tudo bem?")
print("Vamos valida seus dados")

nome = input("Qual o seu nome: ")
idade = int(input("Qual a sua idade: "))
email= input("Qual o seu Email: ")

if idade > 16:
  print("Seu cadastro foi relizado com sucesso festa agendada para 2026")
else:
  print("Você não tem idade para ir há essa festa")





with open ("base_dados.csv", "a") as arquivo:
      arquivo.write(f"Convidado confirmado(a) {nome}, {idade}, {email}.\n")
