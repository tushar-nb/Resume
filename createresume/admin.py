from django.contrib import admin

from createresume.models import CollegeEducation, Experience, Hobby, PersonalDetails, Project, SchoolEducation, Skill, UniversityEducation

# Register your models here.

admin.site.register(PersonalDetails)
admin.site.register(SchoolEducation)
admin.site.register(CollegeEducation)
admin.site.register(UniversityEducation)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Hobby)

