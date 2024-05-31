# Projeto de Monitoramento da Saúde Oceânica

## Descrição do Projeto

Este projeto tem como objetivo capturar, armazenar e visualizar dados relacionados à saúde oceânica. Os dados coletados incluem valores de pH, temperatura e luminosidade. O programa permite que os usuários insiram manualmente os dados, que são então salvos em um arquivo CSV e visualizados através de gráficos gerados com a biblioteca Matplotlib.

## Funcionalidades

- Captura de dados de pH, temperatura e luminosidade fornecidos pelo usuário.
- Armazenamento de dados em um arquivo CSV.
- Leitura de dados de um arquivo CSV existente.
- Geração de gráficos para visualização dos dados capturados.

## Requisitos

- Python 3.x
- Bibliotecas:
    - numpy
    - matplotlib
    - datetime
    - csv
    - os

## Instruções de Uso

1. Clone este repositório para sua máquina local.

   ```bash
   git clone https://github.com/Gabriel-Leao/navgate_python.git

2. Instale as dependências necessárias utilizando `pip`:
   ```bash
   pip install numpy matplotlib
3. Execute o programa principal:
   ```bash
   python main.py
4. Siga as instruções no terminal para inserir os dados de pH, temperatura e luminosidade.
5. Os dados inseridos serão salvos no arquivo 'dados_saude_oceanica.csv' e os gráficos serão gerados e salvos como 'graficos_saude_oceanica.png'.

## Estrutura do Projeto
    ├── main.py
    ├── dados_saude_oceanica.csv
    └── graficos_saude_oceanica.png

## Detalhes do Código

### Função capture_data_from_user
Captura os dados de pH, temperatura e luminosidade fornecidos pelo usuário. Os dados são coletados para o número de amostras especificado e armazenados em listas separadas.

### Função save_data_to_csv
Salva os dados capturados em um arquivo CSV. Se o arquivo já existir, os dados são adicionados ao final do arquivo; caso contrário, um novo arquivo é criado com um cabeçalho apropriado.

### Função read_data_from_csv
Lê os dados de um arquivo CSV existente e retorna os dados em listas separadas.

### Função present_data
Gera gráficos para os dados de pH, temperatura e luminosidade e salva os gráficos como uma imagem PNG.

### Função main
Executa o fluxo completo do programa: captura de dados, salvamento em CSV, leitura de dados existentes e geração de gráficos.

## Observações
Certifique-se de inserir valores numéricos válidos ao capturar os dados. O programa combina dados novos com dados existentes ao gerar gráficos, permitindo uma visualização contínua dos dados ao longo do tempo.

## Equipe

Este projeto foi desenvolvido por:

- **Eduardo Brites** - RM 552943
- **Gabriel Leão** - RM 552642
- **Karolina Soares** - RM 554187

## Licença
Este projeto está licenciado sob a MIT License.

---
