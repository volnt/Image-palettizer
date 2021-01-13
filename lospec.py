import os
import re

import requests


def palette_retriever(name):
    palette_name = name.casefold().strip()
    palette_name = re.sub(r"[\s_]", "-", palette_name)
    palette_name = re.sub(r"([^\w-])", "", palette_name)

    r = requests.get(f"https://lospec.com/palette-list/{palette_name}.gpl", timeout=1.5)
    r.raise_for_status()
    if not os.path.exists("./palettes"):
        os.mkdir("./palettes")
    pal_path = os.path.abspath(f"./palettes/{palette_name}.gpl")
    with open(pal_path, mode="wb+") as f:
        f.write(r.content)
