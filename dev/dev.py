"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

class State(rx.State):
    """The app state."""
    
    #backend

    count: int = 0
  
    def incremenet(selft):
        selft.count += 1

    def decremenet(selft):
        selft.count -= 1

#frontend

def index():
    return rx.vstack(
        rx.hstack(
        rx.button(
            "decrement",
            color_scheme="amber",
            on_click= State.decremenet,

        ),
        rx.heading(State.count, font_size = "2em"),
        rx.button(
            "incremenet",
            color_scheme="grass",
            on_click=State.incremenet,

        ),spacing="5",
    )
    )

app = rx.App()
app.add_page(index)
