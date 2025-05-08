from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    return render(request, 'main/projects.html')

def contact(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        # Validate form data
        if not name or not email or not subject or not message:
            messages.error(request, 'Please fill in all fields.')
            return redirect('contact')

        # Compose the email
        email_subject = f"New Contact Form Submission: {subject}"
        email_message = f"""
        Name: {name}
        Email: {email}
        Subject: {subject}
        Message: {message}
        """

        try:
            # Send the email
            send_mail(
                email_subject,
                email_message,
                settings.EMAIL_HOST_USER,  # From email
                [settings.EMAIL_HOST_USER],  # To email (your email)
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again later.')
            # Log the error for debugging
            print(f"Error sending email: {e}")

        return redirect('contact')

    return render(request, 'main/contact.html')