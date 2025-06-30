     
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Title
st.set_page_config(page_title="WordCloud Generator", layout="centered")
st.title("🎨 WordCloud Generator")

# User input for text
text_input = st.text_area("Enter your text below:", height=200)

# Options for background color
bg_color = st.selectbox(
    "Choose background color:",
    ["black", "white", "skyblue", "lightgreen", "beige", "pink"]
)

# Options for colormap
colormap = st.selectbox(
    "Choose color theme:",
    ["Accent", "viridis", "plasma", "inferno", "magma", "cividis", "Set1", "Pastel1"]
)

# Button to generate WordCloud
if st.button("Generate WordCloud") and text_input.strip():
    # Generate WordCloud
    wordcloud = WordCloud(
        width=800,
        height=400,
        margin=2,
        background_color=bg_color,
        colormap=colormap,
        mode='RGBA'
    ).generate(text_input)

    # Display WordCloud
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)
else:
    st.info("Enter some text and click the button to generate a word cloud.")      
      