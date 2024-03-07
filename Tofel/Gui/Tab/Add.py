import gradio as gr
from Tofel.Utils.Rule import PART_OF_SPEECH

def init_add_new_word_tab() -> gr.Tab:
    with gr.Tab("Add New Word") as add_new_word:

        with gr.Row():
            vocabulary = gr.Textbox(
                label="Word",
                info="Enter the word you want to add",
                scale=1
            )

            part_of_speech = gr.Dropdown(
                label="Part of Speech",
                info="Select the part of speech of the word",
                choices=PART_OF_SPEECH.keys(),
                type="index",
                scale=1
            )
            sentance = gr.Textbox(
                label="Sentance",
                info="Enter a sentance using the word",
                scale=3,
            )

        gr.Button(
            value="Add",
            variant="primary",
        )

    return add_new_word
