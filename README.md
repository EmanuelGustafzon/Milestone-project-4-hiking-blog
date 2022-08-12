# HikeIt Django Full Stack Portfolio Project!
HikeIt is a blog for hikers and adventures people who likes to travel and would like to get up and see the amazing views from different mountains around the world. The blog is designed to inspire and inform about hiking. The content covers tips and practical information for hiking in general and different specific places. The users are also supposed to engage with the blog. That is why the users can like and comment the different posts so that they can share useful information and show other users and the administrator what content they like.
## Site link goes here.

## Design Thinking

 - Purpose of the blog
   - I think that there is many people out there who is looking for a solid blog where you can find many tips when it comes to hiking and at the same time a blog with a beautiful design and unique character that people can interact with.

 - Persona.
   - let us dive into the projects persona. The persona is named Stephanie, She is 26 years old and is working full time with a quit good salary. She is single and cannot be still for to long. She likes adventures and to discover new places. She works to save money for her next trip because she loves travelling and she wants to discover the world as much as she can before she sattle down and having a family. 

 - The design.
   - When I designed this blog I wanted it to look inspiring, trustworthy and playful. I thought that those factors where key thing for the persona Stephanie to like the page. I choosed the typography Kalam as it looks handwritten and playful. I styled the cards and images with round corners and a dropshadow to create that same effect. I choosed blue colors as I think they are soft and give the user an inpression of trustworthyness and seriousness but in the same time the colors really fit the style. The images are unique and not from the intrenet as I think that is the kind of images that gives character and can inspire the user.

   ## User Experience

- User stories

  - As an Administrator I can create drafts so that I can finish the content later.
  - As a User I can Update Comments so that I can Correct something that is wrong.
  - As a Administrator I can create, edit and delete posts so that I can **manage the blog's content **
  - As a User I can Delete comments so that I can change my mind about a comment.
  - As a Admin I can approve and disapprove comments so that I can Get rid of spam comments.
  - As a User I can view posts so that I can read the content
  - As a User I can view other users comments so that I can hear other users point of view.
  - As a User I can view how many likes a post have so that I can see what content other users likes.
  - As a User I can register an account and login so that I can like and comment posts.
  - As a User I can Comment on the posts so that I can Share my experience and inputs with the community
  - As a User I can Like posts so that I can Share ith the community what kind of content I enjoy.

- UX Improvements
  - At the moment a user cannot search in the blog. This can result to poor user experience as it can be hard for the user to find a specific content.
  - When a user wants to delete or update a commet thet get redirected to the home page and not the previous slug they came from. This couses confusion because it is hard to know if the comment really updated or got deleted. 


## Agile Methodology

- When developing this webapplication I used Agile Methodology. I planned my work based on user stories and a project board where I gave them a status of todo, in progress or done. All this was made in GitHub projects. During this project I had a tight deadline and when we work with agile as methodology we never comprimise time or quality but the scope. The features I did not get to do now I added as "future features" in the project board. Check it out here: https://github.com/users/EmanuelGustafzon/projects/4/views/1.

 ## Blog Features 

    - Responsive navigation 

 ![feature nav desktop](/assets/images/IMG-2447.jpg)
 ![feature nav mobile](/assets/images/IMG-2446.jpg)

 - Comment section

   - comment not signed in

 ![feature comment not signed in](/assets/images/IMG-2435.jpg)

   - comment wait approvel

 ![feature comment wait approval](/assets/images/IMG-2441.jpg)

  - delete update comments

 ![feature update comment](/assets/images/IMG-2442.jpg)
 ![feature update and delete comments](/assets/images/IMG-2443.jpg)
 ![feature confirm delete comment](/assets/images/IMG-2445.jpg)

   - login, out register

 ![feature sign out](/assets/images/IMG-2444.jpg)
 ![feature sign up](/assets/images/IMG-2439.jpg)
 ![feature sign in](/assets/images/IMG-2440.jpg)
 

   - Home Page

 ![feature Home page](/assets/images/IMG-2436.jpg)

   - Detail Page

 ![feature Detail page](/assets/images/IMG-2434.jpg)

  - About page

 ![feature About page](/assets/images/IMG-2438.jpg)

   - pegnation

 ![feature pegnation next](/assets/images/IMG-2437.jpg)
 ![feature pegnation prev](/assets/images/IMG-2433.jpg)

 ## Admin Features 

   - post

 ![feature post](/assets/images/Sk%C3%A4rmbild%20(174).png)
 ![feature post](/assets/images/Sk%C3%A4rmbild%20(175).png)
 ![feature post](/assets/images/Sk%C3%A4rmbild%20(176).png)
 

   - comment

 ![feature post](/assets/images/Sk%C3%A4rmbild%20(177).png)

   - people access to admin panal.

 ![feature post](/assets/images/Sk%C3%A4rmbild%20(178).png)

  ## Technologies

