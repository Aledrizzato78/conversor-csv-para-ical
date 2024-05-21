import pandas as pd
from ics import Calendar, Event

def csv_para_ical(csv_arquivo, ical_arquivo):
    # Lê o arquivo CSV com a codificação 'latin1'
    df = pd.read_csv(csv_arquivo, encoding='latin1')
    
    # Remove linhas com valores nulos na coluna 'vencimento'
    df.dropna(subset=['vencimento'], inplace=True)
    
    # Converte a coluna 'vencimento' para datetime
    df['vencimento'] = pd.to_datetime(df['vencimento'])
    
    # Cria um novo calendário
    calendario = Calendar()
    
    # Converte cada linha do CSV em um evento iCal
    for index, row in df.iterrows():
        evento = Event()
        evento.name = str(row['descrição'])
        evento.begin = row['vencimento']  # Mantém como objeto Timestamp
        evento.description = f"Grupo: {row['grupo']}\nValor: {row['valor']}\nSituação: {row['situação']}"
        calendario.events.add(evento)
    
    # Salva o calendário em um arquivo iCal
    with open(ical_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(calendario)

# Exemplo de uso
csv_arquivo = r'C:\Users\Latitude 5280\Downloads\controle geral gastos mensal.csv'
ical_arquivo = r'C:\Users\Latitude 5280\Desktop\Projetos\eventos.ics'
csv_para_ical(csv_arquivo, ical_arquivo)
print(f'Arquivo {ical_arquivo} gerado com sucesso.')
