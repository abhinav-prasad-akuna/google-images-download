pip3 install -r requirements.txt
python3 setup.py install
googleimagesdownload -k "$1, $2" -l $3
cd downloads
ls

