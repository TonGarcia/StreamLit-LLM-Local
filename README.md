# Stream Lit local ChatBot

1. Install OLLAMA from it WebSite: https://ollama.com/
2. Run a OLLAMA model: `$ ollama run llama3.2`
3. Install Python3
   1. MacOS: already installed
   2. Windows: download it from the site: https://www.python.org/downloads/
4. Install pip3
   1. MacOS: already installed
   2. Windows: 
      1. `> curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
      2. `> python get-pip.py`
5. Install+Generate+Activate pyenv:
   1. **create** your local venv: `$ python3 -m venv venv`
   2. **activate** your local venv: `$ source venv/bin/activate`
   3. **install** depnendencies: `$ pip install -r requirements.txt`
6. Run StreamLit: `$ streamlit run app.py`
7. **PS.:** 
   1. before running the streamlit:app on PyCharm it is necessary to run the command directly on the Terminal
   2. on the terminal input/insert your email to sign on it 

# Folders Structure

1. **experiments**: some backup code for reference future investigations
2. **src**: the application source code for long run
3. **app.py**: the application entry point