aluno = dict()

aluno['nome'] = input('Digite o nome do aluno:\n')
aluno['media'] = float(input('Digite a média do aluno:\n'))

print(f'O aluno {aluno["nome"]}, possui mnedia {aluno["media"]}, portanto ele está\n')
if aluno['media'] >= 7:
    print('Aprovado :D')
    aluno['situação'] = 'Aprovado'
elif aluno['media'] <= 3:
    print('Reprovado :C')
    aluno['situação'] = 'Reprovado'
else:
    print('Recuperação :|')
    aluno['situação'] = 'Recuperação'

print(aluno.items())