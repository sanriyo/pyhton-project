from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self):
        data = {"message_title" : "Favorite Quote",
                "message": "Life is 10% what happens to you and 90% how you react to it."}
        return data
    
class AboutPageView (TemplateView):
    template_name = "resume.html"
    def get_context_data(self):
        data = {"message_title" : "Website",
                "message1": "Camarines Sur National High School",
                "message": "Elementary: Tinago Central School"}
        return data

class ContactInfoPageView (TemplateView):
    template_name = "contactInfo.html"
    def get_context_data(self):
        data = {"message_title" : "Ma. Angelica O. Pujado  ",
                "message1": "Address: Lerma Naga City",
                "message2": "Email: angiepujado@gmail.com",               
                "message3": "Mobile No. 09066350801"}
        return data

