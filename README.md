# PDF Combiner App

[PDF Combiner App](https://combinepdf.streamlit.app/)

## Overview

The PDF Combiner App is a web-based application that allows users to securely combine multiple PDF files into a single PDF document while ensuring data privacy. This app is built using [Streamlit](https://streamlit.io/), a user-friendly Python library for creating interactive web applications, and [PyPDF2](https://pythonhosted.org/PyPDF2/), a Python library for handling PDF files.

## Features

- Secure PDF Combination: The app ensures that your data is processed securely and no uploaded files are stored on the server or shared with any third-party.

- Privacy Protection: All data uploaded to the app remains private, and no traces of the uploaded files are left on the server after processing.

- User-Friendly Interface: The app provides a simple and intuitive user interface that makes it easy to upload and combine PDF files effortlessly.

## How to Use

1. **Install Dependencies:** Before running the app, make sure you have Python and the required dependencies installed. You can install the dependencies using the provided `requirements.txt` file: 
```bash
pip install -r requirements.txt
```

2. **Run the App:** Once the dependencies are installed, you can start the app by running the following command in your terminal:
```bash
streamlit run pdf_combiner_app.py
```


3. **Upload PDF Files:** Once the app is running, you will see the PDF Combiner interface. Use the "Choose PDF files to combine" file uploader to select the PDF files you want to combine.

4. **Combine PDFs:** After selecting the PDF files, the app will merge them into a single PDF document.

5. **Download Combined PDFs:** Once the PDFs are combined, the app will generate a zip folder containing the combined PDF file. Click the "Download Combined PDFs" button to download the zip folder to your local machine.

## Important Note

- This app is intended for combining PDF files, and no other file formats are supported.

- The maximum allowed file size for combined PDFs is set to 50 MB. If your files exceed this limit, you may need to split them into smaller segments or optimize the PDFs before combining.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).


## Contributions

Contributions to this project are welcome! If you find any issues or have ideas for improvement, feel free to open an issue or submit a pull request.





