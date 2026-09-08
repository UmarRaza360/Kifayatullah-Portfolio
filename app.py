import base64
import streamlit as st

st.set_page_config(
    page_title="Kifayatullah | Portfolio", layout="wide", page_icon="📄"
)

# Custom CSS to hide default Streamlit padding and maximize display area
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
    </style>
""",
    unsafe_allow_html=True,
)


def render_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")

    # Embed PDF in an iframe filling the view height
    pdf_display = f"""
        <iframe 
            src="data:application/pdf;base64,{base64_pdf}#toolbar=0&navpanes=0&scrollbar=0" 
            width="100%" 
            height="900px" 
            type="application/pdf"
            style="border: none; border-radius: 8px;"
        >
        </iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)


render_pdf("My Personal Portfolio (1).pdf")
