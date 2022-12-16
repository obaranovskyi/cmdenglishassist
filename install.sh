echo 'Installing cmdenglishassist'
mkdir -p ~/.config
cd ~/.config
python3 -m pip install -e git+https://github.com/obaranovskyi/cmdenglishassist.git#egg=cmdenglishassist
cd ~/.config/src/cmdenglishassist
pip install -r requirements.txt
