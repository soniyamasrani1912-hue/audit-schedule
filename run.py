import webview
import os
import sys

def main():
    # Get the directory where the script is located
    if getattr(sys, 'frozen', False):
        # Running as compiled exe
        app_dir = sys._MEIPASS
    else:
        # Running as script
        app_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Path to the HTML file
    html_path = os.path.join(app_dir, 'index-5.html')
    
    # Create and start the window
    window = webview.create_window(
        'Audit Schedule',
        html_path,
        width=1200,
        height=900,
        min_size=(800, 600)
    )
    
    webview.start(debug=False)

if __name__ == '__main__':
    main()
