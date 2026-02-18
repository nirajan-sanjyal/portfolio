from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse


def dashboard(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not email or not message:
            messages.error(request, "Please fill in name, email, and message.")
            return redirect(f"{reverse('profiles:dashboard')}#contact")

        subject = f"Portfolio Contact from {name}"
        body = (
            f"Name: {name}\n"
            f"Email: {email}\n\n"
            f"Message:\n{message}"
        )

        try:
            send_mail(
                subject=subject,
                message=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
                fail_silently=False,
            )
            messages.success(request, "Message sent successfully.")
        except Exception:
            messages.error(request, "Could not send message right now. Please try again.")

        return redirect(f"{reverse('profiles:dashboard')}#contact")

    return render(request, "profiles/dashboard.html")
