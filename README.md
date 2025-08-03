# ASCII Art Generator

![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A simple yet powerful Python script that converts any image into beautiful ASCII art. This tool uses the Pillow library to process images and map pixel brightness to a customizable set of characters, rendering the art directly in your terminal and saving it to a file.

## Demo

---

## Features

-   **Image to Text**: Converts standard image formats (JPG, PNG, etc.) into text-based art.
-   **Smart Resizing**: Automatically resizes the source image to an optimal width for terminal display while maintaining the correct aspect ratio.
-   **Console Output**: Prints the final ASCII art directly to the console.
-   **File Saving**: Saves the generated art to `ascii_image.txt` for easy viewing and sharing.
-   **Highly Customizable**: Easily modify the character set or output width to change the final look.

---

## Getting Started

Follow these instructions to get the project running on your local machine.

### Prerequisites

Make sure you have **Python 3** installed on your system.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Praveen-Thathsara/ASCII-img-Generator.git](https://github.com/Praveen-Thathsara/ASCII-img-Generator.git)
    cd YOUR_REPOSITORY_NAME
    ```

2.  **Create a `requirements.txt` file** in your project folder and add the following line to it:
    ```
    Pillow
    ```

3.  **Install the necessary packages:**
    ```bash
    pip install -r requirements.txt
    ```

---

## How to Use

1.  Place the image you want to convert into the root directory of the project.
2.  Run the script from your terminal:
    ```bash
    python art.py
    ```
3.  When prompted, enter the full name of your image file (e.g., `my_cat.png`) and press Enter.
4.  The script will display the art in the terminal and save the result to `ascii_image.txt`.

---

## Customization

You can easily tweak the `art.py` script to change the output.

-   **Character Set**: Modify the `ASCII_CHARS` list to change the "texture" of the art. The list should be ordered from the visually darkest character to the lightest.

    ```python
    # Feel free to experiment with different characters
    ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
    ```

-   **Output Width**: In the `main()` function, find the `resize_image` call and change the `new_width` value to make the art wider or narrower.

    ```python
    # Change 100 to your desired character width
    resized_image = resize_image(image, new_width=100)
    ```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

