import streamlit as st
import joblib
import json
import pandas as pd

model = joblib.load(open('./models/LinearSVC.pkl', 'rb'))
vec = joblib.load(open('./models/vectorizer.pkl', 'rb'))
val = pd.read_csv('./data/val.txt', sep=';')
val.columns = ['TEXT','EMOTION']



with open('./data/emotions.json', 'rb') as j:
    emotions = json.load(j)

def main(title='Multi-Class Text Classification Application'):
    st.title(title)
    st.markdown(
        f'''
            <style>
                .css-1lcbmhc .e1fqkh3o3 {{
                    width: 375px;
                }}
            </style>
        ''',
        unsafe_allow_html=True
    )
    st.sidebar.write('Validation Data unSeen By Model. Copy and Paste and Example OR Type Your Own!')
    with st.sidebar.expander('Examples'):
        st.dataframe(val)

    text = st.text_input('Enter Text then click "Run Classification"')
    if st.button('Run Classification'):
        p = model.predict(vec.transform([text]))

        predicted = emotions[str(p[0])]

        st.sidebar.write('Prediction: {}'.format(predicted))




if __name__ == '__main__':
    main()