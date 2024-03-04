# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/18
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

import gradio as gr
from typing import Any
from Tofel.Gui.Information import Header as heaader

def build_tofel_record(
        *args: Any, 
        **kwargs: Any,
    ) -> gr.Blocks:

    demo = gr.Blocks(
        title='Chatter Judge',
    )

    with demo:
        gr.Markdown(
            heaader.tofel_record_header
        )


    # demo.auth=auth.auth_admin             # temporary disable auth
    # demo.auth_message = 'Welcome to Tofel!!!'

    return demo
