import streamlit as st
from my_chromadb.chroma_ops import get_latest_version
from ai_writer.writer import rewrite_chapter
from ai_reviewer.reviewer import score_text

st.title("📚 AI Book Rewriter Dashboard")

# Input: Paste a book chapter
original_text = st.text_area("📘 Original Chapter", height=250)

if st.button("✍️ Rewrite Chapter with AI"):
    if original_text.strip() == "":
        st.warning("Please paste a chapter first!")
    else:
        with st.spinner("Rewriting with AI..."):
            rewritten = rewrite_chapter(original_text)
            score = score_text(rewritten)

        st.subheader("✍️ AI Rewritten Chapter")
        st.write(rewritten)

        st.subheader("🏅 Reward Score")
        st.metric("RL Score", f"{score:.2f}")

        if st.checkbox("📝 Edit Before Saving"):
            human_feedback = st.text_area("Make changes:", value=rewritten)
        else:
            human_feedback = rewritten

        if st.button("✅ Save Version"):
            # Save using your ChromaDB wrapper
            get_latest_version().add_version(original_text, human_feedback, score)
            st.success("Version saved in ChromaDB!")

st.sidebar.header("🔍 Previously Saved Versions")

if st.sidebar.button("📂 View Latest Version"):
    latest = get_latest_version().fetch_latest()
    if latest:
        st.sidebar.write("📝 Last Saved Rewrite")
        st.sidebar.write(latest['text'])
        st.sidebar.write("🏅 Score:", latest['score'])
    else:
        st.sidebar.info("No versions found.")
