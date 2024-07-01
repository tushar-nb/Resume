from django.shortcuts import render
from django.http import HttpResponse
from createresume.models import *
from editresume.templates import *
from datetime import datetime



# Create your views here.
def EditResume(request, id):
    try:
        personalDetails = PersonalDetails.objects.get(id = id)
        schoolEducation = SchoolEducation.objects.get(school_id = id)
        collegeEducation = CollegeEducation.objects.get(college_id = id)
        universityEducation = UniversityEducation.objects.get(university_id = id)
        skill = Skill.objects.get(skill_id = id)
        project = Project.objects.get(project_id = id)
        experience = Experience.objects.get(experience_id = id)
        hobby = Hobby.objects.get(hobby_id = id)
    except:
        return HttpResponse("<h2>No such id exists</h2>")
    
    dict = {
        'personalDetails': personalDetails,
        'schoolEducation': schoolEducation,
        'collegeEducation': collegeEducation,
        'universityEducation': universityEducation,
        'skill': skill,
        'project': project,
        'experience': experience,
        'hobby': hobby   
    }
    
    return render(request,'editresume/edit.html', dict)

def UpdateData(request, id):
    #NEW DATA
    updated = request.POST
    
    try:
        personalDetails = PersonalDetails.objects.get(id = id)
        schoolEdu = SchoolEducation.objects.get(school_id = id)
        collegeEdu = CollegeEducation.objects.get(college_id = id)
        universityEdu = UniversityEducation.objects.get(university_id = id)
        skill = Skill.objects.get(skill_id = id)
        project = Project.objects.get(project_id = id)
        experience = Experience.objects.get(experience_id = id)
        hobby = Hobby.objects.get(hobby_id = id)
    except:
        return HttpResponse("<h2>No such id exists</h2>")
        
    personalDetails.name = updated['name']
    personalDetails.dob = datetime.strptime(updated['dob'], '%Y-%m-%d')
    personalDetails.phone_number = updated['phNumber']
    personalDetails.gender = 'male' if updated['gender'] == 'male' else 'female'
    personalDetails.address = updated['address']
    personalDetails.parents_name = updated['parent_name']
    personalDetails.current_location = updated['current_location']
    personalDetails.save()
    
    
    schoolEdu.school_name = updated['school_name']
    schoolEdu.pass_year = int(updated['school_passout'])
    schoolEdu.percentage = updated['school_percentage']
    schoolEdu.board = updated['school_board']
    schoolEdu.district = updated['school_district']
    schoolEdu.state = updated['school_state']
    schoolEdu.save()
    
    
    collegeEdu.college_name = updated['college_name']
    collegeEdu.pass_year = int(updated['college_passout'])
    collegeEdu.percentage = updated['college_percentage']
    collegeEdu.board = updated['college_board']
    collegeEdu.district = updated['college_district']
    collegeEdu.state = updated['college_state']
    collegeEdu.save()
    
    
    universityEdu.university_name = updated['university_name']
    universityEdu.pass_year = int(updated['university_passout'])
    universityEdu.percentage = updated['university_percentage']
    universityEdu.course = updated['university_course']
    universityEdu.branch = updated['university_branch']
    universityEdu.district = updated['university_district']
    universityEdu.state = updated['university_state']
    universityEdu.save()
    
    skill = Skill.objects.get(skill_id = id)
    skill.programming_languages = updated['programming_language']
    skill.technologies = updated['technologies']
    skill.save()
    
    
    project.project_name = updated['project_name']
    project.domain = updated['project_domain']
    project.technologies_used = updated['project_technologies']
    project.save()
    
    
    experience.company_name = updated['company']
    experience.role = updated['role']
    experience.duration = updated['duration']
    experience.technologies_worked_on = updated['exp_technologies']
    experience.save()
    
    
    hobby.hobby = updated['hobbies']
    hobby.save()
    
    return render(request, 'editresume/updateSuccess.html')