import streamlit as st

st.set_page_config(layout='wide', page_title='My App')

# html variable 
html = '''
<html>
    <head>
        <title>This HTML App</title>
    </head>
    <body>
        <h1>This Long Text!!!</h1>
        <br>
        <hr>
        <h3>This a small text</h3>
    </body>
</html>
'''

with open('./com_html.html', 'r', encoding='utf-8') as f:
    filehtml = f.read()
    f.close()

st.title('Fist app')

col1, col2 = st.columns((4,1))
with col1:
    with st.expander('Content'):
        st.subheader('Content11...')

    with st.expander('Content2_image..'):
        st.subheader('Content2_image...')
        st.image('./images/catdog.jpg')
        st.write('<h1>This is new title</h1>', unsafe_allow_html=True)
        st.markdown(html, unsafe_allow_html=True)

    with st.expander('Content3_htmlContent..'):
        st.subheader('Content3_htmlContent...')
        import streamlit.components.v1 as htmlviewer
        htmlviewer.html(filehtml, height=800)

with col2:
    with st.expander('Tips..'):
        st.subheader('Tips..')
