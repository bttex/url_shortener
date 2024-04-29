import pyshorteners as pys


def shortener():
    """
    Esta função pega uma URL longa como entrada e retorna uma URL curta usando a API do TinyURL.

    Parâmetros:
        long_url (str): A URL longa a ser curta

    Retorna:
        str: A URL curta

    """
    long_url = input("Enter the URL to shorten: ")

    type_tiny = pys.Shortener()
    short_url = type_tiny.tinyurl.short(long_url)
 
    print("The Shortened URL is: " + short_url)

shortener()