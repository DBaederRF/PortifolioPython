# Explicação do Código
## Criação do DataFrame:

Usei um dicionário para criar um DataFrame com as colunas Nome, Idade, Cidade e Salario.

### Exibição do DataFrame:

print(df) mostra o conteúdo do DataFrame na tela.
Filtragem de Dados:

df[df['Salario'] > 3000] filtra as linhas onde o salário é maior que 3000.
Cálculo da Média Salarial:

df['Salario'].mean() calcula a média dos valores na coluna Salario.
Adicionar uma Nova Coluna:

Adicionamos a coluna Bonus, que corresponde a 10% do valor do salário.
Salvar em CSV:

O DataFrame atualizado é salvo em um arquivo CSV chamado analise.csv.
Como Executar

## Instale o Pandas se ainda não o tiver instalado:

pip install pandas

## Execute o arquivo:

python analise.py

