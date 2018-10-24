from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self):
        data = {"message_title" : "BLINK!",
                "message": "Glam!"}
        return data
    
class AboutPageView (TemplateView):
    template_name = "about.html"
    def get_context_data(self):
        data = {"message_title" : "ARMY!",
                "message": "BlackPink !"}
        return data
    

