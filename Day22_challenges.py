
import streamlit as st 

st.title('st.form 製作表單 ->  使用with 來向表單添加內容＆一定要包含st.form_submit_button')

st.header('1.Example of using **with** notation')
st.subheader('Coffee Order Form')

with st.form('my_form'):
        st.subheader(' **Order your coffee**')
        #Input Widgets
        coffee_bean_val = st.selectbox('Coffee Bean',['Arabica','Robusta','Taiwan'])
        coffee_roast_val = st.selectbox('Coffee Roast',['Light','Mediun','Dark'])
        brewing_val = st.selectbox('Brewing Method',['Aeropress','Drip','French Press','Moka Pot', 'Siphon'])
        serving_type_val = st.selectbox ('Serving format',['Hot','Iced','Frappe'])
        milk_val = st.select_slider ('Milk Intensity',['None','Low','Medium','High'])
        owncup_val = st.checkbox('Bring your own cup')
        add_sugar = st.checkbox('Additional Sugar?')

        submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        '''    )
else: 
      st.write('Place your order!')

      st.header('Example2 - Example of object notation')

      form = st.form('Form_2')
      selected_val = form.slider("select a value plz")
      form.form_submit_button('Submitted')

      st.write('Selected Value: ', selected_val)