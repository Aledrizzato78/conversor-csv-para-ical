CSV para iCal
Este repositório contém um script Python para converter um arquivo CSV em um calendário iCal (.ics). O script lê um arquivo CSV contendo informações sobre eventos, como datas de vencimento, descrições e outros detalhes, e cria um arquivo iCal que pode ser importado para aplicativos de calendário.

Requisitos
Python 3.x
Bibliotecas Python:
pandas
ics
Você pode instalar as bibliotecas necessárias usando pip:

sh
Copy code
pip install pandas ics
Uso
Clone este repositório ou baixe o arquivo do script.
Prepare um arquivo CSV com a estrutura esperada:
A primeira linha do arquivo CSV deve conter os cabeçalhos: vencimento, descrição, grupo, valor, situação.
A coluna vencimento deve conter datas que serão convertidas para o formato de eventos do iCal.
Modifique as variáveis csv_arquivo e ical_arquivo no script para apontar para o caminho do seu arquivo CSV de entrada e para onde deseja salvar o arquivo iCal de saída.
Estrutura do CSV
O arquivo CSV deve ter a seguinte estrutura:

vencimento	descrição	grupo	valor	situação
2023-05-01	Pagar aluguel	Casa	1000	Pendente
2023-05-10	Conta de luz	Casa	200	Paga
2023-05-15	Fatura do cartão	Banco	500	Pendente
Exemplo de uso
O exemplo abaixo mostra como configurar e executar o script:

python
Copy code
csv_arquivo = r'C:\Caminho\Para\Seu\Arquivo.csv'
ical_arquivo = r'C:\Caminho\Para\Salvar\Arquivo.ics'
csv_para_ical(csv_arquivo, ical_arquivo)
print(f'Arquivo {ical_arquivo} gerado com sucesso.')
Função csv_para_ical
A função csv_para_ical realiza as seguintes etapas:

Lê o arquivo CSV utilizando a codificação 'latin1'.
Remove as linhas com valores nulos na coluna 'vencimento'.
Converte a coluna 'vencimento' para o formato datetime.
Cria um novo calendário.
Para cada linha do CSV, cria um evento iCal e adiciona ao calendário.
Salva o calendário no arquivo iCal especificado.
python
Copy code
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
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
