from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Configure the Generative AI API key
GOOGLE_API_KEY = ""
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize chat model
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

# Create Flask app
app = Flask(__name__)

# Define routes for each page
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/government-employee.html")
def government_employee():
    return render_template("government-employee.html")


@app.route("/alerts")
def alerts():
    return render_template("alerts.html")

@app.route("/blood_bank_info")
def blood_bank_info():
    return render_template("blood_bank_info.html")

@app.route("/blood_donation")
def blood_donation():
    return render_template("blood_donation.html")

@app.route("/blood_donation_schedule")
def blood_donation_schedule():
    return render_template("blood_donation_schedule.html")

@app.route("/appointments")
def appointments():
    return render_template("appointments.html")

@app.route("/book_appointment")
def book_appointment():
    return render_template("book_appointment.html")

@app.route("/call_subscription")
def call_subscription():
    return render_template("call_subscription.html")

@app.route("/cardiology")
def cardiology():
    return render_template("cardiology.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/video_consultation_booking")
def video_consultation_booking():
    return render_template("video_consultation_booking.html")


@app.route("/dermatology")
def dermatology():
    return render_template("dermatology.html")

@app.route("/epharmacy")
def epharmacy():
    return render_template("epharmacy.html")

@app.route("/epharmacy_order")
def epharmacy_order():
    return render_template("epharmacy_order.html")

@app.route("/family_insurance_details")
def family_insurance_details():
    return render_template("family-insurance-details.html")

@app.route("/individual_insurance_details")
def individual_insurance_details():
    return render_template("individual-insurance-details.html")

@app.route("/health_check")
def health_check():
    return render_template("health_check.html")

@app.route("/insurance")
def insurance():
    return render_template("insurance.html")

@app.route("/neurology")
def neurology():
    return render_template("neurology.html")

@app.route("/oncology")
def oncology():
    return render_template("oncology.html")

@app.route("/past_orders")
def past_orders():
    return render_template("past_orders.html")

@app.route("/pediatrics")
def pediatrics():
    return render_template("pediatrics.html")

@app.route("/radiology")
def radiology():
    return render_template("radiology.html")

@app.route("/reports")
def reports():
    return render_template("reports.html")

@app.route("/orthopedics")
def orthopedics():
    return render_template("orthopedics.html")

@app.route("/psychiatry")
def psychiatry():
    return render_template("psychiatry.html")

@app.route("/scan_prescription")
def scan_prescription():
    return render_template("scan_prescription.html")

@app.route("/sms_subscription")
def sms_subscription():
    return render_template("sms_subscription.html")

@app.route("/subscription")
def subscription():
    return render_template("subscription.html")

@app.route("/user_blood_info")
def user_blood_info():
    return render_template("user_blood_info.html")

@app.route("/video_consultation")
def video_consultation():
    return render_template("video_consultation.html")

@app.route("/visiting_doctor")
def visiting_doctor():
    return render_template("visiting_doctor.html")

@app.route("/volunteer")
def volunteer():
    return render_template("volunteer.html")

# New route for the "Become a Donor" page
@app.route("/become_donor")
def become_donor():
    return render_template("become_donor.html")

@app.route("/reimbursement")
def reimbursement():
    # Redirect to the reimbursement page
    return render_template("reimbursement.html")

# Add this route to handle redirection
@app.route("/redirect_to_index")
def redirect_to_index():
    return render_template("index.html")

# Chatbot Route
@app.route('/chat', methods=['POST'])
def chat_response():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = chat.send_message(user_input)
        return jsonify({"response": response.text})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

