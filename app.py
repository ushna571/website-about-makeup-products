import streamlit as st
from PIL import Image

# Set the title of the app
st.title("⚖️ BMI Calculator")

# Create a sidebar with additional information
st.sidebar.title("Additional Information")
st.sidebar.write("📞 Contact Number: +1-234-567-890")
st.sidebar.write("🌐 Facebook: [facebook.com/yourpage](https://facebook.com/yourpage)")
st.sidebar.write("🌐 Instagram: [instagram.com/yourpage](https://instagram.com/yourpage)")
st.sidebar.title("How to Control Your Weight")
st.sidebar.write("""
- Maintain a balanced diet
- Exercise regularly
- Monitor your weight regularly
- Stay hydrated
- Get enough sleep
- Avoid stress
""")

# Create a container with a specified width
container = st.container()
with container:
    # Display an image with a specified width
    image = Image.open('image.png')
    st.image(image, caption='🧍 Body Mass Index', width=300)  # Set the width to 300 pixels

    # Input fields for weight and height
    weight = st.number_input("⚖️ Enter your weight (kg):", min_value=0.0, format="%.2f")
    height = st.number_input("📏 Enter your height (m):", min_value=0.0, format="%.2f")

    # Calculate BMI
    if st.button("🧮 Calculate BMI"):
        if height > 0:
            bmi = weight / (height ** 2)
            st.write(f"📊 Your BMI is {bmi:.2f}")
            
            # Display BMI category and suggest reward or punishment
            if bmi < 18.5:
                category = "underweight"
                st.write(f"⚠️ You are {category}. Consider eating more nutritious food.")
            elif 18.5 <= bmi < 24.9:
                category = "normal weight"
                st.write(f"✅ You are {category}. Great job! Treat yourself to your favorite food.")
            elif 25 <= bmi < 29.9:
                category = "overweight"
                st.write(f"⚠️ You are {category}. Consider exercising more.")
            else:
                category = "obese"
                st.write(f"⚠️ You are {category}. Consider consulting with a healthcare provider.")
