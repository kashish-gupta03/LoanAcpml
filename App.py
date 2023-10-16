import streamlit as st

st.title("Loan Acceptance Prediction")
st.info("Please fill the following details to predict whether you will get loan or not")

gender = st.text_input(" Entrer your gender male(1) and female(0)")
married = st.text_input("Enter your marital status yes(1) and no(0)")
dependents = st.text_input("Enter your dependents")
education = st.text_input("Enter your education graduate(1) and not graduate(0)")
self_employed = st.text_input("Enter your self employed yes(1) and no(0)")
applicant_income = st.number_input("Enter your applicant income")
coapplicant_income = st.number_input("Enter your coapplicant income")
loan_amount = st.text_input("Enter your loan amount")
loan_amount_term = st.text_input("Enter your loan amount term")
credit_history = st.text_input("Enter your credit history")
property_area = st.text_input("Enter your property area rural(0) semiurban(1) urban(2)")

def loan():
    # Check if all input fields are filled
    if not all([married,dependents,gender,education,self_employed,applicant_income,coapplicant_income,loan_amount,loan_amount_term,credit_history,property_area]):    
        st.warning("Please fill in all the features.")
    else:
       if applicant_income%2 == 0:
        st.error("Loan is not accepted")
       else:
        applicant_income != 0
        st.success("Loan is accepted")


# Create a button to trigger the car price prediction
if st.button("Predict The Loan"):
    loan()

# Footer
st.markdown("---")
st.write("Designed and Developed by Kashish Gupta")
