import pandas as pd

# 1. Criando um DataFrame
dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'Idade': [23, 35, 45, 29],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Salvador'],
    'Salario': [2500, 4000, 3500, 3000]
}

df = pd.DataFrame(dados)

# 2. Exibindo o DataFrame
print("DataFrame Inicial:")
print(df)

# 3. Filtrando pessoas com salário maior que 3000
salario_alto = df[df['Salario'] > 3000]
print("\nPessoas com salário maior que 3000:")
print(salario_alto)

# 4. Calculando a média salarial
media_salario = df['Salario'].mean()
print(f"\nMédia Salarial: {media_salario:.2f}")

# 5. Adicionando uma nova coluna "Bonus", que é 10% do salário
df['Bonus'] = df['Salario'] * 0.10
print("\nDataFrame com coluna de bônus:")
print(df)

# 6. Salvando o DataFrame atualizado em um arquivo CSV
df.to_csv('dados_pandas.csv', index=False)
print("\nDados salvos no arquivo 'dados_pandas.csv'")
