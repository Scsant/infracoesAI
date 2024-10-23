import streamlit as st
import requests
from datetime import datetime
from dotenv import load_dotenv
import os

# Especifica o caminho completo para o arquivo gemai.env
load_dotenv(dotenv_path='gemai.env')

# Tentar obter a chave da API
api_key = os.getenv("API_KEY")



# Função para determinar se é manhã ou tarde
def gerar_saudacao():
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Olá"
    else:
        return "Olá"

# Função para formatar a tabela de dados em formato de texto

tabela_velocidade = [
    {
        "Data": "20/10/2024",
        "Hora": "12:27:11",
        "Filial": "Plácidos",
        "Motorista": "Denilson Lemes",
        "Veículo": "001997 - FYM6H86",
        "Hodômetro (km)": 3528500,
        "Duração (hh:mm:ss)": "00:00:10",
        "Velocidade (Km/h)": 46,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 12:46:32",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.98640+-48.55260"
    },
    {
        "Data": "20/10/2024",
        "Hora": "12:41:22",
        "Filial": "Plácidos",
        "Motorista": "Denilson Lemes",
        "Veículo": "001997 - FYM6H86",
        "Hodômetro (km)": 3528581,
        "Duração (hh:mm:ss)": "00:00:19",
        "Velocidade (Km/h)": 72,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 12:45:48",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.95100+-48.50570"
    },
    {
        "Data": "19/10/2024",
        "Hora": "11:35:51",
        "Filial": "Plácidos",
        "Motorista": "Jose Damiao Do Nascimento",
        "Veículo": "002013 - FCF6D94",
        "Hodômetro (km)": 3539907,
        "Duração (hh:mm:ss)": "00:00:08",
        "Velocidade (Km/h)": 51,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "19/10/2024 11:55:51",
        "Usuário da Ação": "Pedro Henrique Leodoro Martins",
        "Local": "https://www.google.com/maps?q=-22.98620+-48.55240"
    },
    {
        "Data": "20/10/2024",
        "Hora": "05:26:48",
        "Filial": "Plácidos",
        "Motorista": "Marcos Gonçalves Leite",
        "Veículo": "002042 - FLP3F47",
        "Hodômetro (km)": 3686269,
        "Duração (hh:mm:ss)": "00:00:18",
        "Velocidade (Km/h)": 34,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA_2",
        "Ação": "Válido",
        "Data da Ação": "20/10/2024 05:44:26",
        "Usuário da Ação": "Ianca Luata Da Silva",
        "Local": "https://www.google.com/maps?q=-22.94730+-48.49680"
    },
    {
        "Data": "20/10/2024",
        "Hora": "06:38:29",
        "Filial": "Plácidos",
        "Motorista": "Luiz Carlos Da Silva",
        "Veículo": "002062 - FKP6H84",
        "Hodômetro (km)": 3663929,
        "Duração (hh:mm:ss)": "00:00:13",
        "Velocidade (Km/h)": 45,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 07:43:44",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.95130+-48.50610"
    },
    {
        "Data": "20/10/2024",
        "Hora": "06:40:15",
        "Filial": "Plácidos",
        "Motorista": "Luiz Carlos Da Silva",
        "Veículo": "002062 - FKP6H84",
        "Hodômetro (km)": 3663940,
        "Duração (hh:mm:ss)": "00:00:14",
        "Velocidade (Km/h)": 34,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA_2",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 07:38:04",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.94730+-48.49680"
    },
    {
        "Data": "19/10/2024",
        "Hora": "14:08:03",
        "Filial": "Plácidos",
        "Motorista": "Jose Benedito Lourenço",
        "Veículo": "002436 - GJH6F43",
        "Hodômetro (km)": 2648076,
        "Duração (hh:mm:ss)": "00:00:11",
        "Velocidade (Km/h)": 51,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "19/10/2024 15:12:06",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-22.95120+-48.50600"
    },
    {
        "Data": "22/10/2024",
        "Hora": "11:43:02",
        "Filial": "Plácidos",
        "Motorista": "Jose Benedito Lourenço",
        "Veículo": "002436 - GJH6F43",
        "Hodômetro (km)": 2661285,
        "Duração (hh:mm:ss)": "00:00:12",
        "Velocidade (Km/h)": 45,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 11:52:55",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.95120+-48.50610"
    },
    {
        "Data": "22/10/2024",
        "Hora": "06:39:45",
        "Filial": "Plácidos",
        "Motorista": "Paulo Dos Santos Tavares",
        "Veículo": "002441 - GGG5H44",
        "Hodômetro (km)": 2949499,
        "Duração (hh:mm:ss)": "00:00:09",
        "Velocidade (Km/h)": 27,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_ROTATORIA SAIDA RONDON ",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 06:43:00",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.56630+-48.82240"
    },
    {
        "Data": "19/10/2024",
        "Hora": "17:17:42",
        "Filial": "Plácidos",
        "Motorista": "Luis Cesar Giacomini",
        "Veículo": "002442 - GHH9H03",
        "Hodômetro (km)": 2539881,
        "Duração (hh:mm:ss)": "00:00:10",
        "Velocidade (Km/h)": 51,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "19/10/2024 17:29:57",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-22.95120+-48.50590"
    },
    {
        "Data": "19/10/2024",
        "Hora": "15:11:59",
        "Filial": "Plácidos",
        "Motorista": "Rildo Tonholi",
        "Veículo": "002444 - FYM6A84",
        "Hodômetro (km)": 2787979,
        "Duração (hh:mm:ss)": "00:00:07",
        "Velocidade (Km/h)": 34,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA_2",
        "Ação": "Valido",
        "Data da Ação": "19/10/2024 17:30:16",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-22.94750+-48.49650"
    },
    {
        "Data": "19/10/2024",
        "Hora": "14:19:05",
        "Filial": "Plácidos",
        "Motorista": "Darci Aparecido Lopes",
        "Veículo": "002452 - FPU1A72",
        "Hodômetro (km)": 2856198,
        "Duração (hh:mm:ss)": "00:00:14",
        "Velocidade (Km/h)": 35,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA_2",
        "Ação": "Valido",
        "Data da Ação": "19/10/2024 15:14:25",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-22.94730+-48.49700"
    },
    {
        "Data": "19/10/2024",
        "Hora": "18:09:35",
        "Filial": "Plácidos",
        "Motorista": "Lucas Francisco Garcia",
        "Veículo": "002716 - FPL2D43",
        "Hodômetro (km)": 3683660,
        "Duração (hh:mm:ss)": "00:00:11",
        "Velocidade (Km/h)": 37,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "19/10/2024 20:30:29",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-22.98660+-48.55240"
    },
    {
        "Data": "21/10/2024",
        "Hora": "21:19:57",
        "Filial": "Plácidos",
        "Motorista": "Gentil Francisco Dos Santos",
        "Veículo": "002716 - FPL2D43",
        "Hodômetro (km)": 3693292,
        "Duração (hh:mm:ss)": "00:00:09",
        "Velocidade (Km/h)": 48,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 21:25:16",
        "Usuário da Ação": "Pedro Henrique Leodoro Martins",
        "Local": "https://www.google.com/maps?q=-22.95120+-48.50570"
    },
    {
        "Data": "22/10/2024",
        "Hora": "12:33:34",
        "Filial": "Plácidos",
        "Motorista": "Rogerio Da Silva Oliveira",
        "Veículo": "002716 - FPL2D43",
        "Hodômetro (km)": 3697092,
        "Duração (hh:mm:ss)": "00:00:11",
        "Velocidade (Km/h)": 48,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 12:48:28",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.95120+-48.50590"
    },
    {
        "Data": "22/10/2024",
        "Hora": "12:35:13",
        "Filial": "Plácidos",
        "Motorista": "Rogerio Da Silva Oliveira",
        "Veículo": "002716 - FPL2D43",
        "Hodômetro (km)": 3697103,
        "Duração (hh:mm:ss)": "00:00:12",
        "Velocidade (Km/h)": 39,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA_2",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 12:48:51",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.94730+-48.49680"
    },
    {
        "Data": "19/10/2024",
        "Hora": "08:57:50",
        "Filial": "Plácidos",
        "Motorista": "Paulo Renato Da Silva",
        "Veículo": "002921 - GDN3C62",
        "Hodômetro (km)": 2460999,
        "Duração (hh:mm:ss)": "00:00:14",
        "Velocidade (Km/h)": 42,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "19/10/2024 09:23:50",
        "Usuário da Ação": "Pedro Henrique Leodoro Martins",
        "Local": "https://www.google.com/maps?q=-22.98650+-48.55260"
    },
    {
        "Data": "21/10/2024",
        "Hora": "08:15:28",
        "Filial": "Plácidos",
        "Motorista": "Julio Cesar Barbosa Oliveira",
        "Veículo": "002921 - GDN3C62",
        "Hodômetro (km)": 2470350,
        "Duração (hh:mm:ss)": "00:00:11",
        "Velocidade (Km/h)": 49,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 12:03:02",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.98640+-48.55240"
    },
    {
        "Data": "19/10/2024",
        "Hora": "01:44:34",
        "Filial": "Plácidos",
        "Motorista": "Joao Gilberto Erba",
        "Veículo": "002925 - FWE4B86",
        "Hodômetro (km)": 4301204,
        "Duração (hh:mm:ss)": "00:00:13",
        "Velocidade (Km/h)": 46,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Válido",
        "Data da Ação": "19/10/2024 03:44:42",
        "Usuário da Ação": "Ianca Luata Da Silva",
        "Local": "https://www.google.com/maps?q=-22.95120+-48.50610"
    },
    {
        "Data": "19/10/2024",
        "Hora": "01:46:08",
        "Filial": "Plácidos",
        "Motorista": "Joao Gilberto Erba",
        "Veículo": "002925 - FWE4B86",
        "Hodômetro (km)": 4301214,
        "Duração (hh:mm:ss)": "00:00:11",
        "Velocidade (Km/h)": 34,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA_2",
        "Ação": "Válido",
        "Data da Ação": "19/10/2024 03:45:34",
        "Usuário da Ação": "Ianca Luata Da Silva",
        "Local": "https://www.google.com/maps?q=-22.94730+-48.49690"
    },
    {
        "Data": "21/10/2024",
        "Hora": "08:26:51",
        "Filial": "Plácidos",
        "Motorista": "Leandro Aparecido De Oliveira",
        "Veículo": "002925 - FWE4B86",
        "Hodômetro (km)": 4310725,
        "Duração (hh:mm:ss)": "00:00:11",
        "Velocidade (Km/h)": 64,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 12:02:44",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.98640+-48.55250"
    },
    {
        "Data": "21/10/2024",
        "Hora": "08:35:49",
        "Filial": "Plácidos",
        "Motorista": "Leandro Aparecido De Oliveira",
        "Veículo": "002925 - FWE4B86",
        "Hodômetro (km)": 4310791,
        "Duração (hh:mm:ss)": "00:00:11",
        "Velocidade (Km/h)": 55,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 12:06:54",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.95120+-48.50590"
    },
    {
        "Data": "21/10/2024",
        "Hora": "08:37:18",
        "Filial": "Plácidos",
        "Motorista": "Leandro Aparecido De Oliveira",
        "Veículo": "002925 - FWE4B86",
        "Hodômetro (km)": 4310802,
        "Duração (hh:mm:ss)": "00:00:11",
        "Velocidade (Km/h)": 42,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA_2",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 12:02:18",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.94740+-48.49670"
    },
    {
        "Data": "22/10/2024",
        "Hora": "09:14:01",
        "Filial": "Plácidos",
        "Motorista": "Motorista Ee1622140206",
        "Veículo": "002925 - FWE4B86",
        "Hodômetro (km)": 4316502,
        "Duração (hh:mm:ss)": "00:00:09",
        "Velocidade (Km/h)": 56,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 09:19:35",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.95110+-48.50580"
    },
    {
        "Data": "22/10/2024",
        "Hora": "09:15:30",
        "Filial": "Plácidos",
        "Motorista": "Motorista Ee1622140206",
        "Veículo": "002925 - FWE4B86",
        "Hodômetro (km)": 4316513,
        "Duração (hh:mm:ss)": "00:00:11",
        "Velocidade (Km/h)": 38,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA_2",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 09:25:53",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.94740+-48.49660"
    },
    {
        "Data": "19/10/2024",
        "Hora": "15:43:01",
        "Filial": "Plácidos",
        "Motorista": "Edy Vieira Da Silva",
        "Veículo": "003623 - GDH1D15",
        "Hodômetro (km)": 2566117,
        "Duração (hh:mm:ss)": "00:00:10",
        "Velocidade (Km/h)": 34,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA_2",
        "Ação": "Valido",
        "Data da Ação": "19/10/2024 17:30:59",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-22.94740+-48.49670"
    },
    {
        "Data": "21/10/2024",
        "Hora": "10:20:19",
        "Filial": "Plácidos",
        "Motorista": "Djalma Aparecido Domingos",
        "Veículo": "003623 - GDH1D15",
        "Hodômetro (km)": 2573591,
        "Duração (hh:mm:ss)": "00:00:10",
        "Velocidade (Km/h)": 36,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 12:06:24",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.98620+-48.55240"
    },
    {
        "Data": "20/10/2024",
        "Hora": "13:15:35",
        "Filial": "Plácidos",
        "Motorista": "Vanderlei Aparecido Gasparelli",
        "Veículo": "003624 - FUT5E26",
        "Hodômetro (km)": 2790776,
        "Duração (hh:mm:ss)": "00:00:12",
        "Velocidade (Km/h)": 44,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 13:18:59",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.98640+-48.55250"
    },
    {
        "Data": "22/10/2024",
        "Hora": "06:09:41",
        "Filial": "Plácidos",
        "Motorista": "Vanderlei Aparecido Gasparelli",
        "Veículo": "003624 - FUT5E26",
        "Hodômetro (km)": 2799078,
        "Duração (hh:mm:ss)": "00:00:11",
        "Velocidade (Km/h)": 26,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_SAIDA DA RONDON ",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 06:44:30",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.56750+-48.82310"
    },
    {
        "Data": "19/10/2024",
        "Hora": "14:13:18",
        "Filial": "BTF 03",
        "Motorista": "Btf3 - Arlindo Vicente Filho",
        "Veículo": "044009 - BYI1F44",
        "Hodômetro (km)": 3278104,
        "Duração (hh:mm:ss)": "00:00:15",
        "Velocidade (Km/h)": 85,
        "Limite (Km/h)": 80,
        "Cerca Embarcada": "-",
        "Ação": "Valido",
        "Data da Ação": "19/10/2024 15:24:32",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-22.86240+-48.16810"
    },
    {
        "Data": "20/10/2024",
        "Hora": "04:58:15",
        "Filial": "BTF 03",
        "Motorista": "Btf3 - Daniel De Oliveira",
        "Veículo": "044009 - BYI1F44",
        "Hodômetro (km)": 3280819,
        "Duração (hh:mm:ss)": "00:00:14",
        "Velocidade (Km/h)": 85,
        "Limite (Km/h)": 80,
        "Cerca Embarcada": "-",
        "Ação": "Válido",
        "Data da Ação": "20/10/2024 05:11:30",
        "Usuário da Ação": "Ianca Luata Da Silva",
        "Local": "https://www.google.com/maps?q=-22.85360+-48.49510"
    },
    {
        "Data": "22/10/2024",
        "Hora": "10:12:46",
        "Filial": "BTF 03",
        "Motorista": "Btf3 - Izaltino Miguel De Oliveira",
        "Veículo": "044014 - BYI9E76",
        "Hodômetro (km)": 3459037,
        "Duração (hh:mm:ss)": "00:02:51",
        "Velocidade (Km/h)": 92,
        "Limite (Km/h)": 80,
        "Cerca Embarcada": "-",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 10:45:57",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.56120+-48.81650"
    },
    {
        "Data": "22/10/2024",
        "Hora": "07:06:37",
        "Filial": "BTF 05",
        "Motorista": "Btf5 - Sergio Antonio Pereira De Freitas Junior",
        "Veículo": "044016 - BOC1D64",
        "Hodômetro (km)": 3662958,
        "Duração (hh:mm:ss)": "00:00:15",
        "Velocidade (Km/h)": 86,
        "Limite (Km/h)": 80,
        "Cerca Embarcada": "-",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 07:44:46",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.36570+-49.03890"
    },
    {
        "Data": "19/10/2024",
        "Hora": "09:33:13",
        "Filial": "BTF 01",
        "Motorista": "Btf1 - Lincoln Marcos De Abreu",
        "Veículo": "044042 - FCZ5H71",
        "Hodômetro (km)": 2828329,
        "Duração (hh:mm:ss)": "00:00:12",
        "Velocidade (Km/h)": 47,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "19/10/2024 10:16:40",
        "Usuário da Ação": "Pedro Henrique Leodoro Martins",
        "Local": "https://www.google.com/maps?q=-22.95120+-48.50600"
    },
    {
        "Data": "19/10/2024",
        "Hora": "04:18:39",
        "Filial": "BTF 03",
        "Motorista": "Btf3 - Samuel Da Silva Cordeiro",
        "Veículo": "044044 - ELO6F45",
        "Hodômetro (km)": 3035667,
        "Duração (hh:mm:ss)": "00:00:08",
        "Velocidade (Km/h)": 50,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_SERRINHA BOTUCATU 5",
        "Ação": "Válido",
        "Data da Ação": "19/10/2024 05:52:10",
        "Usuário da Ação": "Ianca Luata Da Silva",
        "Local": "https://www.google.com/maps?q=-22.93230+-48.35750"
    },
    {
        "Data": "21/10/2024",
        "Hora": "01:00:22",
        "Filial": "BTF 05",
        "Motorista": "Btf5 - Laercio Da Silva Cardoso",
        "Veículo": "044056 - BZF0D46",
        "Hodômetro (km)": 3270429,
        "Duração (hh:mm:ss)": "00:00:08",
        "Velocidade (Km/h)": 25,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_ROTATORIA AVAI",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 01:26:47",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-22.11960+-49.30570"
    },
    {
        "Data": "20/10/2024",
        "Hora": "20:35:36",
        "Filial": "BTF 05",
        "Motorista": "Btf5 - Joao Andre",
        "Veículo": "044067 - BPQ6D13",
        "Hodômetro (km)": 3364671,
        "Duração (hh:mm:ss)": "00:00:08",
        "Velocidade (Km/h)": 27,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_ROTATORIA LWART",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 20:39:53",
        "Usuário da Ação": "Pedro Henrique Leodoro Martins",
        "Local": "https://www.google.com/maps?q=-22.56110+-48.81690"
    },
    {
        "Data": "22/10/2024",
        "Hora": "11:10:54",
        "Filial": "BTF 04",
        "Motorista": "Btf4 - Alessandro Aparecido Porto",
        "Veículo": "044072 - GAG4A43",
        "Hodômetro (km)": 3232054,
        "Duração (hh:mm:ss)": "00:00:24",
        "Velocidade (Km/h)": 25,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_ROTATORIA POSTO PAULISTANIA",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 11:50:35",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.57320+-49.37260"
    },
    {
        "Data": "19/10/2024",
        "Hora": "19:50:09",
        "Filial": "BTF 04",
        "Motorista": "Btf4 - Keber Antonio Cruz Ferreira",
        "Veículo": "044076 - FWO3G71",
        "Hodômetro (km)": 3178338,
        "Duração (hh:mm:ss)": "00:00:25",
        "Velocidade (Km/h)": 45,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PREVISAO CHEGADA",
        "Ação": "Valido",
        "Data da Ação": "19/10/2024 20:36:25",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-22.54110+-48.81050"
    },
    {
        "Data": "20/10/2024",
        "Hora": "00:15:49",
        "Filial": "BTF 04",
        "Motorista": "Btf4 - Edson Luis De Franca",
        "Veículo": "044080 - EJT5F36",
        "Hodômetro (km)": 3346832,
        "Duração (hh:mm:ss)": "00:00:24",
        "Velocidade (Km/h)": 24,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_ROTATORIA POSTO PAULISTANIA",
        "Ação": "Válido",
        "Data da Ação": "20/10/2024 00:42:17",
        "Usuário da Ação": "Ianca Luata Da Silva",
        "Local": "https://www.google.com/maps?q=-22.57340+-49.37260"
    },
    {
        "Data": "20/10/2024",
        "Hora": "17:16:18",
        "Filial": "BTF 04",
        "Motorista": "Btf4 - Edson Luis De Franca",
        "Veículo": "044080 - EJT5F36",
        "Hodômetro (km)": 3350517,
        "Duração (hh:mm:ss)": "00:00:14",
        "Velocidade (Km/h)": 25,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_ROTATORIA POSTO PAULISTANIA",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 17:24:25",
        "Usuário da Ação": "Pedro Henrique Leodoro Martins",
        "Local": "https://www.google.com/maps?q=-22.57330+-49.37270"
    },
    {
        "Data": "22/10/2024",
        "Hora": "07:26:20",
        "Filial": "BTF 04",
        "Motorista": "Btf4 - Fabiano Costa De Lima",
        "Veículo": "044085 - EHH4H41",
        "Hodômetro (km)": 3462643,
        "Duração (hh:mm:ss)": "00:00:17",
        "Velocidade (Km/h)": 24,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_ROTATORIA POSTO PAULISTANIA",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 07:47:50",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.57310+-49.37260"
    },
    {
        "Data": "20/10/2024",
        "Hora": "12:55:34",
        "Filial": "BTF 04",
        "Motorista": "Btf4 - Fabiano Costa De Lima",
        "Veículo": "044097 - ECU9H75",
        "Hodômetro (km)": 2970233,
        "Duração (hh:mm:ss)": "00:00:23",
        "Velocidade (Km/h)": 30,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_ROTATORIA POSTO PAULISTANIA",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 13:01:27",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.57310+-49.37260"
    },
    {
        "Data": "21/10/2024",
        "Hora": "22:21:37",
        "Filial": "BTF 04",
        "Motorista": "Btf4 - Cleisson Souza Rocha",
        "Veículo": "044099 - EOD6H96",
        "Hodômetro (km)": 3188246,
        "Duração (hh:mm:ss)": "00:00:14",
        "Velocidade (Km/h)": 25,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_ROTATORIA POSTO PAULISTANIA",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 22:45:16",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-22.57320+-49.37260"
    },
    {
        "Data": "22/10/2024",
        "Hora": "11:42:55",
        "Filial": "BTF 03",
        "Motorista": "Btf3 - Robson Carlos Pascoine",
        "Veículo": "044119 - GCK4B01",
        "Hodômetro (km)": 2094052,
        "Duração (hh:mm:ss)": "00:00:19",
        "Velocidade (Km/h)": 46,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PREVISAO CHEGADA",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 11:53:18",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.54070+-48.81040"
    },
    {
        "Data": "20/10/2024",
        "Hora": "07:53:27",
        "Filial": "BTF 03",
        "Motorista": "Btf3 - Jose Jackson Mendes Brito",
        "Veículo": "044120 - FAE6G52",
        "Hodômetro (km)": 2055730,
        "Duração (hh:mm:ss)": "00:00:10",
        "Velocidade (Km/h)": 47,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_SERRINHA BOTUCATU 2",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 08:02:42",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.93860+-48.36780"
    },
    {
        "Data": "20/10/2024",
        "Hora": "21:45:39",
        "Filial": "BTF 08",
        "Motorista": "Btf8 - Willian Carlos Pires",
        "Veículo": "044133 - SUO7F08",
        "Hodômetro (km)": 737665,
        "Duração (hh:mm:ss)": "00:00:14",
        "Velocidade (Km/h)": 87,
        "Limite (Km/h)": 80,
        "Cerca Embarcada": "-",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 21:52:57",
        "Usuário da Ação": "Pedro Henrique Leodoro Martins",
        "Local": "https://www.google.com/maps?q=-21.38450+-50.25270"
    },
    {
        "Data": "20/10/2024",
        "Hora": "16:52:18",
        "Filial": "BTF 08",
        "Motorista": "Btf8 - Anderson Donizete Moretto",
        "Veículo": "044147 - GJF7E01",
        "Hodômetro (km)": 848241,
        "Duração (hh:mm:ss)": "00:00:24",
        "Velocidade (Km/h)": 54,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_AREA URBANA TRES LAGOAS",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 17:22:11",
        "Usuário da Ação": "Pedro Henrique Leodoro Martins",
        "Local": "https://www.google.com/maps?q=-20.78860+-51.64060"
    },
    {
        "Data": "22/10/2024",
        "Hora": "11:09:33",
        "Filial": "BTF 08",
        "Motorista": "Motorista Ee2290626747",
        "Veículo": "044147 - GJF7E01",
        "Hodômetro (km)": 859816,
        "Duração (hh:mm:ss)": "00:00:15",
        "Velocidade (Km/h)": 85,
        "Limite (Km/h)": 80,
        "Cerca Embarcada": "-",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 12:41:16",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.30770+-49.05830"
    },
    {
        "Data": "21/10/2024",
        "Hora": "08:50:36",
        "Filial": "BTF 08",
        "Motorista": "Motorista Ee2290626747",
        "Veículo": "044152 - STN1I07",
        "Hodômetro (km)": 796770,
        "Duração (hh:mm:ss)": "00:00:53",
        "Velocidade (Km/h)": 80,
        "Limite (Km/h)": 70,
        "Cerca Embarcada": "BRC_PONTE RIO PARANA",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 11:58:01",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-20.79020+-51.62740"
    },
    {
        "Data": "19/10/2024",
        "Hora": "08:27:12",
        "Filial": "BTF 06",
        "Motorista": "Btf6 - Fabio De Souza Lima",
        "Veículo": "044156 - SUZ1F51",
        "Hodômetro (km)": 844325,
        "Duração (hh:mm:ss)": "00:00:10",
        "Velocidade (Km/h)": 46,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PREVISAO CHEGADA",
        "Ação": "Valido",
        "Data da Ação": "19/10/2024 09:30:27",
        "Usuário da Ação": "Pedro Henrique Leodoro Martins",
        "Local": "https://www.google.com/maps?q=-22.54170+-48.81120"
    },
    {
        "Data": "21/10/2024",
        "Hora": "07:08:01",
        "Filial": "BTF 07",
        "Motorista": "Btf7 - Lenaldo Marcelino Dos Santos",
        "Veículo": "044157 - STX5H35",
        "Hodômetro (km)": 787676,
        "Duração (hh:mm:ss)": "00:00:07",
        "Velocidade (Km/h)": 23,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_SAIDA DA RONDON ",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 07:40:38",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.56710+-48.82310"
    },
    {
        "Data": "19/10/2024",
        "Hora": "10:25:36",
        "Filial": "BTF 06",
        "Motorista": "Btf6 - Maicon Rogerio Ramos",
        "Veículo": "044159 - SVB7J03",
        "Hodômetro (km)": 673476,
        "Duração (hh:mm:ss)": "00:00:09",
        "Velocidade (Km/h)": 50,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "19/10/2024 10:44:17",
        "Usuário da Ação": "Pedro Henrique Leodoro Martins",
        "Local": "https://www.google.com/maps?q=-22.95110+-48.50580"
    },
    {
        "Data": "19/10/2024",
        "Hora": "12:47:17",
        "Filial": "BTF 06",
        "Motorista": "Btf6 - Maicon Rogerio Ramos",
        "Veículo": "044159 - SVB7J03",
        "Hodômetro (km)": 674412,
        "Duração (hh:mm:ss)": "00:00:24",
        "Velocidade (Km/h)": 86,
        "Limite (Km/h)": 80,
        "Cerca Embarcada": "-",
        "Ação": "Valido",
        "Data da Ação": "19/10/2024 13:14:20",
        "Usuário da Ação": "Pedro Henrique Leodoro Martins",
        "Local": "https://www.google.com/maps?q=-22.65770+-48.71140"
    },
    {
        "Data": "22/10/2024",
        "Hora": "06:56:03",
        "Filial": "BTF 06",
        "Motorista": "Btf6 - Maicon Rogerio Ramos",
        "Veículo": "044159 - SVB7J03",
        "Hodômetro (km)": 683968,
        "Duração (hh:mm:ss)": "00:00:07",
        "Velocidade (Km/h)": 23,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_ROTATORIA LWART",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 07:28:02",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.56110+-48.81680"
    },
    {
        "Data": "20/10/2024",
        "Hora": "03:56:06",
        "Filial": "BTF 08",
        "Motorista": "Btf8 - Fabio De Souza Da Silva",
        "Veículo": "044164 - SSV7B42",
        "Hodômetro (km)": 720302,
        "Duração (hh:mm:ss)": "00:00:11",
        "Velocidade (Km/h)": 45,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PREVISAO CHEGADA",
        "Ação": "Válido",
        "Data da Ação": "20/10/2024 04:54:05",
        "Usuário da Ação": "Ianca Luata Da Silva",
        "Local": "https://www.google.com/maps?q=-22.54160+-48.81120"
    },
    {
        "Data": "22/10/2024",
        "Hora": "05:19:40",
        "Filial": "BTF 08",
        "Motorista": "Btf8 - Leandro Ricardo De Freitas",
        "Veículo": "044166 - DYD4C11",
        "Hodômetro (km)": 751614,
        "Duração (hh:mm:ss)": "00:00:23",
        "Velocidade (Km/h)": 93,
        "Limite (Km/h)": 80,
        "Cerca Embarcada": "-",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 07:37:40",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-21.55550+-52.52760"
    },
    {
        "Data": "20/10/2024",
        "Hora": "06:10:53",
        "Filial": "BTF 06",
        "Motorista": "Btf6 - Andre Luiz Alves Dos Santos",
        "Veículo": "044180 - STI7F31",
        "Hodômetro (km)": 795061,
        "Duração (hh:mm:ss)": "00:00:16",
        "Velocidade (Km/h)": 57,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PREVISAO CHEGADA",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 07:42:05",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.54110+-48.81070"
    },
    {
        "Data": "20/10/2024",
        "Hora": "14:48:17",
        "Filial": "BTF 06",
        "Motorista": "Btf6 - Luiz Paulo Gimenes",
        "Veículo": "044193 - SWP1C87",
        "Hodômetro (km)": 858346,
        "Duração (hh:mm:ss)": "00:00:14",
        "Velocidade (Km/h)": 40,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 14:57:52",
        "Usuário da Ação": "Pedro Henrique Leodoro Martins",
        "Local": "https://www.google.com/maps?q=-22.98660+-48.55250"
    },
    {
        "Data": "20/10/2024",
        "Hora": "15:02:31",
        "Filial": "BTF 06",
        "Motorista": "Btf6 - Luiz Paulo Gimenes",
        "Veículo": "044193 - SWP1C87",
        "Hodômetro (km)": 858422,
        "Duração (hh:mm:ss)": "00:00:09",
        "Velocidade (Km/h)": 38,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA_2",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 15:20:12",
        "Usuário da Ação": "Pedro Henrique Leodoro Martins",
        "Local": "https://www.google.com/maps?q=-22.94740+-48.49640"
    },
    {
        "Data": "22/10/2024",
        "Hora": "06:13:29",
        "Filial": "BTF 06",
        "Motorista": "Btf6 - Wanderson Rafael Americo",
        "Veículo": "044193 - SWP1C87",
        "Hodômetro (km)": 864933,
        "Duração (hh:mm:ss)": "00:00:11",
        "Velocidade (Km/h)": 23,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_ROTATORIA SAIDA RONDON ",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 06:43:52",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.56650+-48.82260"
    },
    {
        "Data": "22/10/2024",
        "Hora": "10:41:26",
        "Filial": "BTF 06",
        "Motorista": "Btf6 - Wanderson Rafael Americo",
        "Veículo": "044193 - SWP1C87",
        "Hodômetro (km)": 866036,
        "Duração (hh:mm:ss)": "00:00:08",
        "Velocidade (Km/h)": 49,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 11:53:51",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.95110+-48.50590"
    },
    {
        "Data": "22/10/2024",
        "Hora": "13:28:47",
        "Filial": "BTF 06",
        "Motorista": "Btf6 - Wanderson Rafael Americo",
        "Veículo": "044193 - SWP1C87",
        "Hodômetro (km)": 866774,
        "Duração (hh:mm:ss)": "00:00:16",
        "Velocidade (Km/h)": 47,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PREVISAO CHEGADA",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 13:37:33",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.54100+-48.81070"
    },
    {
        "Data": "19/10/2024",
        "Hora": "13:57:09",
        "Filial": "Plácidos",
        "Motorista": "Jose Aparecido Gil Rodrigues",
        "Veículo": "0P2666 - FSX4B66",
        "Hodômetro (km)": 4489661,
        "Duração (hh:mm:ss)": "00:00:10",
        "Velocidade (Km/h)": 54,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "19/10/2024 15:12:22",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-22.98630+-48.55240"
    },
    {
        "Data": "22/10/2024",
        "Hora": "06:39:37",
        "Filial": "Expresso Olssen",
        "Motorista": "Michael Pereira Nascimento",
        "Veículo": "ELT0B92 - ELT0B92",
        "Hodômetro (km)": 1412346,
        "Duração (hh:mm:ss)": "00:00:10",
        "Velocidade (Km/h)": 52,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_BR153 CURVA",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 06:45:11",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-23.23820+-50.03920"
    },
    {
        "Data": "22/10/2024",
        "Hora": "07:26:37",
        "Filial": "Expresso Olssen",
        "Motorista": "Michael Pereira Nascimento",
        "Veículo": "ELT0B92 - ELT0B92",
        "Hodômetro (km)": 1412860,
        "Duração (hh:mm:ss)": "00:00:14",
        "Velocidade (Km/h)": 54,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PR218-7",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 07:49:44",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-23.44420+-50.23310"
    },
    {
        "Data": "22/10/2024",
        "Hora": "07:27:37",
        "Filial": "Expresso Olssen",
        "Motorista": "Michael Pereira Nascimento",
        "Veículo": "ELT0B92 - ELT0B92",
        "Hodômetro (km)": 1412870,
        "Duração (hh:mm:ss)": "00:00:11",
        "Velocidade (Km/h)": 49,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PR218-6",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 07:38:22",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-23.44850+-50.24170"
    },
    {
        "Data": "22/10/2024",
        "Hora": "07:30:14",
        "Filial": "Expresso Olssen",
        "Motorista": "Michael Pereira Nascimento",
        "Veículo": "ELT0B92 - ELT0B92",
        "Hodômetro (km)": 1412894,
        "Duração (hh:mm:ss)": "00:00:07",
        "Velocidade (Km/h)": 49,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PR218-4",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 07:49:06",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-23.44580+-50.26410"
    },
    {
        "Data": "22/10/2024",
        "Hora": "12:05:57",
        "Filial": "Expresso Olssen",
        "Motorista": "Michael Pereira Nascimento",
        "Veículo": "ELT0B92 - ELT0B92",
        "Hodômetro (km)": 1413347,
        "Duração (hh:mm:ss)": "00:00:13",
        "Velocidade (Km/h)": 57,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PR218-7",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 12:42:00",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-23.44420+-50.23280"
    },
    {
        "Data": "21/10/2024",
        "Hora": "09:52:34",
        "Filial": "Expresso Nepomuceno - Bracell",
        "Motorista": "Marcelo Salgado Maia",
        "Veículo": "EXU8H86 - EXU8H86",
        "Hodômetro (km)": 2944760,
        "Duração (hh:mm:ss)": "00:01:22",
        "Velocidade (Km/h)": 62,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_SERRA",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 12:06:41",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-19.16470+-46.67300"
    },
    {
        "Data": "21/10/2024",
        "Hora": "09:54:08",
        "Filial": "Expresso Nepomuceno - Bracell",
        "Motorista": "Marcelo Salgado Maia",
        "Veículo": "EXU8H86 - EXU8H86",
        "Hodômetro (km)": 2944773,
        "Duração (hh:mm:ss)": "00:00:52",
        "Velocidade (Km/h)": 53,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_SERRA",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 12:05:21",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-19.16060+-46.66790"
    },
    {
        "Data": "19/10/2024",
        "Hora": "20:14:24",
        "Filial": "Garbuio SP",
        "Motorista": "Claudemir Pereira",
        "Veículo": "FJG0E62 - FJG0E62",
        "Hodômetro (km)": 2723460,
        "Duração (hh:mm:ss)": "00:00:15",
        "Velocidade (Km/h)": 46,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PREVISAO CHEGADA",
        "Ação": "Valido",
        "Data da Ação": "19/10/2024 20:30:47",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-22.54110+-48.81070"
    },
    {
        "Data": "22/10/2024",
        "Hora": "06:52:28",
        "Filial": "Lourenço",
        "Motorista": "Motorista Ee2138232731",
        "Veículo": "FUR1J38 - FUR1J38",
        "Hodômetro (km)": 4488557,
        "Duração (hh:mm:ss)": "00:00:15",
        "Velocidade (Km/h)": 35,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA_2",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 07:51:15",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.94730+-48.49690"
    },
    {
        "Data": "22/10/2024",
        "Hora": "04:43:23",
        "Filial": "CargoPolo MS",
        "Motorista": "Motorista Ee0492571399",
        "Veículo": "GAW3J94 - GAW3J94",
        "Hodômetro (km)": 5813258,
        "Duração (hh:mm:ss)": "00:00:10",
        "Velocidade (Km/h)": 52,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PR218-6",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 04:54:34",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-23.44840+-50.24180"
    },
    {
        "Data": "19/10/2024",
        "Hora": "03:04:03",
        "Filial": "CargoPolo MS",
        "Motorista": "Ricardo Pedroti Florencio",
        "Veículo": "GDW4J22 - GDW4J22",
        "Hodômetro (km)": 20933924,
        "Duração (hh:mm:ss)": "00:00:15",
        "Velocidade (Km/h)": 29,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_ROTATORIA_TRES LAGOAS",
        "Ação": "Válido",
        "Data da Ação": "19/10/2024 03:43:57",
        "Usuário da Ação": "Ianca Luata Da Silva",
        "Local": "https://www.google.com/maps?q=-20.77900+-51.59410"
    },
    {
        "Data": "19/10/2024",
        "Hora": "05:48:07",
        "Filial": "CargoPolo MS",
        "Motorista": "Marcio Jose Cipriano",
        "Veículo": "GHB1B84 - GHB1B84",
        "Hodômetro (km)": 5332310,
        "Duração (hh:mm:ss)": "00:00:21",
        "Velocidade (Km/h)": 42,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_ROTATORIA_TRES LAGOAS",
        "Ação": "Valido",
        "Data da Ação": "19/10/2024 06:25:39",
        "Usuário da Ação": "Pedro Henrique Leodoro Martins",
        "Local": "https://www.google.com/maps?q=-20.77900+-51.59340"
    },
    {
        "Data": "21/10/2024",
        "Hora": "23:12:52",
        "Filial": "CargoPolo MS",
        "Motorista": "Flavio Da Silva",
        "Veículo": "GHS1H44 - GHS1H44",
        "Hodômetro (km)": 5382457,
        "Duração (hh:mm:ss)": "00:00:11",
        "Velocidade (Km/h)": 63,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_BR153 CURVA",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 23:29:38",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-23.23850+-50.03930"
    },
    {
        "Data": "21/10/2024",
        "Hora": "23:16:11",
        "Filial": "CargoPolo MS",
        "Motorista": "Flavio Da Silva",
        "Veículo": "GHS1H44 - GHS1H44",
        "Hodômetro (km)": 5382494,
        "Duração (hh:mm:ss)": "00:00:09",
        "Velocidade (Km/h)": 69,
        "Limite (Km/h)": 60,
        "Cerca Embarcada": "BRC_BR153 CURVA2",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 23:29:12",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-23.26290+-50.05960"
    },
    {
        "Data": "19/10/2024",
        "Hora": "15:25:19",
        "Filial": "Plácidos",
        "Motorista": "Joao Carlos Gottardi",
        "Veículo": "OO2067 - FQS3B93",
        "Hodômetro (km)": 3526546,
        "Duração (hh:mm:ss)": "00:00:11",
        "Velocidade (Km/h)": 34,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_CURVA PERIGOSA",
        "Ação": "Valido",
        "Data da Ação": "19/10/2024 17:30:31",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-22.98640+-48.55230"
    },
    {
        "Data": "20/10/2024",
        "Hora": "14:10:33",
        "Filial": "Expresso Nepomuceno - Bracell",
        "Motorista": "Jose Valdir Mendes Freire",
        "Veículo": "OPP4E71 - OPP4E71",
        "Hodômetro (km)": 899313,
        "Duração (hh:mm:ss)": "00:00:11",
        "Velocidade (Km/h)": 85,
        "Limite (Km/h)": 80,
        "Cerca Embarcada": "-",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 14:19:14",
        "Usuário da Ação": "Pedro Henrique Leodoro Martins",
        "Local": "https://www.google.com/maps?q=-20.99670+-47.85230"
    },
    {
        "Data": "21/10/2024",
        "Hora": "11:56:53",
        "Filial": "Expresso Nepomuceno - Bracell",
        "Motorista": "Josimar Aparecido Da Silva",
        "Veículo": "OPP5H70 - OPP5H70",
        "Hodômetro (km)": 974263,
        "Duração (hh:mm:ss)": "00:00:08",
        "Velocidade (Km/h)": 55,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_ALCA ROD JOAO RIBEIRO DE BARROS ",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 13:23:07",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.33200+-48.75870"
    },
    {
        "Data": "20/10/2024",
        "Hora": "10:05:22",
        "Filial": "Expresso Nepomuceno - Bracell",
        "Motorista": "Anselmo Rodrigo Avante",
        "Veículo": "OQA0G80 - OQA0G80",
        "Hodômetro (km)": 925198,
        "Duração (hh:mm:ss)": "00:00:08",
        "Velocidade (Km/h)": 23,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_ROTATORIA LINHA2",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 12:07:04",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.55000+-48.81510"
    },
    {
        "Data": "21/10/2024",
        "Hora": "04:46:25",
        "Filial": "Transpes - Bracell MS",
        "Motorista": "Tiago Augusto Valerio Bueno",
        "Veículo": "RTJ7G97 - RTJ7G97",
        "Hodômetro (km)": 2676203,
        "Duração (hh:mm:ss)": "00:00:31",
        "Velocidade (Km/h)": 85,
        "Limite (Km/h)": 80,
        "Cerca Embarcada": "-",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 05:03:19",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-22.42340+-49.12300"
    },
    {
        "Data": "22/10/2024",
        "Hora": "10:35:29",
        "Filial": "Transpes - Bracell SP",
        "Motorista": "Valmir Constancio",
        "Veículo": "RUL7G28 - RUL7G28",
        "Hodômetro (km)": 2618944,
        "Duração (hh:mm:ss)": "00:00:20",
        "Velocidade (Km/h)": 47,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PREVISAO CHEGADA",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 11:54:18",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.54120+-48.81060"
    },
    {
        "Data": "22/10/2024",
        "Hora": "12:05:13",
        "Filial": "Transpes - Bracell SP",
        "Motorista": "Valmir Constancio",
        "Veículo": "RUL7G28 - RUL7G28",
        "Hodômetro (km)": 2618985,
        "Duração (hh:mm:ss)": "00:00:17",
        "Velocidade (Km/h)": 46,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PREVISAO CHEGADA",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 12:42:30",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.54100+-48.81080"
    },
    {
        "Data": "22/10/2024",
        "Hora": "08:51:26",
        "Filial": "Transpes - Bracell MS",
        "Motorista": "Tiago Augusto Valerio Bueno",
        "Veículo": "RUR7J11 - RUR7J11",
        "Hodômetro (km)": 2414532,
        "Duração (hh:mm:ss)": "00:00:10",
        "Velocidade (Km/h)": 60,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PR218-6",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 09:21:33",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-23.44840+-50.24080"
    },
    {
        "Data": "22/10/2024",
        "Hora": "08:52:28",
        "Filial": "Transpes - Bracell MS",
        "Motorista": "Tiago Augusto Valerio Bueno",
        "Veículo": "RUR7J11 - RUR7J11",
        "Hodômetro (km)": 2414541,
        "Duração (hh:mm:ss)": "00:00:14",
        "Velocidade (Km/h)": 58,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PR218-7",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 09:21:01",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-23.44420+-50.23290"
    },
    {
        "Data": "22/10/2024",
        "Hora": "11:30:00",
        "Filial": "Transpes - Bracell MS",
        "Motorista": "Tiago Augusto Valerio Bueno",
        "Veículo": "RUR7J11 - RUR7J11",
        "Hodômetro (km)": 2416027,
        "Duração (hh:mm:ss)": "00:00:14",
        "Velocidade (Km/h)": 89,
        "Limite (Km/h)": 80,
        "Cerca Embarcada": "-",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 12:40:18",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.74570+-49.47510"
    },
    {
        "Data": "22/10/2024",
        "Hora": "12:04:31",
        "Filial": "Transpes - Bracell MS",
        "Motorista": "Tiago Augusto Valerio Bueno",
        "Veículo": "RUR7J11 - RUR7J11",
        "Hodômetro (km)": 2416418,
        "Duração (hh:mm:ss)": "00:00:18",
        "Velocidade (Km/h)": 85,
        "Limite (Km/h)": 80,
        "Cerca Embarcada": "-",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 12:40:24",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.49360+-49.25740"
    },
    {
        "Data": "22/10/2024",
        "Hora": "13:00:01",
        "Filial": "Transpes - Bracell MS",
        "Motorista": "Tiago Augusto Valerio Bueno",
        "Veículo": "RUR7J11 - RUR7J11",
        "Hodômetro (km)": 2417030,
        "Duração (hh:mm:ss)": "00:00:10",
        "Velocidade (Km/h)": 23,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_SAIDA DA RONDON ",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 13:21:19",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.56750+-48.82320"
    },
    {
        "Data": "22/10/2024",
        "Hora": "13:05:53",
        "Filial": "Transpes - Bracell MS",
        "Motorista": "Tiago Augusto Valerio Bueno",
        "Veículo": "RUR7J11 - RUR7J11",
        "Hodômetro (km)": 2417068,
        "Duração (hh:mm:ss)": "00:00:17",
        "Velocidade (Km/h)": 48,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PREVISAO CHEGADA",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 13:22:08",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.54100+-48.81050"
    },
    {
        "Data": "21/10/2024",
        "Hora": "21:47:22",
        "Filial": "VDA",
        "Motorista": "Carlos Eduardo Cardoso",
        "Veículo": "RWO6E61 - RWO6E61",
        "Hodômetro (km)": 3704412,
        "Duração (hh:mm:ss)": "00:00:11",
        "Velocidade (Km/h)": 53,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PR218-7",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 22:44:12",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-23.44440+-50.23350"
    },
    {
        "Data": "22/10/2024",
        "Hora": "08:16:41",
        "Filial": "VDA",
        "Motorista": "Adolfo Nalin",
        "Veículo": "RWS0C39 - RWS0C39",
        "Hodômetro (km)": 3399259,
        "Duração (hh:mm:ss)": "00:00:09",
        "Velocidade (Km/h)": 68,
        "Limite (Km/h)": 60,
        "Cerca Embarcada": "BRC_BR153 CURVA2",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 08:37:07",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-23.26280+-50.05960"
    },
    {
        "Data": "22/10/2024",
        "Hora": "09:01:14",
        "Filial": "VDA",
        "Motorista": "Adolfo Nalin",
        "Veículo": "RWS0C39 - RWS0C39",
        "Hodômetro (km)": 3399733,
        "Duração (hh:mm:ss)": "00:00:09",
        "Velocidade (Km/h)": 56,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PR218-7",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 09:20:18",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-23.44440+-50.23370"
    },
    {
        "Data": "22/10/2024",
        "Hora": "06:12:11",
        "Filial": "Expresso Olssen",
        "Motorista": "Paulo Celso Dos Santos",
        "Veículo": "RYJ4F25 - RYJ4F25",
        "Hodômetro (km)": 1879422,
        "Duração (hh:mm:ss)": "00:00:12",
        "Velocidade (Km/h)": 68,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PR218-7",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 06:46:15",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-23.44430+-50.23340"
    },
    {
        "Data": "22/10/2024",
        "Hora": "08:47:30",
        "Filial": "Expresso Olssen",
        "Motorista": "Paulo Celso Dos Santos",
        "Veículo": "RYJ4F25 - RYJ4F25",
        "Hodômetro (km)": 1879867,
        "Duração (hh:mm:ss)": "00:00:10",
        "Velocidade (Km/h)": 63,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PR218-6",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 09:23:10",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-23.44840+-50.24060"
    },
    {
        "Data": "22/10/2024",
        "Hora": "08:48:30",
        "Filial": "Expresso Olssen",
        "Motorista": "Paulo Celso Dos Santos",
        "Veículo": "RYJ4F25 - RYJ4F25",
        "Hodômetro (km)": 1879876,
        "Duração (hh:mm:ss)": "00:00:14",
        "Velocidade (Km/h)": 54,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PR218-7",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 09:22:06",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-23.44420+-50.23290"
    },
    {
        "Data": "22/10/2024",
        "Hora": "09:01:21",
        "Filial": "Expresso Olssen",
        "Motorista": "Paulo Celso Dos Santos",
        "Veículo": "RYJ4F25 - RYJ4F25",
        "Hodômetro (km)": 1880001,
        "Duração (hh:mm:ss)": "00:00:11",
        "Velocidade (Km/h)": 41,
        "Limite (Km/h)": 30,
        "Cerca Embarcada": "BRC_PR218-3",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 09:24:55",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-23.49600+-50.13700"
    },
    {
        "Data": "20/10/2024",
        "Hora": "06:18:12",
        "Filial": "Expresso Olssen",
        "Motorista": "Motorista Ee1601279239",
        "Veículo": "RYR3E46 - RYR3E46",
        "Hodômetro (km)": 1644709,
        "Duração (hh:mm:ss)": "00:00:09",
        "Velocidade (Km/h)": 85,
        "Limite (Km/h)": 80,
        "Cerca Embarcada": "-",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 07:06:05",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.43180+-49.13220"
    },
    {
        "Data": "21/10/2024",
        "Hora": "07:23:06",
        "Filial": "VDA",
        "Motorista": "Marcio Paulo Rodrigues",
        "Veículo": "SAL3A92 - SAL3A92",
        "Hodômetro (km)": 2872403,
        "Duração (hh:mm:ss)": "00:00:15",
        "Velocidade (Km/h)": 86,
        "Limite (Km/h)": 80,
        "Cerca Embarcada": "-",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 07:39:24",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.50570+-48.92210"
    },
    {
        "Data": "22/10/2024",
        "Hora": "07:39:35",
        "Filial": "VDA",
        "Motorista": "Marcio Paulo Rodrigues",
        "Veículo": "SAL3A92 - SAL3A92",
        "Hodômetro (km)": 2880379,
        "Duração (hh:mm:ss)": "00:00:11",
        "Velocidade (Km/h)": 73,
        "Limite (Km/h)": 60,
        "Cerca Embarcada": "BRC_BR153 CURVA2",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 07:48:29",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-23.26260+-50.05930"
    },
    {
        "Data": "22/10/2024",
        "Hora": "08:22:42",
        "Filial": "VDA",
        "Motorista": "Marcio Paulo Rodrigues",
        "Veículo": "SAL3A92 - SAL3A92",
        "Hodômetro (km)": 2880860,
        "Duração (hh:mm:ss)": "00:00:17",
        "Velocidade (Km/h)": 47,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PR218-7",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 08:37:31",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-23.44420+-50.23300"
    },
    {
        "Data": "20/10/2024",
        "Hora": "11:10:07",
        "Filial": "VDA",
        "Motorista": "Marcio Antonio Matheus",
        "Veículo": "SAL3A93 - SAL3A93",
        "Hodômetro (km)": 2640898,
        "Duração (hh:mm:ss)": "00:00:13",
        "Velocidade (Km/h)": 87,
        "Limite (Km/h)": 80,
        "Cerca Embarcada": "-",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 12:04:59",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.78510+-49.51280"
    },
    {
        "Data": "21/10/2024",
        "Hora": "21:20:44",
        "Filial": "Transpes - Bracell SP",
        "Motorista": "Dacio Pereira Da Silva",
        "Veículo": "SHE3J02 - SHE3J02",
        "Hodômetro (km)": 1348112,
        "Duração (hh:mm:ss)": "00:00:08",
        "Velocidade (Km/h)": 85,
        "Limite (Km/h)": 80,
        "Cerca Embarcada": "-",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 21:25:38",
        "Usuário da Ação": "Pedro Henrique Leodoro Martins",
        "Local": "https://www.google.com/maps?q=-23.44730+-50.24610"
    },
    {
        "Data": "21/10/2024",
        "Hora": "03:14:47",
        "Filial": "Transpes - Bracell MS",
        "Motorista": "Antonio Manoel Da Silva",
        "Veículo": "SHE5C82 - SHE5C82",
        "Hodômetro (km)": 1332019,
        "Duração (hh:mm:ss)": "00:00:17",
        "Velocidade (Km/h)": 49,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PREVISAO CHEGADA",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 03:40:02",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-22.54100+-48.81060"
    },
    {
        "Data": "21/10/2024",
        "Hora": "10:43:18",
        "Filial": "Transpes - Bracell MS",
        "Motorista": "Braz Costa",
        "Veículo": "SHE5C82 - SHE5C82",
        "Hodômetro (km)": 1334744,
        "Duração (hh:mm:ss)": "00:00:08",
        "Velocidade (Km/h)": 25,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_COMUNIDADE_NOSSA_SENHORA",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 12:03:46",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-23.45900+-50.36510"
    },
    {
        "Data": "21/10/2024",
        "Hora": "23:22:09",
        "Filial": "Garbuio SP",
        "Motorista": "Diego Dos Santos Ferreira De Souza",
        "Veículo": "SIY0C29 - SIY0C29",
        "Hodômetro (km)": 1262998,
        "Duração (hh:mm:ss)": "00:00:10",
        "Velocidade (Km/h)": 91,
        "Limite (Km/h)": 80,
        "Cerca Embarcada": "-",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 23:28:55",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-20.97560+-47.86250"
    },
    {
        "Data": "20/10/2024",
        "Hora": "09:41:33",
        "Filial": "Garbuio SP",
        "Motorista": "Walter Nunes Fischer",
        "Veículo": "SJE7G40 - SJE7G40",
        "Hodômetro (km)": 1160066,
        "Duração (hh:mm:ss)": "00:00:10",
        "Velocidade (Km/h)": 49,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_ALCA ROD JOAO RIBEIRO DE BARROS ",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 12:06:20",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.33200+-48.75880"
    },
    {
        "Data": "19/10/2024",
        "Hora": "22:35:17",
        "Filial": "Expresso Nepomuceno - Bracell",
        "Motorista": "Antonio Marcos Paulino",
        "Veículo": "SSV0A56 - SSV0A56",
        "Hodômetro (km)": 1239681,
        "Duração (hh:mm:ss)": "00:00:19",
        "Velocidade (Km/h)": 49,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PREVISAO CHEGADA",
        "Ação": "Válido",
        "Data da Ação": "19/10/2024 23:28:01",
        "Usuário da Ação": "Ianca Luata Da Silva",
        "Local": "https://www.google.com/maps?q=-22.54120+-48.81060"
    },
    {
        "Data": "19/10/2024",
        "Hora": "23:05:17",
        "Filial": "Expresso Nepomuceno - Bracell",
        "Motorista": "Antonio Marcos Paulino",
        "Veículo": "SSV0A56 - SSV0A56",
        "Hodômetro (km)": 1239964,
        "Duração (hh:mm:ss)": "00:00:10",
        "Velocidade (Km/h)": 48,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_ALCA ROD JOAO RIBEIRO DE BARROS ",
        "Ação": "Válido",
        "Data da Ação": "19/10/2024 23:27:21",
        "Usuário da Ação": "Ianca Luata Da Silva",
        "Local": "https://www.google.com/maps?q=-22.33190+-48.75880"
    },
    {
        "Data": "19/10/2024",
        "Hora": "13:30:48",
        "Filial": "Expresso Nepomuceno - Bracell",
        "Motorista": "Carlos Eduardo Viana Da Silva",
        "Veículo": "SSV9D40 - SSV9D40",
        "Hodômetro (km)": 1140442,
        "Duração (hh:mm:ss)": "00:00:20",
        "Velocidade (Km/h)": 45,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_SERRA",
        "Ação": "Valido",
        "Data da Ação": "19/10/2024 15:11:22",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-19.15960+-46.67090"
    },
    {
        "Data": "19/10/2024",
        "Hora": "13:31:51",
        "Filial": "Expresso Nepomuceno - Bracell",
        "Motorista": "Carlos Eduardo Viana Da Silva",
        "Veículo": "SSV9D40 - SSV9D40",
        "Hodômetro (km)": 1140449,
        "Duração (hh:mm:ss)": "00:00:27",
        "Velocidade (Km/h)": 55,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_SERRA",
        "Ação": "Valido",
        "Data da Ação": "19/10/2024 15:11:35",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-19.16510+-46.67160"
    },
    {
        "Data": "22/10/2024",
        "Hora": "00:15:49",
        "Filial": "Expresso Nepomuceno - Bracell",
        "Motorista": "Isaias De Souza Daniel",
        "Veículo": "SSY0C97 - SSY0C97",
        "Hodômetro (km)": 1236183,
        "Duração (hh:mm:ss)": "00:00:20",
        "Velocidade (Km/h)": 34,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_ROTATORIA LWART",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 00:29:07",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-22.56110+-48.81650"
    },
    {
        "Data": "20/10/2024",
        "Hora": "06:05:45",
        "Filial": "Expresso Olssen",
        "Motorista": "Adenilson Rosa Da Silva",
        "Veículo": "SUX9C68 - SUX9C68",
        "Hodômetro (km)": 1680217,
        "Duração (hh:mm:ss)": "00:00:11",
        "Velocidade (Km/h)": 46,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_PREVISAO CHEGADA",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 07:43:33",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.54040+-48.81030"
    },
    {
        "Data": "21/10/2024",
        "Hora": "12:18:46",
        "Filial": "Expresso Olssen",
        "Motorista": "Adenilson Rosa Da Silva",
        "Veículo": "SUX9C68 - SUX9C68",
        "Hodômetro (km)": 1691612,
        "Duração (hh:mm:ss)": "00:00:10",
        "Velocidade (Km/h)": 26,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_SAIDA DA RONDON ",
        "Ação": "Valido",
        "Data da Ação": "21/10/2024 13:22:51",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.56730+-48.82340"
    },
    {
        "Data": "19/10/2024",
        "Hora": "16:11:02",
        "Filial": "Expresso Nepomuceno - Bracell",
        "Motorista": "Carlos Eduardo Viana Da Silva",
        "Veículo": "SVB9J08 - SVB9J08",
        "Hodômetro (km)": 1221052,
        "Duração (hh:mm:ss)": "00:00:10",
        "Velocidade (Km/h)": 45,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_SERRA",
        "Ação": "Valido",
        "Data da Ação": "19/10/2024 17:29:40",
        "Usuário da Ação": "Marcelo Chagas Silva",
        "Local": "https://www.google.com/maps?q=-19.15900+-46.66320"
    },
    {
        "Data": "20/10/2024",
        "Hora": "08:14:17",
        "Filial": "Expresso Olssen",
        "Motorista": "Eberson Rodrigo Ferreira",
        "Veículo": "SWS6G59 - SWS6G59",
        "Hodômetro (km)": 1435845,
        "Duração (hh:mm:ss)": "00:00:08",
        "Velocidade (Km/h)": 24,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_COMUNIDADE_NOSSA_SENHORA",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 09:37:23",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-23.45900+-50.36520"
    },
    {
        "Data": "22/10/2024",
        "Hora": "06:47:12",
        "Filial": "Garbuio SP",
        "Motorista": "Ronaldo Carlos",
        "Veículo": "SYD4C58 - SYD4C58",
        "Hodômetro (km)": 667792,
        "Duração (hh:mm:ss)": "00:00:08",
        "Velocidade (Km/h)": 23,
        "Limite (Km/h)": 20,
        "Cerca Embarcada": "BRC_SAIDA DA RONDON ",
        "Ação": "Valido",
        "Data da Ação": "22/10/2024 07:29:05",
        "Usuário da Ação": "Leandro Santos Da Costa",
        "Local": "https://www.google.com/maps?q=-22.56740+-48.82340"
    },
    {
        "Data": "20/10/2024",
        "Hora": "08:51:59",
        "Filial": "Garbuio SP",
        "Motorista": "Valmir Nereu Gomes",
        "Veículo": "SYD4C62 - SYD4C62",
        "Hodômetro (km)": 904654,
        "Duração (hh:mm:ss)": "00:00:09",
        "Velocidade (Km/h)": 46,
        "Limite (Km/h)": 40,
        "Cerca Embarcada": "BRC_ALCA ROD JOAO RIBEIRO DE BARROS ",
        "Ação": "Valido",
        "Data da Ação": "20/10/2024 09:36:48",
        "Usuário da Ação": "Matheus Vinicius Morgado",
        "Local": "https://www.google.com/maps?q=-22.33180+-48.75870"
    }
        # Adicione mais registros se necessário...
    
# Função para formatar a tabela de infrações
def formatar_tabela(tabela_velocidade):
    tabela_infracao = ""
    for registro in tabela_velocidade:
        tabela_infracao += (
            f"Data: {registro['Data']}\n"
            f"Hora: {registro['Hora']}\n"
            f"Filial: {registro['Filial']}\n"
            f"Motorista: {registro['Motorista']}\n"
            f"Veículo: {registro['Veículo']}\n"
            f"Hodômetro (km): {registro['Hodômetro (km)']}\n"
            f"Duração: {registro['Duração (hh:mm:ss)']}\n"
            f"Velocidade: {registro['Velocidade (Km/h)']} Km/h\n"
            f"Limite: {registro['Limite (Km/h)']} Km/h\n"
            f"Cerca Embarcada: {registro['Cerca Embarcada']}\n"
            f"Ação: {registro['Ação']}\n"
            f"Data da Ação: {registro['Data da Ação']}\n"
            f"Usuário da Ação: {registro['Usuário da Ação']}\n"
            f"Local: {registro['Local']}\n\n"
        )
    
    return tabela_infracao

# Função para fazer a requisição à API do Gemini
def consultar_gemini_api(pergunta, api_key, tabela_velocidade):
    url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'
    
    headers = {
        'Content-Type': 'application/json',
    }

    # Contexto que será passado em todas as interações
    contexto = (
        "Foram 119 ocorrências do dia 19/10/2024 a 22/10/2024. "
        "A variável tabela_velocidade contém o link com as coordenadas exatas para apontarmos o local exato da ocorrência."
        "A tabela disponibilizada acima é sobre as ocorrências de velocidade. "
        "A Logística Florestal da Bracell inovando e utilizando IA para ajudar nas análises de infrações de velocidade!! "
    )
    
    # Formatar a tabela e incluir no contexto
    tabela_infracao = formatar_tabela(tabela_velocidade)
    
    # Combina o contexto, a tabela e a pergunta do usuário
    pergunta_com_contexto = f"{contexto}\n\nTabela de Dados:\n{tabela_infracao}\n\nPergunta: {pergunta}"
    
    # Corpo da requisição com a pergunta, contexto e a tabela
    data = {
        "contents": [
            {
                "parts": [
                    {"text": pergunta_com_contexto}
                ]
            }
        ]
    }
    
    params = {
        'key': api_key  # Chave de autenticação da API
    }
    
    # Fazendo a requisição POST
    response = requests.post(url, headers=headers, json=data, params=params)
    
    if response.status_code == 200:
        return response.json()  # Retorna a resposta em JSON
    else:
        return {"erro": "Falha ao se comunicar com a API.", "status_code": response.status_code}

# Função para extrair e formatar a resposta da API de forma amigável
def formatar_resposta(resposta):
    try:
        # Extraindo o texto da resposta gerada
        texto_resposta = resposta["candidates"][0]["content"]["parts"][0]["text"]
        return texto_resposta
    except (KeyError, IndexError):
        return "Não foi possível processar a resposta da API."

# Função principal para interface do Streamlit
def main():
    st.title("Painel de Infrações de Velocidade - Bracell")
    
    # Exibe uma saudação dinâmica com base na hora do dia
    saudacao = gerar_saudacao()
    st.write(f"{saudacao}! Este painel foi desenvolvido para analisar infrações de velocidade usando IA.")

    # Entrada de texto para a pergunta do usuário
    pergunta = st.text_input("Digite sua pergunta sobre as infrações de velocidade:")

    # Botão para consultar a API
    if st.button("Consultar Inteligência Artificial"):
        if pergunta and api_key:
            resposta = consultar_gemini_api(pergunta, api_key, tabela_velocidade)
            
            # Exibindo a resposta da API
            if 'erro' in resposta:
                st.error(f"Erro: {resposta['erro']} (Status code: {resposta['status_code']})")
            else:
                resposta_formatada = formatar_resposta(resposta)
                st.write("Resposta da IA:")
                st.write(resposta_formatada)
        else:
            st.warning("Por favor, insira a pergunta e a API Key.")

if __name__ == '__main__':
    main()
# Função para fazer a requisição à API do Gemini
def consultar_gemini_api(pergunta, api_key, tabela_velocidade):
    url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'
    
    headers = {
        'Content-Type': 'application/json',
    }

    # Contexto que será passado em todas as interações
    contexto = (
        "Foram 119 ocorrências do dia 19/10/2024 a 22/10/2024. "
        "A variável tabela_velocidade contém o link com as coordenadas exatas para apontarmos o local exato da ocorrência."
        "A tabela disponibilizada acima é sobre as ocorrências de velocidade. "
        "A Logística Florestal da Bracell inovando e utilizando IA para ajudar nas análises de infrações de velocidade!! "
    )
    
    # Formatar a tabela e incluir no contexto
    tabela_infracao = formatar_tabela(tabela_velocidade)
    
    # Combina o contexto, a tabela e a pergunta do usuário
    pergunta_com_contexto = f"{contexto}\n\nTabela de Dados:\n{tabela_infracao}\n\nPergunta: {pergunta}"
    
    # Corpo da requisição com a pergunta, contexto e a tabela
    data = {
        "contents": [
            {
                "parts": [
                    {"text": pergunta_com_contexto}
                ]
            }
        ]
    }
    
    params = {
        'key': api_key  # Chave de autenticação da API
    }
    
    # Fazendo a requisição POST
    response = requests.post(url, headers=headers, json=data, params=params)
    
    if response.status_code == 200:
        return response.json()  # Retorna a resposta em JSON
    else:
        return {"erro": "Falha ao se comunicar com a API.", "status_code": response.status_code}

# Função para extrair e formatar a resposta da API de forma amigável
def formatar_resposta(resposta):
    try:
        # Extraindo o texto da resposta gerada
        texto_resposta = resposta["candidates"][0]["content"]["parts"][0]["text"]
        return texto_resposta
    except (KeyError, IndexError):
        return "Não foi possível processar a resposta da API."

# Função principal para interface do Streamlit
def main():
    st.title("Painel de Infrações de Velocidade - Bracell")
    
    # Exibe uma saudação dinâmica com base na hora do dia
    saudacao = gerar_saudacao()
    st.write(f"{saudacao}! Este painel foi desenvolvido para analisar infrações de velocidade usando IA.")

    # Entrada de texto para a pergunta do usuário
    pergunta = st.text_input("Digite sua pergunta sobre as infrações de velocidade:")

    # Botão para consultar a API
    if st.button("Consultar Inteligência Artificial"):
        if pergunta and api_key:
            resposta = consultar_gemini_api(pergunta, api_key, tabela_velocidade)
            
            # Exibindo a resposta da API
            if 'erro' in resposta:
                st.error(f"Erro: {resposta['erro']} (Status code: {resposta['status_code']})")
            else:
                resposta_formatada = formatar_resposta(resposta)
                st.write("Resposta da IA:")
                st.write(resposta_formatada)
        else:
            st.warning("Por favor, insira a pergunta e a API Key.")

if __name__ == '__main__':
    main()

