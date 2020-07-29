pip install -r requirements.txt
python3 setup.py install
echo $1
googleimagesdownload $1
cd downloads
ls

