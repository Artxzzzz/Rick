###
--------------------------------------------------------
# Rick

## 🔒 Licença:
* Este projeto está licenciado sob a [` GNU General Public License v3.0 `](LICENSE)

## Créditos:
* A arte ASCII usada nesse projeto foi retirada do repositório `ascii-live`:
https://github.com/hugomd/ascii-live


### 💡 Exemplos de uso
``` bash
rick -c Blue
rick -f 3
rick -v
rick -b
rick -s
```
* Opções disponíveis:
    - `-c, --color <color>` → Define a cor do ASCII
    - `-f, --frame <fps>` → Controla a velocidade da animação
    - `-b, --bright` → Ativa cores brilhantes
    - `-v, --version `→ Exibe a versão do programa
    - `-s, --sound` → Abre uma página no navegador com Never Gonna Give You Up


### 🔧 Funcionalidades:
* Alternar entre cores brilhantes ou não
* Trocar o **FPS**
* Trocar a cor

### ⚙️ Requisitos:
* 🐍 `Python 3.13.3` ou superior
* 📚 Bibliotecas Python:
    ```
    pip install colorama
    ```
    Ou
    ```
    pip install -r requirements.txt
    ```

### 💻 Como instalar:

**Por Releases (recomendado)**  
- Baixe o `Rick.exe`
- Execute o `install.bat` **como administrador** na mesma pasta  
- Pronto: use `Rick` em qualquer terminal

**Pelo source-code**  
- Gere o executável conforme abaixo  
- Renomeie-o para `rick.exe`
- Execute o `install.bat` como acima



### ▶️ Como executar:
* Baixe ou clone o repositório usando 
    ``` bash
    git clone https://github.com/Artxzzzz/Rick.git
    ```
* Na pasta do projeto execute:

    ``` python
    python main.py
    ```

### 🔨 Gerando um executável:
* Instale a biblioteca do `PyInstaller` usando

    ``` python
    pip install pyinstaller
    ```
* Depois gere o executável usando

    ``` python
    pyinstaller --onefile --add-data "frames;frames" main.py
    ```

* Agora o executável estará na pasta `dist/`

### Contribuindo para o projeto


### ✍️ Como contribuir

 - Faça um fork ou clone o repositório:
	``` bash
	https://github.com/Artxzzzz/Rick.git
	```
 - Crie uma branch para suas alterações:
	``` bash
	git checkout -b minha-feature
	```
 - Faça suas alterações, commit e push:	
	``` bash
	git add .
	git commit -m "descrição do que fez"
	git push origin minha-feature
	```
* Agora é só abrir uma **Pull Request**

### 📂 Estrutura do projeto:

-  `main.py` - Fluxo principal do programa, onde todos os `módulos` são controlados

- `install.bat` - Código que instala o `Rick.exe` na `PATH` do usuário

- `packages/` - Packages utilitários
    - `__init__.py` - Inicializador do package
    - `constants.py` - Constantes

- `frames/` - Pasta onde os frames ficam organizados pelo `ID` deles (EX: 0, 1, 2 ...)

- `manager/` - Package `gerenciador`
    - `__init__.py` - Inicializador do package
    - `args.py` - Módulo que gerencia os `argumentos`
    - `frames.py` - Módulo que recebe os `frames`
    - `getArgs.py` - Módulo que recebe `argumentos`
    - `playAscii.py` - Módulo que toca a `ASCII art`

- `features/` - Package de `features`
    - `__init__.py` - Inicializador do package
    - `showVersion.py` - Módulo que amostra a versão
