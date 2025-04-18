from django.shortcuts import render

def home(request):
    jobs = [
        {
            "title": "Full Stack Developer",
            "company": "Amazon",
            "location": "Bangalore",
            "salary": "₹12 LPA",
            "exp": "1–3 yr Exp",
            "type": "Onsite",
            "posted": "24h Ago",
            "logo_url": "https://cdn-icons-png.flaticon.com/512/732/732229.png",
            "description1": "A user-friendly interface lets you browse stunning photos and videos",
            "description2": "Filter destinations based on interests and travel style"
        },
        {
            "title": "Node Js Developer",
            "company": "Tesla",
            "location": "Hyderabad",
            "salary": "₹12 LPA",
            "exp": "1–3 yr Exp",
            "type": "Onsite",
            "posted": "24h Ago",
            "logo_url": "https://cdn-icons-png.flaticon.com/512/5968/5968332.png",
            "description1": "Collaborate on real-time performance monitoring tools",
            "description2": "Develop efficient server-side components"
        },
        {
            "title": "UX/UI Designer",
            "company": "Swiggy",
            "location": "Mumbai",
            "salary": "₹12 LPA",
            "exp": "1–3 yr Exp",
            "type": "Onsite",
            "posted": "24h Ago",
            "logo_url": "https://cdn-icons-png.flaticon.com/512/888/888879.png",
            "description1": "Design stunning user interfaces for food delivery platforms",
            "description2": "Collaborate with developers and product teams"
        },
        {
            "title": "Full Stack Developer",
            "company": "Flipkart",
            "location": "Delhi",
            "salary": "₹12 LPA",
            "exp": "1–3 yr Exp",
            "type": "Onsite",
            "posted": "24h Ago",
            "logo_url": "https://cdn-icons-png.flaticon.com/512/919/919836.png",
            "description1": "Develop responsive web applications",
            "description2": "Integrate backend services and APIs"
        },
    ]
    return render(request, 'home.html', {'jobs': jobs})
# views.py

from django.shortcuts import render, redirect
from .models import Job

def create_job(request):
    if request.method == 'POST':
        job_title = request.POST.get('job_title')
        company_name = request.POST.get('company_name')
        location = request.POST.get('location')
        job_type = request.POST.get('job_type')
        salary_min = request.POST.get('salary_min')
        salary_max = request.POST.get('salary_max')
        application_deadline = request.POST.get('application_deadline')
        job_description = request.POST.get('job_description')

        Job.objects.create(
            job_title=job_title,
            company_name=company_name,
            location=location,
            job_type=job_type,
            salary_min=salary_min,
            salary_max=salary_max,
            application_deadline=application_deadline,
            job_description=job_description
        )
        return redirect('home')  # change 'home' to your homepage route name
    return redirect('home')
