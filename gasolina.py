# código de geração do gráfico
import pandas as pd
import seaborn as sns


dados_gasolina = pd.read_csv('gasolina.csv')


with sns.axes_style('darkgrid'):
 grafico_gasolina = sns.lineplot(
   x = 'venda',
   y = 'dia',
   data = dados_gasolina
 )

 grafico_gasolina.set(
   title = 'Preço médio de venda de gasolina na cidade de São Paulo',
   xlabel = 'Preço',
   ylabel = 'Dia (R$)'
 )

 figura = grafico_gasolina.get_figure()
 figura.savefig('gasolina.png', dpi=600) # código de geração do gráfico
