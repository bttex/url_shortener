import pyshorteners as pys
import requests
import streamlit as st

st.set_page_config(page_title="Encurtador",layout="centered")

# Título do aplicativo
st.header("Encurtador de links com Fallback")

# Função principal para tentar encurtar o link usando os serviços TinyURL e is.gd
def encurtar_link(link):
    """
    Tenta encurtar o link usando TinyURL e is.gd.
    Se um falhar, passa para o outro.
    """
    # Lista de funções para encurtar o link
    encurtadores = [
        encurtar_com_tinyurl,  # Serviço TinyURL
        encurtar_com_isgd      # Serviço is.gd
    ]
    
    # Tentativa de encurtamento usando cada serviço
    for encurtador in encurtadores:
        try:
            short_url = encurtador(link)  # Tenta encurtar o link
            return short_url  # Retorna a URL encurtada se funcionar
        except Exception as e:
            st.warning(f"Erro com {encurtador.__name__}: {e}")  # Exibe aviso em caso de erro
            continue  # Passa para o próximo serviço

    # Se nenhum encurtador funcionar, lança uma exceção
    raise Exception("Nenhum serviço de encurtador está disponível no momento.")

# Função para encurtar o link usando TinyURL
def encurtar_com_tinyurl(link):
    """
    Encurta o link usando a API do TinyURL via pyshorteners.
    """
    type_tiny = pys.Shortener()
    return type_tiny.tinyurl.short(link)

# Função para encurtar o link usando is.gd
def encurtar_com_isgd(link):
    """
    Encurta o link usando a API do is.gd diretamente.
    """
    api_url = f"https://is.gd/create.php?format=simple&url={link}"
    response = requests.get(api_url)  # Faz a requisição à API
    response.raise_for_status()  # Verifica se houve erro na requisição
    return response.text  # Retorna a URL encurtada

# Entrada do usuário no Streamlit
link = st.text_input("Cole o link para encurtar:")

# Verifica se o link foi preenchido
if link:
    try:
        # Tenta encurtar o link usando os serviços disponíveis
        short_url = encurtar_link(link)
        st.success(f"URL encurtada: {short_url}")  # Exibe a URL encurtada
    except Exception as e:
        st.error(f"Erro ao encurtar a URL: {e}")  # Exibe erro caso nenhum serviço funcione
