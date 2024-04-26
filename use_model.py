import pickle
from common_functions import clean_resume, get_category_by_id

classifier_model = pickle.load(open('classifier.pkl', 'rb'))
vectorizer_model = pickle.load(open('vectorizer.pkl', 'rb'))

def get_category(resume_text):
    # Clean input text
    clean_text = clean_resume(resume_text)
    
    # Re-fit vectorizer with input text
    vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
    # vectorizer.fit([clean_text])
    
    # Vectorize input text
    vectorized_text = vectorizer.transform([clean_text])
    
    # Predict category
    classifier_model = pickle.load(open('classifier.pkl', 'rb'))
    prediction_category = classifier_model.predict(vectorized_text)[0]
    prediction_category = get_category_by_id(prediction_category)    
    return prediction_category

my_resume_text = """First Last
Python Developer
WORK EXPERIENCE
______________________________________________________________________
Resume Worded, London, United Kingdom
VR gaming startup with 50+ employees and $100m+ annual revenue
Python Developer 01/2022 – Present
● Created the back-end financial systems that made 20+ RW applications
user-friendly and seamless to navigate.
● Developed and updated productivity applications, which increased user
downloads by 30% within 96 hours of release.
● Supervised programming tasks and maintained 10+ company websites with
a 50% success rate in product update deployment.
● Designed a marketing lead MySQL database that categorized and filtered
740+ leads from several sources.
Polyhire, London, United Kingdom
NYSE-listed recruitment and employer branding company
Technical Support Specialist 10/2019 – 12/2021
● Responded to and resolved 300+ customer questions about implementing
access software, CMS, IP Cameras, DVRs, and Access Control.
● Provided technical solutions for 70+ Small and Medium-sized enterprises
(SMEs) and 20+ micro-merchants, which accounted for 38% of Polyhire card
payments.
● Discovered a software glitch that prevented 150+ customers from accessing
their accounts in the first week of employment.
● Answered customers' inquiries within 60+ seconds of contact via chat
sessions and live support.
Growthsi, London, United Kingdom & Barcelona, Spain
Career training and membership SaaS with 150,000 users
Junior Software Developer 11/2018 – 09/2019
● Created a user interface as a single-page application using React and MobX;
increased the productivity of 1100+ users by 64%.
● Implemented functionality to support disconnected client machines, which
enabled 420+ customers to work offline without losing data.
● Designed a data dictionary generator that creates documentation for 1200+
developers as spreadsheets and web pages.
● Launched a search engine for consumers to search for ATM locations in 20+
states, saving institutions $50K on data research.
PREVIOUS EXPERIENCE
______________________________________________________________________
Coder, ABC Company, London, UK 06/2017 – 10/2018
Ethical Hacker, XYZ Company, New York, USA 01/2016 – 05/2017
Application Developer, ABC, New York, USA 07/2014 – 12/2015
CONTACT
__________________________
• Bradford, United Kingdom
• +44 1234567890
• first.last@gmail.com
SKILLS
__________________________
Hard Skills:
• Deep Learning
• Data Structures
• Generators
• Iterators
• Multi-Process Architecture
• Object Relational Mapping
Scripting:
• Python
• Shell
• Perl
Source Code Management
Tools:
• GitLab
• Mercurial
• Apache Subversion (SVN)
• CVS
Languages:
• English (Native)
• Romanian (Native)
• Spanish (Conversational)
EDUCATION
__________________________
Associate in Applied
Science
Computer Science
Cultural Studies
New York City, New York
10/2011 - 06/2014
OTHER
___________________________
• Certified Entry-Level Python
Programmer
• Certified Associate in Python
Programming"""

my_resume_text = my_resume_text
prediction_category = get_category(my_resume_text)
print('prediction_category: ', prediction_category)
