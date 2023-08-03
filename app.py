import streamlit as st
from PyPDF2 import PdfFileMerger

def merge_pdfs(pdf_list):
    merger = PdfFileMerger()
    for pdf_file in pdf_list:
        merger.append(pdf_file)
    return merger

def main():
    st.title("PDF Combiner App")
    st.write("Upload multiple PDF files and combine them into a single PDF.")

    uploaded_files = st.file_uploader("Choose PDF files to combine", type=["pdf"], accept_multiple_files=True)

    if uploaded_files:
        total_file_size = sum(file.size for file in uploaded_files)
        max_file_size = 50 * 1024 * 1024  # 50 MB (adjust this as needed)

        if total_file_size > max_file_size:
            st.error(f"Total file size exceeds the maximum limit of {max_file_size / (1024 * 1024)} MB.")
            return

        pdf_list = [pdf_file for pdf_file in uploaded_files]
        merger = merge_pdfs(pdf_list)

        # Merge the PDFs and create a combined PDF
        output_pdf = "combined_pdf.pdf"
        with open(output_pdf, "wb") as output:
            merger.write(output)

        st.success("PDFs successfully combined. Click the link below to download the combined PDF:")
        st.markdown(f"[Download Combined PDF]({output_pdf})")

if __name__ == "__main__":
    main()
