from django.shortcuts import render
from django.http import HttpResponse
from createresume.templates import *
from createresume.models import *

# Create your views here.
def Create(request):
    return render(request,'createresume/create.html')

def Success(request):
    dict  = request.POST
    
    personal = PersonalDetails(
        name = dict['name'],
        dob = dict['dob'],
        phone_number = dict['phNumber'],
        gender = dict['gender'],
        address = dict['address'],
        parents_name = dict['parent_name'],
        current_location = dict['current_location']
    )
    personal.save()
    
    school = SchoolEducation(
        school_id = personal,
        school_name = dict['school_name'],
        pass_year = dict['school_passout'],
        percentage = dict['school_percentage'],
        board = dict['school_board'],
        district = dict['school_district'],
        state = dict['school_state']
    )
    school.save()
    
    college = CollegeEducation(
        college_id = personal,
        college_name = dict['college_name'],
        pass_year = dict['college_passout'],
        percentage = dict['college_percentage'],
        board = dict['college_board'],
        district = dict['college_district'],
        state = dict['college_state']
    )
    college.save()
    
    university = UniversityEducation(
        university_id = personal,
        university_name = dict['university_name'],
        pass_year = dict['university_passout'],
        percentage = dict['university_percentage'],
        course = dict['university_course'],
        branch = dict['university_branch'],
        district = dict['university_district'],
        state = dict['university_state']
    )
    university.save()
    
    skill = Skill(
        skill_id = personal,
        programming_languages = dict['programming_language'],
        technologies = dict['technologies']
    )
    skill.save()
    
    project = Project(
        project_id = personal,
        project_name = dict['project_name'],
        domain = dict['project_domain'],
        technologies_used = dict['project_technologies']
    )
    project.save()
    
    experience = Experience(
        experience_id = personal,
        company_name = dict['company'],
        role = dict['role'],
        duration = dict['duration'],
        technologies_worked_on = dict['exp_technologies']
    )
    experience.save()
    
    hobby = Hobby(
        hobby_id = personal,
        hobby = dict['hobbies']
    )
    hobby.save()

    return render(request, 'createresume/goToHome.html')