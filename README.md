# Font Awesome with Typst

## Usage

1. Download the font files from [Font Awesome](https://use.fontawesome.com/releases/v6.4.0/fontawesome-free-6.4.0-desktop.zip).

2. Unzip the downloaded file and install the fonts in the `otfs` folder to your system.

3. Copy the `fa.typ` file in this repository to your typst project.

4. Use the icons in your project:
```typst
import "fa.typ": *

#fa-github
```

## Build from source

Just run:
```bash
python3 process.py <path-to-font-awesome-folder/metadata/icons.json> > fa.typ
```

## License

The Font Awesome font files are licensed under the [SIL OFL 1.1](https://scripts.sil.org/OFL).

This project is licensed under the [MIT License](https://opensource.org/license/mit/).