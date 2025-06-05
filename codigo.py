import pyautogui
import time

# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar 1 tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotskey -> apertar uma combinação de teclas

pyautogui.PAUSE = 0.7

# Passo 1: Entrar no sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# esperar 3 segundos
time.sleep(3)

# Passo 2: Fazer login
# preencher email
pyautogui.click(x=630, y=506)
pyautogui.write("cristiansouto2019@gmail.com")
# preencher senha
pyautogui.press("tab")
pyautogui.write("123456")
# botão logar
pyautogui.press("tab")
pyautogui.press("enter")
# espera de 3segundos
time.sleep(3)


# Passo 3:  Importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar 1 produto
for linha in tabela.index: #para cada linha da minha tabela
    pyautogui.click(x=693, y=368)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab") #passar para o proximo campo
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab") #passar para o proximo campo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab") #passar para o proximo campo
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab") #passar para o proximo campo
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab") #passar para o proximo campo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab") #passar para o proximo campo
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab") #passar para o botao enviar
    pyautogui.press("enter") #dar enter e enviar

    pyautogui.scroll(10000) # voltar para o inicio da pagina

# Passo 5: Repetir para todos os produtos