- Languages used
  - HTML 5
  - CSS 3
  - Javascript
  - Python

- Databases
  - Postgresql
    - As database in Heroku
  - SQLite
    - Used for automatic tests.

- Frameworks
  - Bootstrap
  - Django

- Django Extentions
  - Allauth
  - Summernote
  - Django-Crispyforms
  - Django-Copyright

- Tools for design
 - Coolors
 - Font Awsome
 - Google Fonts


Cloud storage and deployment services

    Cloudinary
    Heroku
    Gunicorn


  ## Testing 

 - All the testing goes here.

  ## Bugs 

- Solved
  - solved goes here
  
- Unsolved
  - unsolved bugs goes here

  ## Other Featured that can be implemented
   
- improvements of code goes here.

  ## Deployment 

Initial Deployment:

- Step One, install django and packages with these commands:
  - pip3 install 'django<4' gunicorn
  - pip install dj_database_url psycopg2
  - pip3 install dj3-cloudinary-storage
  - pip3 freeze --local > requirements.txt
  - django-admin startproject "project_name".
  - python3 manage.py startapp "app_name"
  - pip3 install django-crispy-forms
  - Migrate the work using:
    - python3 manage.py makemigrations --dry-run
    - python3 manage.py makemigrations
    - python3 manage.py migrate --plan
    - python3 manage.py migrate
  - Now, type the commend python3 manage.py runserver to see the preview It should say that django installed successfully.

- Env.py file. 
  - Add Cloudinary API variable, postgres DATABASE_URL and SECRET_KEY.
  - Make sure env.py is in the gitignore-file
  - Commit all changes to GitHub.
    - git add .
    - git commit -m "commit message."
    - git push

- Set up delpoyment with Heroku:
  - Register and login to Heroku.
  - Create an app with a unique name and choose the region that is closest to you, USA or Europe.
  - In Heroku/app/resources add postgres and attach it to the database url.
  - Under Settings-> Config vars:
    - I used Cloudinary to store images so I added my personal Cloudniery API variable.
    - add DISABLE_COLLECTSTATIC, this is to prevent accidentally showing debug messages while DEBUG is True in settings.py
    - Add port 8000
    - Add SECRET_KEY from the env.py file.
  - Under Deploy choose deployment methods Github and search for my repo.
  - The branch to deploy should be set to main.
  - Deploy branch


- Login to Heroku in terminal if needed.
  - heroku login -i
   - Provide Heroku username, email and password.
  - heroku run python3 manage.py migrate --app APP_NAME

- The usage of two databases.
 - For this project I used PostgrSQL as the satabase for deployment but when I did the automatic testings I needed to use djangos default database, LiteSQL.
 
  - Create an if else statement for the databases:
   - if 'DEVELOPMENT' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
 - Set DEBUG = 'DEVELOPMENT' in os.environ
- In env.py add os.environ['DEVELOPMENT'] = 'True'
- Migrate those changes and push them to github.
- Remove DISABLE_COLLECTSTATIC in heroku config vars.

  ## Credits 
- The documentation from Code Institute
- DjangoCentral https://djangocentral.com/building-a-blog-application-with-django/
- Medium.com https://towardsdatascience.com/build-a-django-crud-app-by-using-class-based-views-12bc69d36ab6
- StackOverFlow
- Bootsrtap Documentation https://getbootstrap.com/docs/5.0/getting-started/introduction/