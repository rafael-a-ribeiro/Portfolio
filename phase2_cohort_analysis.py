"""
FASE 2: Análise de Retenção de Clientes

Este script contém os 3 passos da Fase 2 da análise de cohort.
Copie cada seção para células separadas no notebook.
"""

# =============================================================================
# CÉLULA 1: Markdown - Título da Fase 2
# =============================================================================
"""
## FASE 2: Análise de Retenção de Clientes
Nesta fase, vamos:
1. Agrupar o dataframe pela coluna `CohortMonth` e `CohortIndex` e contar o número de `Customer ID` únicos em cada grupo.
2. Transformar a tabela de contagem em um formato de planilha (Pivot Table), onde as linhas são os `CohortMonth` e as colunas são o `CohortIndex`.
3. Dividir o número de clientes em cada célula pelo número de clientes no Mês 1 (tamanho inicial do cohort). Multiplicar por 100 para obter a porcentagem.
"""

# =============================================================================
# CÉLULA 2: Código - Passo 1: Contagem de Clientes
# =============================================================================
# 1. Contagem de Clientes
# Agrupar por CohortMonth e CohortIndex e contar Customer IDs únicos
cohort_data = df.groupby(['CohortMonth', 'CohortIndex'])['Customer ID'].nunique()

# Resetar o índice para transformar em DataFrame
cohort_data = cohort_data.reset_index()

# Renomear a coluna para melhor entendimento
cohort_data.rename(columns={'Customer ID': 'NumCustomers'}, inplace=True)

print("Dados de cohort agrupados:")
display(cohort_data.head(20))

# =============================================================================
# CÉLULA 3: Código - Passo 2: Pivotamento da Tabela
# =============================================================================
# 2. Pivotamento da Tabela
# Transformar em pivot table: linhas = CohortMonth, colunas = CohortIndex
cohort_counts = cohort_data.pivot(index='CohortMonth', 
                                   columns='CohortIndex', 
                                   values='NumCustomers')

print("Tabela pivotada - Contagem de clientes por cohort:")
display(cohort_counts)

# =============================================================================
# CÉLULA 4: Código - Passo 3: Cálculo da Retenção
# =============================================================================
# 3. Cálculo da Retenção
# Dividir cada célula pelo valor do Mês 1 (primeira coluna) e multiplicar por 100
cohort_sizes = cohort_counts.iloc[:, 0]
retention = cohort_counts.divide(cohort_sizes, axis=0) * 100

print("Taxa de Retenção (%):\n")
display(retention.round(1))

# Estatísticas básicas
print("\nEstatísticas da taxa de retenção:")
print(retention.describe().round(1))
