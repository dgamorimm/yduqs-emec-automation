<img class="imagem" src="https://yt3.googleusercontent.com/Zw6DksF6r6iGrKd2_IoqY93NXDtvS6D-8qWfUjw8ImZvA39QrUUQw4f2cFnA7y39-Oy8GFAn=s176-c-k-c0x00ffffff-no-rj" alt="YDUQS" style="width:300px;height:200px;border-radius: 100px;display: block; margin-left: auto; margin-right: auto;">

---
toc: true
---

## Pré Requisitos
+ **Python:** versão 3.10.11
+ **SO:** Windows 10
+ **Input:** Arquivo excel respeitando a ordem das colunas
  1. Periodo --------------------> Célula[ <font color='red'>A1</font> ]
  2. Disciplina ------------------> Célula[ <font color='red'>B1</font> ]
  3. Horas ----------------------> Célula[ <font color='red'>C1</font> ]
  4. Ementa ---------------------> Célula[ <font color='red'>D1</font> ]
  5. BibliografiaBasica ----------> Célula[ <font color='red'>E1</font> ]
  6. BibliografiaComplementar -> Célula[ <font color='red'>F1</font> ]


## Preparando o ambiente
+ Criar o ambiente (*Executar o comando no terminal do powershell*)
  + **```python -m venv .venv```**
+ Ativar o ambiente (*Executar o comando no terminal do powershell*)
  + **```.venv/Scripts/activate```**
+ Atualizando o Pip (*Executar o comando no terminal do powershell*)
  + **```python -m pip install --upgrade pip```**
+ Instalando as libs (*Executar o comando no terminal do powershell*)
  + **```pip install -r requirements.txt```**

## Executando a aplicação
+ Executar o comando no terminal do powershell
  + **```python setup.py```**

## Acessando a aplicação
+ Abrir o navegador e colocar o seguinte endereço
  + <a href="http://localhost:8501" target="_blank">http://localhost:8501</a>

![AppInit](image/app-init.png)

## Iniciando a aplicação
+ Adicionando as camadas de input

![AppInputs](image/inputs.png)

+ Realizar o login =>**ATENÇÃO**<=
  1. Quando clicar no botão de login, irá abrir o navegador do Chrome nesse endereço

![AppLogin](image/login.png)

  2. Ao aparecer essa tela, clique em "OK" para fechar o Pop-Up.
  3. O login deverá ser feito em uma outra janela devido a bloqueios de segurança por parte do orgão, portanto aperte a tecla **```CTRL + N```**
  4. Faça o login nesta nova janela e mantenha a outra ainda aberta

![AppTwoWindows](image/two-windows.png)
  
  5. Feito isso, volte para a aplicação e aperte o botão **Executar**

![AppExecute](image/execute.png)

## Logs
![AppLogs](image/logs.png)

## Suporte
![AppSupport](image/support.png)