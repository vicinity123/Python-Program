import re


def link_params(link):
    pattern = re.compile(r"([a-zA-Z]+)=([a-zA-Z0-9_]+)")
    matches = re.findall(pattern, link)
    return dict(matches)


def link_extend(link):
    pattern = re.compile(r"/(\w+)")
    matches = re.findall(pattern, link)
    if "www" in matches:
        matches.remove("www")
    return f"https://youtube.com/watch?v={matches[0]}"
