nAlunos = int(input("Digite o número de alunos: "))

totalMedia = 0
alunos = []

for _ in range(nAlunos):
    nome = input("\nDigite o nome do aluno: ")
    notas = []
    
    for i in range(1, 4):
        nota = float(input(f"Digite a nota {i} de {nome}: "))
        notas.append(nota)
    
    media = sum(notas) / len(notas)
    totalMedia += media
    
    situacao = "Aprovado" if media >= 7.0 else "Reprovado"
    
    alunos.append((nome, notas, media, situacao))

print("\nResultado final:")
for aluno in alunos:
    nome, notas, media, situacao = aluno
    print(f"Nome: {nome}, Notas: {notas}, Média: {media:.2f}, Situação: {situacao}")

media_geral = totalMedia / nAlunos if nAlunos > 0 else 0
print(f"\nMédia geral da turma: {media_geral:.2f}")