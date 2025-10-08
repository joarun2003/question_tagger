import gradio as gr
def ensure_nltk_resources():
    pass

demo = gr.Interface(
"""Launcher for the question_tagger Gradio demo.
This small wrapper keeps the repo root `app.py` runnable while moving
the main implementation into the `question_tagger` package.
"""
)
from question_tagger import demo


if __name__ == "__main__":
    demo.launch()