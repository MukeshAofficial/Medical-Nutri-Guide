import openai
import streamlit as st
import os

# Set your OpenAI API key
openai.api_key = os.environ.get("API_KEY")

def generate_nutrition_plan(calories):
    # Define the prompt
    prompt = f"Generate a nutrition plan for {calories} calories per day."

    # Generate the completion
    completion = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150
    )

    # Extract and return the response
    return completion.choices[0].text.strip()

# Allow users to input their details
age = st.number_input("Enter your age:", min_value=15, max_value=80, step=1)
gender = st.selectbox("Select your gender:", ["Male", "Female"])
height_cm = st.number_input("Enter your height in cm:")
weight_kg = st.number_input("Enter your weight in kg:")
activity_level = st.selectbox("Select your activity level:", ["Sedentary", "Lightly active", "Moderately active", "Very active", "Extra active"])

# Calculate daily calorie requirements
if gender == "Male":
    bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
elif gender == "Female":
    bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

if activity_level == "Sedentary":
    calories = bmr * 1.2
elif activity_level == "Lightly active":
    calories = bmr * 1.375
elif activity_level == "Moderately active":
    calories = bmr * 1.55
elif activity_level == "Very active":
    calories = bmr * 1.725
elif activity_level == "Extra active":
    calories = bmr * 1.9

if st.button("Generate Nutrition Plan"):
    # Generate nutrition plan
    nutrition_plan = generate_nutrition_plan(calories)

    # Display the nutrition plan
    st.write("Nutrition Plan:")
    st.write(nutrition_plan)
