import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7d5c893d9e294dec18be110d215714e1"
# Your Auth Token from twilio.com/console
auth_token  = "7400ec0828d603154164528606e97e2e"
client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir os arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, "Vendas"].values[0]
        print(f' No mes {mes} alguem bateu a meta. Vendedor: {vendedor}. Vendas: {vendas}')
        message = client.messages.create(
            to="+5551997110194",
            from_="+16204004866",
            body=f' No mes {mes} alguem bateu a meta. Vendedor: {vendedor}. Vendas: {vendas}')

        print(message.sid)

# Para cada arquivo:

# Verificar se algum valor na coluna vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendendor

# Caso não seja maior do que 55.000 não quero fazer nada


