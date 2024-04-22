from flask import Flask, render_template, redirect, request
import smtplib

app = Flask(__name__)

# Function to send email
def send_email(email, message, name, phone):
    sender_email = "tunemusic.org@gmail.com"  # Your email address
    receiver_email = "ahzaafs2004@gmail.com"  # Recipient's email address
    password = "@Mylanchi"  # Your email password

    # Create message
    msg = f"Subject: New Contact Form Submission\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"

    # Send email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        message = request.form['message']
        phone = request.form['phone']
        
        # Send email
        send_email(email, message, fullname, phone)
        
        # Redirecting back to the home page after form submission
        return redirect('/')
    else:
        return 'Method Not Allowed', 405

if __name__ == '__main__':
    app.run(debug=True)
