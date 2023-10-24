"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
import reflex as rx
import openai as ai 

ai.api_key = "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"

class State(rx.State):
    #app state 
    prompt = ""
    image_url = ""
    processing = False
    complete = False


    def get_image(self):
        #get image from prompt
        if self.prompt == "": 
            return rx.window_alert("prompt Empty")
        
        self.processing = True 
        self.complete = False
        yield
        response = ai.Image.create(prompt=self.prompt, n=1, size="1024x1024")
        self.image_url = response["data"][0]["url"]
        self.processing, self.complete = False, True


def index():
    return rx.center(
         rx.vstack(
              rx.heading("DALL-E"),
              rx.input(placeholder="Enter a prompt", on_blur=State.set_prompt),
              rx.button(
                   "Generate",
                    on_click=State.get_image, 
                    is_loading=State.processing,
                    width="100%",
              ),
              rx.cond(
                    State.complete,
                    rx.image(
                          src=State.image_url,
                          height="25em",
                          width="25em",
                    )
              ),
              padding="2em",
              shadow="lg",
              border_radius="lg",
         ),
         width="100%",
         height="100vh",
    )


#Add state and page to app.
app = rx.App()
app.add_page(index, title="reflex:DALL-E")
app.compile()