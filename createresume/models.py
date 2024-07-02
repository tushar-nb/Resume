from django.db import models

# Create your models here.

class PersonalDetails(models.Model):
    name = models.CharField(max_length=30)
    dob = models.DateField()
    phone_number = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    address = models.TextField()
    parents_name = models.CharField(max_length=30)
    current_location = models.CharField(max_length=50)

    def __str__(self):
        return self.name 
    
class SchoolEducation(models.Model):
    school_id = models.ForeignKey(PersonalDetails, on_delete= models.CASCADE)
    school_name = models.CharField(max_length=255)
    pass_year = models.IntegerField()
    percentage = models.FloatField()
    board = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.school_name

class CollegeEducation(models.Model):
    college_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    college_name = models.CharField(max_length=255)
    pass_year = models.IntegerField()
    percentage = models.FloatField(max_length=4)
    board = models.CharField(max_length=25)
    district = models.CharField(max_length=25)
    state = models.CharField(max_length=25)

    def __str__(self):
        return self.college_name

class UniversityEducation(models.Model):
    university_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    university_name = models.CharField(max_length=100)
    pass_year = models.IntegerField()
    percentage = models.FloatField(max_length=4)
    course = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.university_name

class Skill(models.Model):
    skill_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    programming_languages = models.CharField(max_length=255)
    technologies = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.programming_languages}, {self.technologies}"

class Project(models.Model):
    project_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    domain = models.CharField(max_length=100)
    technologies_used = models.CharField(max_length=255)

    def __str__(self):
        return self.project_name

class Experience(models.Model):
    experience_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, blank=True, default='')
    role = models.CharField(max_length=100, blank=True, default='')
    duration = models.CharField(max_length=100, blank=True, default='')
    technologies_worked_on = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return f"{self.company_name} - {self.role}"

class Hobby(models.Model):
    hobby_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    hobby = models.CharField(max_length=255)

    def __str__(self):
        return self.hobby
