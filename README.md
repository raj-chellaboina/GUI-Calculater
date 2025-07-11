﻿# GUI-Calculater
# Custom Calculator

A graphical calculator application built with [customtkinter](https://github.com/TomSchimansky/CustomTkinter) for the UI and [pygame](https://www.pygame.org/) for sound effects. Supports basic arithmetic and advanced functions like trigonometry, square root, cube root, and logarithm.

## Features

- Basic arithmetic operations (+, -, *, /, %, etc.)
- Advanced functions: sin, cos, tan, sqrt, cbrt, log
- Sound effects for button presses
- Toggle for advanced/trigonometric functions
- Customizable and modern UI

## Requirements

- Python 3.x
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
- [pygame](https://www.pygame.org/)

Install dependencies with:

```sh
pip install customtkinter pygame
```

## Usage

1. Place your sound files in the specified paths or update the paths in `customcalci.py`.
2. Run the calculator:

```sh
python customcalci.py
```

## Notes

- The calculator uses Python's `eval()` for expression evaluation. Be cautious with input.
- Sound files must exist at the paths specified in the code, or you will get an error.

## File Structure

- [`customcalci.py`](customcalci.py): Main application file.

## License

This project is for educational
