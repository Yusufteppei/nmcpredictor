import streamlit as st
import predict

subjects = [
         'BIOLOGY',
         'CHEMISTRY',
         'JUNIOR INFORMATICS',
         'JUNIOR MATHEMATICS',
         'JUNIOR SCIENCE',
         'PHYSICS',
         'SENIOR INFORMATICS',
         'SENIOR MATHEMATICS'
    ]

header = st.container()
user_input = st.container()
result = st.container()

with header:
	st.title('NMC First Round Predictor')


with user_input:
	st.title('Input score and subject')
	sub = st.selectbox(label='Subject', options=subjects)
	sc = st.number_input(label='Score', max_value=100, min_value=0)

	if st.button('Predict Result'):
		with result:
			st.write(predict.predict(sub, sc))