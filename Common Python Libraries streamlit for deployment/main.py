import streamlit as st

st.title('My project')
st.header('This is a header')
st.subheader('This is a subheader')
st.text('AI Viet Nam')
st.caption('This is a caption')

st.divider()

st.markdown('# Heading 1')
st.markdown('[AI Viet Nam](https://)')
st.markdown("""
    1. Machine Learning
    2. Deep Learning
""")
st.markdown(r'$ \sqrt{2x} $')

st.divider()

st.latex('\sqrt{2x}')

st.write('')

st.write('AI Viet Nam')
st.write('# Heading 1')
st.write('[Google](http://)')
st.write('1 + 1 = ', 2)

st.divider()
st.code("""
    import random
    value = random.randint(3, 10)
    print(value)
""")

def get_year():
    return '19'

with st.echo():
    st.write('This is a text')
    def get_name():
        return 'Thai'
    
    name = get_name()
    year = get_year()

    st.write(name, year)

agree = st.checkbox('I agree !')

if agree:
    st.write('Thank !')

status = st.selectbox('Your contact', ['Email', 'Address'])
print(status)

options = st.multiselect('Colors:', ['Green', 'Yellow', 'Blue'], ['Yellow'])
print(options)

if st.button("Say Hello"):
    st.write("Hello")
else:
    st.write("Goodbye")

value = st.text_input('Your name', value = 'Thai')
st.write(value)

st.divider()

uploaded_files = st.file_uploader('Choose Files', accept_multiple_files = True)
for uploaded_file in uploaded_files:
    read_f = uploaded_files.read()
    st.write('File Name:', uploaded_file.name)

with st.form('my form'):
    col1, col2 = st.columns(2)
    f_name = col1.text_input('Name:')
    f_age = col2.text_input('Age:')

    submited = st.form_submit_button('Submit')
    if submited:
        st.write(f'Name {f_name}, Age: {f_age}' )

st.divider()

import random
value = random.randint(1, 10)
if 'key' not in st.session_state:
    st.session_state['email'] = value
    st.session_state['password'] = value
# st.write(st.session_state.key)
