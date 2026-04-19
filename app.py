import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model/house_price_model.pkl")

# Title
st.title("🏠 House Price Prediction App")

st.write("Enter the details of the house to predict its price.")

# Load dataset to get feature columns
df = pd.read_csv("data/cleaned_dataset.csv")
X = df.drop("SalePrice", axis=1)

# Sidebar inputs
st.sidebar.header("Input Features")

input_data = {}

for col in X.columns:
    if X[col].dtype == "int64" or X[col].dtype == "float64":
        input_data[col] = st.sidebar.number_input(
            f"{col}", 
            value=float(X[col].mean())
        )
    else:
        input_data[col] = st.sidebar.text_input(
            f"{col}", 
            value=str(X[col].mode()[0])
        )

# Convert input to DataFrame
input_df = pd.DataFrame([input_data])

# Encoding (same as training)
input_encoded = pd.get_dummies(input_df)

# Align with training columns
input_encoded = input_encoded.reindex(columns=X.columns, fill_value=0)

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_encoded)[0]

    # Convert USD → INR
    price_inr = prediction * 83  # Approx conversion rate

    st.success(f"""
🏡 **Estimated House Price**

💵 USD: ${prediction:,.2f}  
🇮🇳 INR: ₹{price_inr:,.2f}
""")