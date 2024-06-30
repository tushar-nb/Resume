from django.http import HttpResponse
from django.shortcuts import redirect, render
from listresume.templates import *
from createresume.models import *
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
def ListResume(request):
    objects = PersonalDetails.objects.all()
    items = []
    for obj in objects:
        items.append(
            {
                'id' : obj.id,
                'title' :  obj.name +", "+ str(obj.dob)
            }
        )
    
    return render(request,'listresume/list.html', {'items': items})

def DeleteResume(request, id):
    obj = PersonalDetails.objects.get(id=id)
    obj.delete()
    return redirect('/listresume')
    
def ViewResume(request, id):
    personalDetails = PersonalDetails.objects.get(id = id)
    schoolEdu = SchoolEducation.objects.get(school_id = id)
    collegeEdu = CollegeEducation.objects.get(college_id = id)
    universityEdu = UniversityEducation.objects.get(university_id = id)
    skill = Skill.objects.get(skill_id = id)
    project = Project.objects.get(project_id = id)
    experience = Experience.objects.get(experience_id = id)
    hobby = Hobby.objects.get(hobby_id = id)
    
    context = {
        'name': personalDetails.name,
        'dob': personalDetails.dob,
        'phNumber': personalDetails.phone_number,
        'gender': personalDetails.gender,
        'address': personalDetails.address,
        'parents_name': personalDetails.parents_name,
        'current_location': personalDetails.current_location,
        'school_education': {
            'school_name': schoolEdu.school_name,
            'pass_year': schoolEdu.pass_year,
            'percentage': schoolEdu.percentage,
            'board': schoolEdu.board,
            'district': schoolEdu.district,
            'state': schoolEdu.state
        },
        'college_education': {
            'college_name': collegeEdu.college_name,
            'pass_year': collegeEdu.pass_year,
            'percentage': collegeEdu.percentage,
            'board': collegeEdu.board,
            'district': collegeEdu.district,
            'state': collegeEdu.state
        },
        'university_education': {
            'university_name': universityEdu.university_name,
            'pass_year': universityEdu.pass_year,
            'percentage': universityEdu.percentage,
            'course': universityEdu.course,
            'branch': universityEdu.branch,
            'district': universityEdu.district,
            'state': universityEdu.state
        },
        'skills': {
            'programming_languages': skill.programming_languages,
            'technologies': skill.technologies
        },
        'projects': [
            {
                'project_name': project.project_name,
                'domain': project.domain,
                'technologies_used': project.technologies_used
            },
        ],
        'experience': [
            {
                'company_name': experience.company_name,
                'role': experience.role,
                'duration': experience.duration,
                'technologies_worked_on': experience.technologies_worked_on
            },
        ],
        'hobbies': hobby.hobby,
    }
    return render_to_pdf('listresume/viewresume.html', context)

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    pisa_status = pisa.CreatePDF(
       html, dest=response
    )
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response