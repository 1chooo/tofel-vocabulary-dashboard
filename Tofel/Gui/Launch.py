# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/18
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

import gradio as gr
from typing import Any
from Tofel.Gui.Information import Header as heaader
from Tofel.Gui.Tab.Add import init_add_new_word_tab
from Tofel.Gui.Tab.Dictionay import init_dictionay

def build_tofel_record(
        *args: Any, 
        **kwargs: Any,
    ) -> gr.Blocks:

    demo = gr.Blocks(
        title='Tofel Vocabulary Record',
    )

    with demo:
        gr.HTML(
            heaader.tofel_record_header
        )

        init_add_new_word_tab()

        init_dictionay()

        with gr.Tab("Quiz"):
            gr.Markdown(
                "Quiz"
            )

        with gr.Tab("Memory"):
            gr.Markdown(
                "Memory"
            )


    return demo
