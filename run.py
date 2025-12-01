import webview
import os
import sys

app_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(app_dir, 'index-5.html')

window = webview.create_window(
    'Audit Schedule',
    html_path,
    width=1200,
    height=900
)
webview.start()
