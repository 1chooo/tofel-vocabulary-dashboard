import gradio as gr


def init_add_new_word_tab() -> gr.Tab:
    with gr.Tab("Add New Word") as add_new_word:
        gr.Markdown(
            "Add New Word"
        )

    return add_new_word
