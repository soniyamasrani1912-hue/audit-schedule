import webview

webview.create_window(
    'Audit Schedule',
    'index-5.html',
    width=1200,
    height=900,
    min_size=(800, 600)
)
webview.start()
