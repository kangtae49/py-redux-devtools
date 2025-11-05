import argparse
import webview
from apps.utils import get_index_url

def run():

    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", action="store_true", help="verbose")
    args = parser.parse_args()
    debug = args.verbose

    webview.create_window(
        title='PyReduxDevtools',
        url=get_index_url(),
        text_select=True,
        draggable=True,
        zoomable=False,
        confirm_close=False,
        width=840, height=600,
    )

    webview.start(debug=debug)