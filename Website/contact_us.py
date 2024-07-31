from flask import Blueprint, redirect, render_template, request,flash,session, url_for

from Website.mail import send_mail

contact= Blueprint("contact",__name__)

@contact.route('/contact-us',methods=['GET', 'POST'])
def contactUs():
   
    if request.method == 'POST':
        user_email = request.form.get("email")
        username = request.form.get("firstName")
        user_lastname = request.form.get("lastName")
        input_message = request.form.get("message")
        receiver_email = "carecompass5@gmail.com"

        full_message = f"""User: {username} {user_lastname}\nEmail: {user_email}\n
{input_message}"""

        message = f"Subject: New Event\n\n{full_message}"

        # Function to send email
        send_mail(user_email, username, user_lastname, message, receiver_email)
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact.contactUs'))

    return render_template('contactDetails.html')