import openai
import streamlit as st
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")


def generate_article(title, outline):
  model_engine = "text-davinci-003"
  prompt = (f"Escribe un sermón  con ocasión de '{title}' basado en el siguiente esquema:\n{outline}. El sermón debe contener al menos una cita bíblica en cada sección")

  completions = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      max_tokens=3024,
      n=1,
      stop=None,
      temperature=0.7,
  )

  article = completions.choices[0].text
  return article

st.title("Generador de sermones")

sidebar = st.sidebar
title = sidebar.text_input("Título:")
outline = sidebar.text_area("Esquema:")

if st.button("Generar sermón"):
  article = generate_article(title, outline)
  st.success(article)
