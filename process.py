#!env python3

import json
import sys

from typing import Dict

def get_metadata(path: str) -> Dict[str, str]:
    result = {}
    with open('icons.json') as f:
        icons = json.load(f)
        for key, value in icons.items():
            result[key] = value['unicode']
    return result

def print_typ(metadata: Dict[str, str]) -> None:
    start = """
#let fa(name) = {
  text(
    font: "Font Awesome 6 Free Solid",
    box[ #name ]
  )
}
    """
    print(start)
    for key, value in metadata.items():
        print(f"#let fa-{key} = fa(symbol(\"\\u{{{value}}}\"))")
    print("")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 process.py <path/to/icons.json> > output.typ")
        sys.exit(1)
    path = sys.argv[1]
    result = get_metadata(path)
    print_typ(result)