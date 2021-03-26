"""
Example using the components provided by spacy-streamlit in an existing app.
Prerequisites:
python -m spacy download en_core_web_sm
"""
import spacy_streamlit
import streamlit as st

st.image(image='censusimg.jpg',caption='https://pixabay.com/illustrations/magnifying-glass-human-head-faces-1607208/')

# allows tooltips to function in fullscreen
st.markdown('<style>#vg-tooltip-element{z-index: 1000051}</style>',
             unsafe_allow_html=True)

DEFAULT_TEXT = """Google was founded in September 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a California privately held company on September 4, 1998, in California. Google was then reincorporated in Delaware on October 22, 2002."""

spacy_model = "en_core_web_sm"

st.title("Named Entity Recognition")
text = st.text_area("Text to analyze", DEFAULT_TEXT, height=200)
doc = spacy_streamlit.process_text(spacy_model, text)

spacy_streamlit.visualize_ner(
    doc,
    labels=["PERSON", "DATE", "GPE", "ORG"],
    show_table=False,
    title="Persons, dates and locations",
)

st.text(f"Analyzed using spaCy model {spacy_model}")