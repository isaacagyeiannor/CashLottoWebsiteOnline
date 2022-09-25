from django.urls import path

from .views import (
    apps_chat_chat_view,
    apps_email_inbox_view,
    apps_email_read_view,
)

app_name = "apps"
urlpatterns = [
    
    # chat
    path("chat", view=apps_chat_chat_view, name="chat"),
    # Email
    path("email/inbox", view=apps_email_inbox_view, name="email.inbox"),
    path("emial/read_email", view=apps_email_read_view, name="email.read"),
]
