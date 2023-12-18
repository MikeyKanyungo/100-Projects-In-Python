from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os 

class generator: 
  def __init__(self, title, author, description, keywords, pdf_name):
    self.title = title
    self.author = author
    self.template = """ 
    [Full Name: ]
    [Address: ]
    [Phone number: ] | [Email: ]
    
    [Objective: ]
    [Supplementary Information: ]

    [Education: ]
    [Experience: ]
    [Skills: ]

    [References: ]
    """	

    self.cv_data = {
      "Full Name": author,
      "Address": "Address",
      "Phone number": "Phone number",
      "Email": "Email",
      "Objective": "Objective",
      "Supplementary Information": "Supplementary Information",
      "Education": "Education",
      "Experience": "Experience",
      "Skills": "Skills",
    }

  def add_cv_data(self):
    self.cv_data["Full Name"] = input("Enter your full name: ")
    self.cv_data["Address"] = input("Enter your address: ")
    self.cv_data["Phone number"] = input("Enter your phone number:")
    self.cv_data["Email"] = input("Enter your email: ")

  def get_object(self):
    self.cv_data["objective: "] = input("Enter your objective: ")

  def get_summary(self):
    full_name = self.cv_data["Full Name"]
    address = self.cv_data["Address"]
    phone_number = self.cv_data["Phone number"]
    self.cv_data["Supplementary Information"] = input("Enter your supplementary information: ")

  def get_education(self):
    num_education = int(input("Enter the number of educations: "))
    for i in range(num_education):
      certification = input("Enter certification: ")
      institution = input("Enter the institution: ")
      graduation_year = input("Enter the graduation year: ")
      self.cv_data["Education"] += f"{certification} at {institution} ({graduation_year})\n"

  def get_experience(self):
    num_experience = int(input("Enter the number of experiences: "))
    for i in range(num_experience):
      company = input("Enter the company: ")
      position = input("Enter the position: ")
      start_year = input("Enter the start year: ")
      end_year = input("Enter the end year: ")
      self.cv_data["Experience"] += f"{company} ({position}) ({start_year} - {end_year})\n"

  def get_skills(self):
    num_skills = int(input("Enter the number of skills: "))
    for i in range(num_skills):
      skill = input("Enter the skill: ")
      self.cv_data["Skills"] += f"{skill}\n"

  def generate_pdf(self):
    pdf_name = os.path.abspath("{self.title}.pdf")
    cv = self.template
    for field, value in self.cv_data.items():
        cv = cv.replace(f"[{field}]", value)

    c = canvas.Canvas(pdf_name, pagesize=letter)
    width, height = letter
    lines = cv.split('\n')
    line_height = 14 

    for i, line in enumerate(lines):
      c.drawString(100, height - 100 - 1 * line_height, line)

    c.save()
    print (f"Your CV is ready. PDF saved as: {pdf_name}")

if __name__ == "__main__":
    cv_generator = generator("Title", "Your Name", "Description", "Keywords", "output_pdf")
    cv_generator.add_cv_data()
    cv_generator.get_object()
    cv_generator.get_summary()
    cv_generator.get_education()
    cv_generator.get_experience()
    cv_generator.get_skills()

    generated_pdf = f"{cv_generator.title}.pdf"

    print("Your CV is ready.")