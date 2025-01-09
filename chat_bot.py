# %%
import joblib

# Load trained Decision Tree model
model = joblib.load('loan_approval_prediction_model.joblib')

def get_user_input(prompt, input_type=str):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(f"Please enter a valid {input_type.__name__}.")

def predict_loan_acceptance(model, features):
    # Assuming 'features' is a list of all the required inputs for the model
    prediction = model.predict([features])
    return prediction[0]

def main():
    print("Welcome to the Loan Acceptance Prediction Chatbot!")
    
    # Collect user inputs
    name = get_user_input("Please enter your name: ", str)
    print("Hello "+name+", let me get some other information in order to predict if your loan application will be accepted or not.")
    
    #Required Attributes
    age = get_user_input("Please enter your age (only whole numbers): ", int)
    
    gender = get_user_input("Use the following number in place of your gender,\n0 for Female\n1 for Male\n2 for Others\nPlease enter your gender: ", int)
    
    experience = get_user_input("Please enter your experience i.e. number of years (only whole numbers): ", int)
    
    income = get_user_input("Please enter your monthly income: ", float)
    income = income/1000
    
    homeOwnership = get_user_input("Use the following number in place of your home ownership status,\n0 for Home Mortgage\n1 for Home Owner\n2 for Rent\nPlease enter your home ownership status: ", int)
    
    family = get_user_input("Please enter the number of members in your family: ", int)
    
    ccavg = get_user_input("Please enter your monthly average credit card expense: ", float)
    ccavg = ccavg/1000
    
    education = get_user_input("Use the following number in place of your level of education,\n1 for Bachelors Degree\n2 for Masters Degree\n3 for Advanced/Professional Degree\nPlease enter your education level: ", int)
    
    mortgage = get_user_input("Please enter your total mortgage: ", float)
    mortgage = mortgage/1000
    
    securityAccount = get_user_input("If you have a security account enter 1, else enter 0.\nDo you have a security account? : ", int)
    
    cdAccount = get_user_input("If you have a certificate of deposit account enter 1, else enter 0.\nDo you have a certificate of deposit account? : ", int)
    
    online = get_user_input("If you have a internet banking enter 1, else enter 0.\nDo you have a internet banking? : ", int)
    
    creditCard = get_user_input("If you have a credit card enter 1, else enter 0.\nDo you have a credit card? : ", int)
    
    
    # Make prediction
    features = [age,gender,experience,income,homeOwnership,family,ccavg,education,mortgage,securityAccount,cdAccount,online,creditCard]
    print(features)
    prediction = predict_loan_acceptance(model, features)
    
    if prediction == 1:
        print("Congratulations! Your loan application is predicted to be accepted.")
    else:
        print("Unfortunately, your loan application is predicted to be rejected.")
    
if __name__ == "__main__":
    main()

# %%
