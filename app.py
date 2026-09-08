import fitz  # PyMuPDF
import streamlit as st

st.set_page_config(
    page_title="Kifayatullah | Portfolio", layout="centered", page_icon="📄"
)

# Custom CSS for shadow and clean presentation
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 2rem;
            max-width: 900px;
        }
        [data-testid="stImage"] img {
            border-radius: 8px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.15);
            margin-bottom: 15px;
        }
    </style>
""",
    unsafe_allow_html=True,
)

PDF_PATH = "My Personal Portfolio (1).pdf"


@st.cache_data
def render_pdf_to_images(file_path):
    doc = fitz.open(file_path)
    images = []
    for page in doc:
        # Render page to image at 150 DPI for crisp quality
        pix = page.get_pixmap(dpi=150)
        images.append(pix.tobytes("png"))
    return images


try:
    pdf_pages = render_pdf_to_images(PDF_PATH)
    for img in pdf_pages:
        st.image(img, use_container_width=True)
except FileNotFoundError:
    st.error(
        f"Could not find '{PDF_PATH}'. Ensure the PDF is in the same folder as app.py and the filename matches exactly."
    )
