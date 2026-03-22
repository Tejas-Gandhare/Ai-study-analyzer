import streamlit as st
import pandas as pd
import pickle

# Load model (we will save it first)
model = pickle.load(open("model.pkl", "rb"))

st.title("🎓 AI Study Analyzer")

st.write("Enter your study details:")

hours = st.slider("Hours Studied", 0, 12, 5)
sleep = st.slider("Sleep Hours", 0, 10, 7)
phone = st.slider("Phone Usage (hours)", 0, 10, 3)
attendance = st.slider("Attendance (%)", 0, 100, 75)

if st.button("Predict"):

    data = pd.DataFrame({
        'hours_studied': [hours],
        'sleep_hours': [sleep],
        'phone_usage': [phone],
        'attendance': [attendance]
    })

    prediction = model.predict(data)

    st.subheader(f"📊 Predicted Marks: {prediction[0]:.2f}")

    # Suggestions
    suggestions = []

    if hours < 6:
        suggestions.append("📚 Increase study time")
    if sleep < 6:
        suggestions.append("😴 Improve sleep")
    if phone > 4:
        suggestions.append("📱 Reduce phone usage")
    if attendance < 75:
        suggestions.append("🏫 Improve attendance")

    if not suggestions:
        suggestions.append("✅ Great job!")

    st.subheader("💡 Suggestions:")
    for s in suggestions:
        st.write("-", s)
        st.markdown("---")
        st.markdown("### 🚀 Improve your performance with smart AI insights")
        st.success(f"📊 Predicted Marks: {prediction[0]:.2f}")
        st.warning(s)