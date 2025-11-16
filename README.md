# Car_Evaluation_Model-
A simple and interactive web application that predicts the acceptability of a car (Unacceptable, Acceptable, Good, or Very Good) based on six categorical features, using a Machine Learning classification model.  The app is built with Flask, uses Label Encoders for preprocessing, and loads a trained model using Joblib.

✅ __Features__

Predicts the acceptability of a car based on user inputs
User-friendly web interface
Built using Python + Flask
Uses Label Encoders for all categorical features
Displays results with meaningful icons

❌ Unacceptable
👍 Acceptable
✅ Good
🌟 Very Good

🧰 __Prerequisites__

Python 3.7 or above
pip (Python package manager)

📥 __Installation__
1. Clone the repository
git clone https://github.com/Atchaya-62/Car_Evaluation_Model-/


2. Install dependencies
pip install -r requirements.txt

3. Run the Flask application
python app.py

4. Open the app in your browser
http://localhost:5000

🔍 __How It Works__

The model is trained on the Car Evaluation Dataset

All input fields (buying, maintenance, doors, persons, lug_boot, safety) are label encoded

The saved encoders (label_encoders.pkl) convert user inputs into numerical form

The trained model (model.pkl) predicts the car's acceptability

The prediction is converted back into human-readable format and displayed in a clean UI

📂 __File Structure__

car_evaluation_project/

├── app.py                 
├── model.pkl              
├── label_encoders.pkl    
├── requirements.txt       
├── templates/

│     └── index.html       

🌟 __Future Enhancements__

Add CSS styling for better UI

Add more ML models for comparison

Visualize feature importance

Deploy online (Render / Railway)


🖼 __Step-by-Step Guide__: How to Use the Car Evaluation App

Step 1: Input Form
<img width="1825" height="964" alt="image" src="https://github.com/user-attachments/assets/45811c00-c4d4-45f9-ba5a-8df205f7b948" />


Step 2: Fill the Details

<img width="744" height="831" alt="image" src="https://github.com/user-attachments/assets/ab9b7ed3-ba3c-4aff-b2b9-2c755acf1424" />


Step 3: View Prediction Result

<img width="747" height="155" alt="image" src="https://github.com/user-attachments/assets/d80078dc-328e-4ea6-ae5c-0cb32620eb05" />



