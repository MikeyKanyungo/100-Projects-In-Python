"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
import reflex as rx
import openai as ai 

ai.api_key = "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"

class State(rx.state):
    #app state