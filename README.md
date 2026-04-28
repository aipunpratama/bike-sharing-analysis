## Setup Environment - Anaconda
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt

## Setup Environment - Shell/Terminal
mkdir proyek_analisis_data
cd notebook
pipenv install
pipenv shell
pip install -r requirements.txt

## Run Streamlit App
cd dashboard
streamlit run dashboard.py

## Link Dashboard
https://aipun-bike-sharing-analysis.streamlit.app/
