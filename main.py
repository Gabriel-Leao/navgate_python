import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import csv
import os


# Função para capturar dados fornecidos pelo usuário
def capture_data_from_user(num_samples):
    time_stamps = [datetime.now() - timedelta(minutes=i) for i in range(num_samples)]
    time_stamps.reverse()  # Reverter para que os timestamps estejam em ordem cronológica
    ph_values = []
    temp_values = []
    ldr_values = []

    for i in range(num_samples):
        while True:
            try:
                ph = float(input(f"Digite o valor de pH para a amostra {i+1}: "))
                temp = float(input(f"Digite o valor da temperatura (°C) para a amostra {i+1}: "))
                ldr = float(input(f"Digite o valor da luminosidade para a amostra {i+1} (0-100): "))
                ph_values.append(ph)
                temp_values.append(temp)
                ldr_values.append(ldr)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira valores numéricos.")

    return time_stamps, np.array(ph_values), np.array(temp_values), np.array(ldr_values)


# Função para salvar dados em um arquivo CSV
def save_data_to_csv(file_name, time_stamps, ph_values, temp_values, ldr_values):
    file_exists = os.path.isfile(file_name)
    try:
        with open(file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Timestamp", "pH", "Temperatura (°C)", "Luminosidade"])
            for i in range(len(time_stamps)):
                writer.writerow([time_stamps[i].strftime('%Y-%m-%d %H:%M:%S'),
                                 f"{ph_values[i]:.2f}",
                                 f"{temp_values[i]:.2f}",
                                 f"{ldr_values[i]:.2f}"])
        if file_exists:
            print(f"Arquivo CSV '{file_name}' atualizado.")
        else:
            print(f"Dados salvos em '{file_name}'.")
    except Exception as e:
        print(f"Erro ao salvar dados no arquivo: {e}")


# Função para ler dados de um arquivo CSV
def read_data_from_csv(file_name):
    time_stamps = []
    ph_values = []
    temp_values = []
    ldr_values = []

    try:
        with open(file_name, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                time_stamps.append(datetime.strptime(row["Timestamp"], '%Y-%m-%d %H:%M:%S'))
                ph_values.append(float(row["pH"]))
                temp_values.append(float(row["Temperatura (°C)"]))
                ldr_values.append(float(row["Luminosidade"]))
        return time_stamps, np.array(ph_values), np.array(temp_values), np.array(ldr_values)
    except Exception as e:
        print(f"Erro ao ler dados do arquivo: {e}")
        return [], [], [], []


# Função para apresentar os dados em gráficos
def present_data(all_time_stamps, all_ph_values, all_temp_values, all_ldr_values):
    plt.figure(figsize=(19.2, 10.8))

    # Gráfico de pH
    plt.subplot(3, 1, 1)
    plt.plot(all_ph_values, label='pH', color='blue')
    for i, txt in enumerate(all_ph_values):
        plt.annotate(f'{round(txt, 2)}', (i, all_ph_values[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    plt.ylabel('pH')
    plt.title('Níveis de pH ao longo do tempo', pad=20)
    plt.legend()

    # Gráfico de Temperatura
    plt.subplot(3, 1, 2)
    plt.plot(all_temp_values, label='Temperatura (°C)', color='red')
    for i, txt in enumerate(all_temp_values):
        plt.annotate(f'{round(txt, 2)}', (i, all_temp_values[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    plt.ylabel('Temperatura (°C)')
    plt.title('Níveis de temperatura ao longo do tempo', pad=20)
    plt.legend()

    # Gráfico de Luminosidade
    plt.subplot(3, 1, 3)
    plt.plot(all_ldr_values, label='Luminosidade', color='green')
    for i, txt in enumerate(all_ldr_values):
        plt.annotate(f'{round(txt, 2)}', (i, all_ldr_values[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    plt.ylabel('Luminosidade')
    plt.title('Níveis de luminosidade ao longo do tempo', pad=20)
    plt.legend()

    plt.tight_layout()
    plt.savefig('graficos_saude_oceanica.png')  # Salvar o gráfico como imagem
    print("Gráficos salvos como 'graficos_saude_oceanica.png'")
    plt.show()


# Função principal para executar o protótipo
def main():
    try:
        num_samples = int(input("Digite o número de amostras: "))
        if num_samples <= 0:
            raise ValueError("O número de amostras deve ser um inteiro positivo.")

        csv_file_name = 'dados_saude_oceanica.csv'
        img_file_name = 'graficos_saude_oceanica.png'

        time_stamps, ph_values, temp_values, ldr_values = capture_data_from_user(num_samples)

        # Salvar dados em um arquivo CSV
        save_data_to_csv(csv_file_name, time_stamps, ph_values, temp_values, ldr_values)

        # Ler dados do arquivo CSV
        time_stamps, ph_values, temp_values, ldr_values = read_data_from_csv(csv_file_name)

        # Apresentar dados processados
        present_data(time_stamps, ph_values, temp_values, ldr_values)

        print(f"Gráficos salvos como '{img_file_name}'.")

    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    main()
