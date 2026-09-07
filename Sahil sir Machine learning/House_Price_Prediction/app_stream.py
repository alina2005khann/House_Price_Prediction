
import pickle
import pandas as pd
import streamlit as st

# =========================
# Page Configuration
# =========================

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# =========================
# Load Model
# =========================

with open("model_Final.pkl", "rb") as file:
    model = pickle.load(file)

with open("locations.pkl", "rb") as file:
    locations = pickle.load(file)
    locations = list(locations)

with open("area_type.pkl", "rb") as file:
    area_types = pickle.load(file)
    area_types = list(area_types)

with open("avalibility.pkl", "rb") as file:
    available = pickle.load(file)
    available = list(available)


# =========================
# Prediction Function
# =========================

def predict_house_price(
    area_type,
    availability,
    location,
    size_BHK,
    total_sqft,
    bath,
    balcony
):
    try:
        # Create input data
        data = [[
            area_type,
            availability,
            location,
            int(size_BHK),
            float(total_sqft),
            int(bath),
            int(balcony)
        ]]

        # Column names must be exactly the same
        # as the columns used during model training
        columns = [
            "area_type",
            "availability",
            "location",
            "size_BHK",
            "total_sqft",
            "bath",
            "balcony"
        ]

        df = pd.DataFrame(data, columns=columns)

        # Prediction
        prediction = model.predict(df)

        price = round(prediction[0], 2)

        return price

    except Exception as e:
        return f"Error: {str(e)}"


# =========================
# Streamlit Interface
# =========================

st.title("🏠 House Price Prediction")

st.write(
    "Enter the property details below to predict "
    "the estimated house price."
)

st.divider()


# =========================
# Input Section
# =========================

col1, col2 = st.columns(2)

with col1:

    area_type = st.selectbox(
        "Area Type",
        options=area_types,
        index=(
            area_types.index("Super built-up Area")
            if "Super built-up Area" in area_types
            else 0
        )
    )

    availability = st.selectbox(
        "Availability",
        options=available
    )

    location = st.selectbox(
        "Location",
        options=locations
    )

    size_BHK = st.number_input(
        "BHK Size",
        min_value=1,
        value=2,
        step=1
    )


with col2:

    total_sqft = st.number_input(
        "Total Size (sqft)",
        min_value=100.0,
        value=1000.0,
        step=50.0
    )

    bath = st.number_input(
        "Number of Bathrooms",
        min_value=1,
        value=2,
        step=1
    )

    balcony = st.number_input(
        "Number of Balconies",
        min_value=0,
        value=1,
        step=1
    )


st.divider()


# =========================
# Prediction Button
# =========================

if st.button("🔮 Predict House Price", type="primary"):

    result = predict_house_price(
        area_type,
        availability,
        location,
        size_BHK,
        total_sqft,
        bath,
        balcony
    )

    if isinstance(result, (int, float)):

        st.success(
            f"🏠 Estimated House Price: ₹{result} Lakh"
        )

    else:

        st.error(f"❌ {result}")
        
