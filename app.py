import streamlit as st
import PyPDF2

def merge_pdfs(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf_file in pdf_list:
        merger.append(pdf_file)
    return merger

def main():
    st.title("PDF Combiner App")
    st.write("Upload multiple PDF files and combine them into a single PDF.")

    uploaded_files = st.file_uploader("Choose PDF files to combine", type=["pdf"], accept_multiple_files=True)

    if uploaded_files:
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
