import streamlit as st
import pandas as pd
import os

def show():
    st.title("History Page")
    data = pd.read_csv('./data/history.csv')
    st.write(data)

show()







    # show_history()

# def show_history():
#     if "history" in st.session_state:
#         st.markdown("### Vodafone Churn Prediction History")
#         input_features_df = st.session_state['df']
#         history_df = pd.DataFrame(st.session_state["history"])
#         history_df = pd.concat([history_df, input_features_df], axis=1)

#         new_column_order = ['Model-Chosen', 'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Prediction', 'Probability', 'Date', 'Time']
#         history_df = history_df[new_column_order]

#         # Save history dataframe to CSV including new columns
#         save_to_csv(history_df)

#         display_saved_file("History.csv")
#     else:
#         st.write("No previous history found.")

# def save_to_csv(history_df):
#     try:
#         # Check if the file exists
#         if os.path.isfile("History.csv"):
#             # If it exists, append the new data to the file
#             history_df.to_csv("History.csv", mode='a', index=False, header=False)
#         else:
#             # If it doesn't exist, create a new file
#             history_df.to_csv("History.csv", index=False)
#     except Exception as e:
#         st.error(f"Error saving history to CSV: {e}")

# def display_saved_file(file_path):
#     try:
#         saved_df = pd.read_csv(file_path)
#         st.write(saved_df)
#     except Exception as e:
#         st.error(f"Error reading and displaying saved file: {e}")

# def main():
#     show()

# if __name__ == "__main__":
#     main()
