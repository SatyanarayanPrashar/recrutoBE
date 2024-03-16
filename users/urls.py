from django.urls import path
from .views import UserView, AllUsers, UserProfileCreateAPIView

urlpatterns = [
    path('', UserProfileCreateAPIView.as_view(), name='user-create'),
    path('all/', AllUsers.as_view(), name='all-users'),
    path('<str:g_token>/', UserView.as_view(), name='user-detail'),
] 


# {
#     "user_id": 4,
#     "g_token": "p3Aze3KHc2RUC3rKCT965xYsGAy2",
#     "full_name": "Satyanarayan Prashar",
#     "profile_photo": "NA",
#     "location": "Banglore, In",
#     "preferred_roles": "Software Engineer",
#     "bio": "To work with the bests, and learn from them while leveraging my programming and organisational skills to contribute to the prosperity of the organization.",
#     "portfolio_link": "https://example.com/portfolio",
#     "linkedin_link": "https://www.linkedin.com/in/satyanarayan-prashar-57a170229/",
#     "github_link": "https://github.com/SatyanarayanPrashar",
#     "anyother_link": "https://example.com/other",
#     "exp_title": "Product Manager Intern",
#     "exp_company": "TreeVed",
#     "exp_description": "Created strategy, and roadmap for the product based on Market Research and resources available • Leaded the development team working with NextJS, Django Rest FrameWork, AWS and Azure • Created required wire frames for designs and documents using tools Figma, Slack • Executed Market Research and User Feedback in various online communities",
#     "project_title": "Edloops",
#     "project_link": "https://edloops.com",
#     "project_description": "• Created an innovative EdTech platform for curating learning materials and building courses • Utilized Next.js Framework and Firebase for authentication • Utilized Django Rest Framework for building robust RESTful APIs to interact with the frontend • Implemented Redux for centralized state management, ensuring data consistency across components • Deployed the application on an EC2 instance within the AWS cloud environment for scalability and reliability",
#     "skills": "C++, NextJS, ReactJs, HTML, CSS, JavaScript, Python, Django, AWS"
#   },