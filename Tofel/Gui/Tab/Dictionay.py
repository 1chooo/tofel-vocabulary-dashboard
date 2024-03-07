import gradio as gr
from Tofel.Utils.Rule import PART_OF_SPEECH

def init_dictionay() -> gr.Tab:
    with gr.Tab("Dictionary") as dictionay:

        gr.Textbox(
            label="Search",
            info="Enter the word you want to search",
        )
        
        with gr.Row():
            gr.CheckboxGroup(
                choices=PART_OF_SPEECH.keys(),
                label="Part of Speech", 
                info="Select the part of speech that you want to display",
                scale=5,
            ),

            with gr.Column():
                gr.Button(
                    value="Clear",
                )

                gr.Dropdown(
                    choices=["A-Z", "Z-A", "Frequency"],
                    label="Sort", 
                    scale=1,
                ),


    return dictionay
