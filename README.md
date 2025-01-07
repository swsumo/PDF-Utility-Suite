PDF Utility Suite

Welcome to PDF Utility Suite! This project is an all-in-one solution for working with PDF files. Whether you need to convert images to PDFs, split large PDFs into smaller files, or merge multiple PDFs into one, this application has you covered.

Features

1. Image to PDF Conversion

Convert images (JPG, PNG, etc.) to PDF format.

Save the generated PDF with your chosen filename and location.

2. Split PDF Files

Extract specific pages from a PDF file.

Save the split pages as individual PDF files in a designated folder.

3. Merge PDF Files

Combine two PDF files into a single document.

Save the merged file with a custom filename.

4. User-Friendly Interface

Built with Tkinter for a clean and intuitive graphical interface.

Reset functionality to reload the UI for new operations.

How to Use

Prerequisites

Python 3.8 or higher installed on your system.

Required libraries:

tkinter

PyPDF2

img2pdf

Pillow

Install the dependencies using:

pip install PyPDF2 img2pdf Pillow

Steps to Run

Clone the repository:

git clone https://github.com/your-username/pdf-utility-suite.git

Navigate to the project directory:

cd pdf-utility-suite

Run the application:

python PDF_Converter.py

Build the Executable

To create an executable for distribution:

Ensure cx_Freeze is installed:

pip install cx_Freeze

Use the provided setup.py to build the executable:

python setup.py build

The executable will be available in the build folder.

Project Structure

pdf-utility-suite/
├── PDF_Converter.py    # Main application script
├── setup.py            # Script to build the executable using cx_Freeze
├── README.md           # Project documentation
└── requirements.txt    # Dependencies for the project

Future Enhancements

Add support for password-protected PDFs.

Include batch processing for large-scale operations.

Integrate OCR functionality to extract text from images.

Contribution

Contributions are welcome! If you'd like to add new features, fix bugs, or improve the documentation:

Fork the repository.

Create a new branch:

git checkout -b feature-name

Commit your changes:

git commit -m "Add your message here"

Push to your branch:

git push origin feature-name

Open a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Credits

Developed by Swapnil. Visit again for more exciting tools and utilities!


 
