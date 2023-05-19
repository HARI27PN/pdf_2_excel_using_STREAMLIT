import os
import streamlit as st
import tabula
import pandas as pd

# Function to convert PDF to Excel
def convert_to_excel(pdf_file):
    try:
        # Read the PDF file and extract the tabular data
        df = tabula.read_pdf(pdf_file, pages='all')

        # Convert the extracted data to a Pandas DataFrame
        df = pd.concat(df)

        return df

    except Exception as e:
        st.error(f"Error occurred while converting {pdf_file.name}: {str(e)}")
        return None

# Streamlit app
def main():
    st.title("PDF to Excel Converter")

    # File uploader
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        # Convert PDF to Excel
        df = convert_to_excel(uploaded_file)

        if df is not None:
            # Display the converted DataFrame
            st.subheader("Converted Excel Data")
            st.dataframe(df)

            # Save as Excel file
            excel_file = st.button("Save as Excel")
            if excel_file:
                excel_filename = f"{uploaded_file.name.replace('.pdf', '.xlsx')}"
                df.to_excel(excel_filename, index=False)
                st.success(f"Excel file saved as {excel_filename}")

# Run the app
if __name__ == "__main__":
    main()
