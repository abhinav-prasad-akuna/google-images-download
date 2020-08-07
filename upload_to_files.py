from requests_toolbelt import MultipartEncoder
import requests
import os


file = "dist/google_images_download-2.8.0-py2.py3-none-any.whl"
with open(file, 'rb') as f:
    session = requests.Session()
    form = MultipartEncoder({
        "creator": "abhinav.prasad",
        "fileInfo": ("google_images_download-2.8.0-py2.py3-none-any.whl", f),
    })
    headers = {"Content-Type": form.content_type}
    res = session.post(url="https://files-api.ch1devhubble.akunacapital.local/put", headers=headers, data=form)
    print(res.text)
    session.close()
