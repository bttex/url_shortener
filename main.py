import pyshorteners as pys
import requests
import streamlit as st

# Configuração da página
st.set_page_config(page_title="Encurtador", layout="centered",page_icon="🔗")

# Seleção de idioma
language = st.radio("Escolha o idioma / Choose the language", ["Português", "English"])

# Dicionário de traduções
translations = {
    "header": {"Português": "Encurtador de links", "English": "Link Shortener"},
    "input_placeholder": {"Português": "Cole o link para encurtar:", "English": "Paste the link to shorten:"},
    "success_message": {"Português": "URL encurtada: {}", "English": "Shortened URL: {}"},
    "error_message": {"Português": "Erro ao encurtar a URL: {}", "English": "Error shortening the URL: {}"},
    "warning_message": {"Português": "Erro com {}: {}", "English": "Error with {}: {}"},
    "no_services": {
        "Português": "Nenhum serviço de encurtador está disponível no momento.",
        "English": "No shortening service is currently available."
    },
}

# Título do aplicativo
st.header(translations["header"][language])

# Função principal para tentar encurtar o link usando os serviços TinyURL e is.gd
def encurtar_link(link):
    encurtadores = [encurtar_com_tinyurl, encurtar_com_isgd]
    for encurtador in encurtadores:
        try:
            short_url = encurtador(link)
            return short_url
        except Exception as e:
            st.warning(translations["warning_message"][language].format(encurtador.__name__, e))
            continue
    raise Exception(translations["no_services"][language])

# Função para encurtar o link usando TinyURL
def encurtar_com_tinyurl(link):
    type_tiny = pys.Shortener()
    return type_tiny.tinyurl.short(link)

# Função para encurtar o link usando is.gd
def encurtar_com_isgd(link):
    api_url = f"https://is.gd/create.php?format=simple&url={link}"
    response = requests.get(api_url)
    response.raise_for_status()
    return response.text

# Entrada do usuário no Streamlit
link = st.text_input(translations["input_placeholder"][language])

# Verifica se o link foi preenchido
if link:
    try:
        short_url = encurtar_link(link)
        st.success(translations["success_message"][language].format(short_url))
    except Exception as e:
        st.error(translations["error_message"][language].format(e))
