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
   1. **create** your local venv:
      1. Windows: 
         1. CMD: `> python -m venv venv`
         2. GitBash: `$ python -m venv venv`
      2. MacOS: `$ python3 -m venv venv`
   2. **activate** your local venv: 
      1. MacOS: `$ source venv/bin/activate`
      2. Windows:  
         1. GitBash: `>  source venv/Scripts/activate`
         2. CMD: `> venv\Scripts\activate`
   3. **install** depnendencies: 
      1. `$ brew install cmake apache-arrow`
      2. `$ pip install -r requirements.txt`
6. Run StreamLit: `$ streamlit run app.py`
7. **PS.:** 
   1. before running the streamlit:app on PyCharm it is necessary to run the command directly on the Terminal
   2. on the terminal input/insert your email to sign on it 
8. **PyCharm Debug**:
   1. create a config run
   2. if it raise any error on run/debug just delete and create a new run file:
      1. set it to **module** instead of _script_
      2. **module** value = `streamlit`
      3. **script parameters** = `run app.py`
   3. **IF** errors like: "asyncio\base_events.py:182" or "Python\Python312\Lib\asyncio\events.py", line 88" **you must disable**  `python.debug.asyncio.repl`:
      1. click on seach icon (top right near to close button X)
      2. type on the search input: "registry" and click on "registry..."
      3. look for `python.debug.asyncio.repl` and uncheck the checkbox

# Folders Structure

1. **experiments**: some backup code for reference future investigations
2. **src**: the application source code for long run
3. **app.py**: the application entry point