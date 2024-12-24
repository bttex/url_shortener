# Url Shortener

Este projeto é um encurtador de links que utiliza os serviços TinyURL e is.gd. Se um dos serviços falhar, o outro é utilizado como fallback. A interface do usuário é construída com Streamlit.

## Funcionalidades

- Encurtamento de links usando TinyURL e is.gd
- Interface de usuário simples e intuitiva com Streamlit
- Mensagens de erro e sucesso exibidas na interface

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/bttex/url_shortener
    cd url_shortener
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Execute o aplicativo Streamlit:
    ```bash
    streamlit run main.py
    ```

2. Abra o navegador e acesse o endereço fornecido pelo Streamlit (geralmente `http://localhost:8501`).

3. Cole o link que deseja encurtar no campo de entrada e pressione Enter.

## Estrutura do Código

- [`main.py`](main.py ): Contém a lógica principal do aplicativo, incluindo as funções para encurtar links usando TinyURL e is.gd, e a interface do usuário com Streamlit.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.