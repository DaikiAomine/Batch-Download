import webbrowser

with open("links.txt") as f:
    for url in f:
        webbrowser.open_new_tab(url.strip())