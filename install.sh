echo 'Installing cmdenglishassist'
cd ~
mkdir -p ~/.config
python3 -m pip install -e git+https://github.com/obaranovskyi/cmdenglishassist.git#egg=cmdenglishassist
cd cmdenglishassist
pip install -r requirements.txt
