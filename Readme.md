![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

# OpenCV Color Space Converter

A simple command-line utility built with Python and OpenCV to load an image and visualize it in different color spaces like Grayscale, HSV, CIELAB, and RGB.

![Demo GIF showing the script running in the terminal and displaying images](./project1demo.gif)

---

## 📖 About the Project

This project was built to explore the fundamentals of digital image processing using the OpenCV library. The main goal was to understand how images are represented in different color spaces and to create a hands-on utility for visualizing these transformations. This tool provides a simple, interactive way to see the effects of converting a standard BGR image into other popular color models used in computer vision.

### 🛠️ Built With

* **Python**
* **OpenCV**

---

## ✨ Features

* **Load Local Images**: Load any image from your computer by providing its file path.
* **Interactive CLI Menu**: An easy-to-use menu to select the desired color space.
* **Multiple Conversions**:
    * BGR to **Grayscale**
    * BGR to **HSV** (Hue, Saturation, Value)
    * BGR to **CIELAB**
    * BGR to **RGB**

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

You'll need to have Python 3 and pip installed on your system.

### Installation

1.  **Clone the repository** to your local machine.
    ```sh
    git clone [https://github.com/zerowraith/colourSpaceChanger.git](https://github.com/ZeroWraith/colourSpaceChanger.git)
    cd colourSpaceChanger
    ```

2.  **(Recommended)** Create and activate a virtual environment. This keeps your project dependencies isolated.
    ```sh
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages** : run the following command in your terminal to install them

```sh
    pip install -r requirements.txt
    ```

---

## Usage

1.  Run the main script from your terminal.
    ```sh
    python main.py
    ```

2.  The program will prompt you to enter the path to your image.
    ```
    Enter the path to the image: C:\Users\YourUser\Pictures\park.jpg
    ```

3.  Once the image is loaded, you will see a menu of options.
    ```
    Choose an option --
    1. Greyscale
    2. HSV
    3. CIELAB
    4. RGB
    5. Quit
    Enter your Choice:
    ```

4.  Enter the number corresponding to the conversion you want to see. Two windows will pop up: one with the original image and one with the converted image.

5.  To close the image windows, simply press any key. To exit the program, choose option **5** from the menu.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## 📧 Contact

Aaditya Pratap Singh - [LinkedIn](https://linkedin.com/in/aps-cv)    [GitHub](https://github.com/zerowraith)

Project Link: [https://github.com/zerowraith/colourSpaceChanger.git](https://github.com/zerowraith/colourSpaceChanger.git)
