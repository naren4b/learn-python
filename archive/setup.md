```bash
sudo apt update && sudo apt upgrade -y

sudo apt install build-essential software-properties-common -y

sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt update -y

sudo apt install python3 -y

sudo apt install -y python-is-python3

sudo apt install pipx -y
pipx ensurepath
python --version

# Creates the virtual environment and creates the directory '.venv'
# pyvenv.cfg file inside your .venv folder and change the line `include-system-site-packages = false` to `true`. 
# pip cache dir

python -m venv .venv --system-site-packages
source .venv/bin/activate

pip install -r requirements.txt
python app.py 
# Then install ruff globally
pipx install ruff
# ruff format <filename>