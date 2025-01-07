# PDF Utility Suite
PDF Utility Suite is a comprehensive, user-friendly application for managing PDF files. It allows users to convert images to PDF, split PDF files into individual pages or a range of pages, and merge multiple PDF files into a single document. Built with Python and a simple GUI using Tkinter, this tool is perfect for anyone seeking efficient PDF management.

# Features

1. Convert Images to PDF

 Supports popular image formats like JPG and PNG.
 
 Easily convert images into high-quality PDF files.

2. Split PDF Files

 Extract specific pages or ranges of pages from a PDF.
 
 Save the extracted pages as individual PDF files in a specified folder.

3. Merge PDF Files

Combine multiple PDF files into one seamless document.

Maintain the order and structure of the original PDFs.

# Technologies Used

Python
Tkinter (for GUI development)
PyPDF2 (for PDF manipulation)
img2pdf (for image-to-PDF conversion)
Pillow (for image handling)

# Setup Instructions
Follow these steps to run the project on your local machine:
 
 # Prerequisites
 Ensure you have the following installed:
 
  Python (version 3.7 or later)
  
  pip (Python package installer)
  
  Installation
  
  Clone the repository:
  
  git clone https://github.com/your-username/pdf-utility-suite.git
  cd pdf-utility-suite
  
  Install the required dependencies:
  
  pip install -r requirements.txt
  
  Run the application:
  
  python PDF_Converter.py

# Usage

Launch the application by running PDF_Converter.py.
Select one of the following options from the GUI:

Convert: Choose an image to convert to PDF.
Split: Select a PDF to extract specific pages or ranges.
Join: Merge two or more PDF files into one.

# You can follow the prompts to select files and save the output.

Building an Executable

# You can create a standalone executable for the application using cx_Freeze:

  Ensure cx_Freeze is installed:
  
  pip install cx_Freeze
  
  Run the setup.py script:
  
  python setup.py build


# License

This project is licensed under the MIT License. See the LICENSE file for more details.

# Acknowledgments

PyPDF2 for robust PDF processing.
Pillow and img2pdf for seamless image handling.
The Python community for extensive documentation and support.

# For any questions or feedback, feel free to open an issue or contact me through the repository!


