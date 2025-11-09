import joblib
import numpy as np
import pandas as pd

# ===============================
# Load Trained Model
# ===============================
try:
    model_pipeline = joblib.load("ev_price_predictor_xgboost.joblib")
    print(" Loaded model from ev_price_predictor_xgboost.joblib")
except Exception as e:
    print(f" Error loading model: {e}")
    model_pipeline = None

print(" EV Assistant Chatbot (type 'exit' anytime to quit)")
print("----------------------------------------------------\n")

# ===============================
# Chat Loop
# ===============================
while True:
    user_input = input(" You: ").strip().lower()
    if user_input in ["exit", "quit"]:
        print(" Chatbot: Thanks for chatting! Have an electrifying day ⚡")
        break

    elif "predict" in user_input:
        if model_pipeline is None:
            print(" Model not loaded. Please check your model file.")
            continue

        print("\n Let’s estimate your EV’s cost!")
        print("Provide the following details (press Enter to use default).")

        try:
            # Collect 7 key features
            brand = input("brand: ") or "default_brand"
            battery_capacity_kwh = float(input("battery_capacity_kwh: ") or 60)
            efficiency_wh_per_km = float(input("efficiency_wh_per_km: ") or 5)
            motor_power_kw = float(input("motor_power_kw: ") or 200)
            charging_time_hr = float(input("charging_time_hr: ") or 1.5)
            curb_weight_kg = float(input("curb_weight_kg: ") or 1800)
            seats = int(input("seats: ") or 5)

            # Get feature names expected by model
            try:
                feature_names = model_pipeline.feature_names_in_
            except AttributeError:
                feature_names = [f"feature_{i}" for i in range(model_pipeline.n_features_in_)]

            # Create dummy DataFrame for prediction
            input_df = pd.DataFrame(columns=feature_names)
            for col in input_df.columns:
                input_df[col] = [0]  # fill with default zeros

            # Fill available columns with provided values if names match
            for col in input_df.columns:
                if "battery" in col.lower():
                    input_df[col] = battery_capacity_kwh
                elif "efficiency" in col.lower():
                    input_df[col] = efficiency_wh_per_km
                elif "motor" in col.lower():
                    input_df[col] = motor_power_kw
                elif "charge" in col.lower() or "charging" in col.lower():
                    input_df[col] = charging_time_hr
                elif "weight" in col.lower():
                    input_df[col] = curb_weight_kg
                elif "seat" in col.lower():
                    input_df[col] = seats
                elif "brand" in col.lower():
                    input_df[col] = hash(brand) % 100  # simple encoding for unseen brand

            # Predict cost
            predicted_cost = model_pipeline.predict(input_df)[0]

            # Convert to INR
            predicted_cost_inr = predicted_cost * 83.0

            # Display results
            print("\n===================================")
            print(" EV Cost Estimation Summary")
            print("===================================")
            print(f" Brand: {brand}")
            print(f" Battery Capacity: {battery_capacity_kwh} kWh")
            print(f" Efficiency: {efficiency_wh_per_km} Wh/km")
            print(f" Motor Power: {motor_power_kw} kW")
            print(f" Charging Time: {charging_time_hr} hr")
            print(f" Weight: {curb_weight_kg} kg")
            print(f" Seats: {seats}")
            print("-----------------------------------")
            print(f" Estimated EV Cost: ₹ {predicted_cost_inr:,.2f}")
            print("===================================")
            print(" Estimated cost (converted to INR).\n")

        except Exception as e:
            print(f" Prediction error: {e}")

    else:
        print(" Chatbot: I can predict EV cost! Just type 'predict' to start.\n")
