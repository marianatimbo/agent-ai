import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
import yaml

with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)
os.environ['OPENAI_API_KEY'] = config['OPENAI_API_KEY']

openai = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)

template = ''' 
Você é especialista em comunicação empresarial.

Escreva um Email sobre o seguinte objetivo: "{objetivo}".

Esse email deve ser destinado a "{destinatario}", que está representando a empresa "{empresa}".

O email deve ser desenvolvido com o tom {tom} no idioma {idioma}.

Certifique-se de que o e-mail seja claro, direto e profissional.
Inclua um título e uma saudação apropriada.
'''

prompt_template = PromptTemplate.from_template(template=template)

tons = ['Formal', 'Direto', 'Amigável']
idiomas = ['Português', 'Inglês', 'Francês', 'Espanhol']

st.title('Gerador de Email Empresarial:')

objetivo = st.text_input('Descreva o objetivo do email:')
destinatario = st.text_input('Escreva o nome do destinatário:')
empresa = st.text_input('Escreva o nome da empresa relacionada ao destinatário:')
tom = st.selectbox('Selecione o tom da email:', tons)
idioma = st.selectbox('Selecione o idioma da email:', idiomas)

if st.button('Gerar Email'):
    prompt = prompt_template.format(
        objetivo = objetivo,
        destinatario = destinatario,
        empresa = empresa,
        tom = tom,
        idioma = idioma
    )

    response = openai.invoke(prompt)
    st.subheader('Email Gerado:')
    st.write(response.content)
