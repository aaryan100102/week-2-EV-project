⚡ Week 2 – Electric Vehicle (EV) Project
🚗 Overview

This week’s project focuses on building an intelligent Electric Vehicle (EV) cost prediction system integrated with an interactive chatbot interface.
The goal is to allow users to estimate the approximate price of an EV based on its key technical specifications such as battery capacity, efficiency, power, and other attributes.

The project combines machine learning, data preprocessing, and user-friendly automation to provide an end-to-end predictive experience.

🎯 Objectives

Develop a machine learning model to predict EV cost based on performance and design parameters.

Build an interactive Python chatbot that guides users to enter vehicle details.

Enable real-time cost prediction with a conversational interface.

Deploy a structured and modular EV cost estimation system.

🧠 Machine Learning Model

Model Used: XGBoost Regressor

Training Dataset: EV specifications dataset (battery, range, power, etc.)

Output: Predicted cost (converted into INR ₹)

Saved Model File: ev_price_predictor_xgboost.joblib

Features Used:

brand

battery_capacity_kwh

efficiency_wh_per_km

motor_power_kw

charging_time_hr

curb_weight_kg

seats

💬 EV Assistant Chatbot

The EV Chatbot acts as an assistant that interacts with the user to collect EV parameters and displays a real-time estimated cost.

🔧 How It Works:

The chatbot prompts the user to enter EV details interactively.

Inputs are passed to the trained ML model.

The model predicts the approximate EV cost in INR.

A summary of inputs and predictions is displayed neatly in the console.

🚀 Outcomes

Built an end-to-end EV cost prediction system.

Integrated interactive user chatbot for real-time estimation.

Enhanced understanding of XGBoost regression, feature engineering, and user interaction design.

📅 Week 2 Summary

✅ Model trained successfully using XGBoost
✅ Chatbot integrated for real-time EV price prediction
✅ Clean codebase with modular structure and GitHub version control
