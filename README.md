# Care Management System (CMS)
A subsection of Complete Care Portal (CCP)

## A Care Notes Management System primarily for carers.
### CMS manages notes about clients that have been assigned to carers. Allowing access for review and update in situ.

The responsive website allows registered users to create blog posts (journal entries) and a profile with thier bio and a photo. Users who are not registered are free to browse the posts. To make it easy to find content for you, users can filter blog posts by author or country.  

# **[Link to Live Site](https://client-management-system-8d776b4f8b61.herokuapp.com/cms/)**  

*This a the final FullStack Bootcamp (Berks) project for the Code Institue.*  

**Built by Duncan Thow**

---

# Table of Contents  

 1. [ UX ](#ux)
 2. [ Agile Development ](#agile-development)
 3. [ Features implemented ](#features-implemented)  
 4. [ Features Left to Implement ](#features-left-to-implement)  
 5. [ Technology used ](#technology-used) 
 6. [ Testing ](#testing-and-Validation)  
 7. [ Bugs ](#known-bugs)  
 8. [ Deployment](#deployment)
 9. [ Resources ](#resources)  
 10. [ Credits and acknowledgements ](#credits-and-acknowledgements)

---

# UX

## Database Planning

Due to a refocusing halfway through my final project (which will be expanded upon under Agile Development) my original database entity relationship diagrams (hereinafter refered to as ERD's).  While I have a 'register' feature on the CMS this does not automatically create a new user.  A site admin must grant a user the correct access rights ('carer') to ensure client medical details data security.  The 'register' feature can also double as an input field for a logged in carer but they will not be able to access the client unless it is assigned and this may not be to the carer who created this entry.
![CMS ERD current]("/static/readme/images/CMS ERD 2.png")

## UX Design

### Overview
Sojourn Scribbles is envisioned as a modern, vibrant, and inclusive platform tailored specifically for solo female travelers. The UX design focuses on creating an engaging and welcoming environment that reflects the spirit of exploration and camaraderie. With a fun and feminine aesthetic, the site aims to foster connections, inspire wanderlust, and celebrate the diverse experiences of solo female travelers.

### Site User
The primary users of Sojourn Scribbles are solo female travelers from diverse backgrounds and ages, each with their own unique travel stories and perspectives. These users seek a supportive and inclusive community where they can share their adventures, seek advice, and connect with others who share their passion for exploration. They value authenticity, empathy, and the opportunity to engage with like-minded individuals in a safe and welcoming space.

### Goal
Sojourn Scribbles aims to empower solo female travelers by providing a platform where they can share their experiences, find inspiration for future trips, and build meaningful connections with fellow adventurers. Through authentic storytelling, travel tips, and community engagement, the site strives to create a supportive environment where users feel encouraged to share their stories, seek advice, and support one another in their journeys. The goal is to cultivate a vibrant and inclusive community that celebrates the strength, resilience, and spirit of solo female travelers, while also providing valuable resources and inspiration for their adventures.


## Wireframes

I used Balsamiq to create my wireframes. The final product looks a bit different to original intentions but served as a good guide nonetheless. The wireframes contain a lot of detail about the future vision and long term plan for Sojourn Scribbes with future features. These features were not possible due to the scope of the current project for the time contrainsts given. 

![Plan overview](/static/images/readme/Plan.png)

The origional intention was for the profile section, posts and reccomendations (future feature) to all be on the same page. Upon review this would have been overloading the page a bit.

![Home page wireframe](/static/images/readme/Home.png)

After reassessing that set up I created another wireframe for the profile page - the final structure of this is slightly differnt in that the two sections are stacked horizontally not vertically.

![Profile wireframe](/static/images/readme/Profile.png)

Next we have the navbar and footer - the end product of both turned out nearly the same as the wireframe with just the filter function seperated from the navbar since it wouldn't be relevant for all pages.

![Navbar and footer wireframe](/static/images/readme/NavFoot.png)

##### [ Back to Top ](#table-of-contents)

# Agile Development

For the development of Sojourn Scribbles, I adopted an Agile methodology to ensure iterative and efficient progress throughout the project lifecycle. Central to this approach was the utilization of a Kanban board hosted on GitHub Projects. You can view the project board [here](https://github.com/users/katiejanecoughlan/projects/2).

## Kanban Board Overview

The Kanban board served as a visual representation of the project's progress and allowed for effective task management. It consisted of the following sections:

- **Backlog:** This section contained all the tasks and user stories that were yet to be prioritized for implementation.
- **Ready:** Tasks and user stories ready for development were moved to this column.
- **In Progress:** Work in progress was tracked here, indicating tasks actively being worked on.
- **In Review:** Upon completion, tasks were moved here for review before being marked as done.
- **Done:** Tasks that were completed successfully were moved to this column.
- **Future Features:** Ideas and tasks earmarked for future development were kept in this section for consideration in subsequent iterations.

### User Stories Integration

User stories played a pivotal role in shaping the development process, ensuring that features were aligned with user needs. These user stories were mapped onto the Kanban board, guiding the prioritization and implementation of tasks. 

### Task Management

In addition to tracking user stories, the Kanban board served as a comprehensive task list. I utilized it to break down user stories into smaller, actionable tasks, ensuring clear and manageable objectives for development. This granular approach facilitated efficient progress tracking and enhanced team collaboration.

By leveraging Agile principles and utilizing the Kanban board effectively, the development of Sojourn Scribbles remained focused, adaptable, and responsive to evolving requirements, resulting in a more robust and user-centric Django blog application.


## User Stories Overview

1. **Title:** Implement User Registration
   - As a **user**, I can **register for an account** on Sojourn Scribbles so that **I can create and share my travel experiences with others**.

2. **Title:** Enable User Authentication
   - As a **registered user**, I can **log in** to my account on Sojourn Scribbles so that **I can access personalized features and interact with other users**.

3. **Title:** Create Journal Entry Form
   - As a **user**, I can **create journal entries** to document my travel experiences on Sojourn Scribbles so that **I can share my adventures with the community**.

4. **Title:** Display Journal Posts
   - As a **user**, I can **view journal posts** created by other users on Sojourn Scribbles so that **I can discover new travel destinations and gain inspiration for my own trips**.

5. **Title:** Create Comment Functionality
   - As a **user**, I can **comment on posts** on Sojourn Scribbles so that **I can engage with other users and discuss our experineces**.

6. **Title:** Create Profile Page
   - As a **user**, I can **create a profile** with a bio and my photo **I can save and edit my profile to customize my journal**.

7. **Title:** Integrate Cloudinary API for Image Hosting
   - As a **user**, I can **upload my travel images** to the Cloudinary API on Sojourn Scribbles so that **I can enhance my journal entries with visually appealing content**.

##### [ Back to Top ](#table-of-contents)

# Features Implemented

## Home Page:
  - Blog posts are displayed as cards.
  - Filters (user and country) functionality allows users to filter posts.
  - Users can click on a blog card to read the entire post.
  - Commenting functionality allows users to comment on blog posts.
  - Users can edit and delete their own comments.
  - Users must be logged in to comment, edit, or delete comments.
  - Users must be logged in to delete their own blog posts.
  - Users cannot delete or edit blog posts or comments created by other users.
  - Comments require admin approval.

## About Page:
  - Provides an overview of Sojourn Scribbles and its aims.
  - Includes a feedback form for users to share their feedback.
  - Accessible without the need for user authentication.

## Footer/Nav Bar:
  - Navigation links facilitate easy navigation throughout the website.
  - Social media links direct users to Sojourn Scribbles' social media pages.

## Profile Page:
  - Access requires user authentication.
  - Users can edit their profile information (bio and title).
  - Profile editing is done through a form toggled by an "Edit Profile" button.
  - Users can create blog posts, including uploading images.
  - After submitting a post, users are redirected to the home page to view their published post.

## Login Page:
  - Secure signup functionality allows users to register securely.
  - Successful login redirects users to the home page.

## Registration Page:
  - Secure login functionality allows users to log in securely.
  - Successful registration redirects users to the home page.

## Logout Page:
  - Logout functionality allows users to sign out securely.
  - After successful logout, users are redirected to the home page.

### Responsive Design:

   - The website is designed to be responsive, ensuring optimal usability across various screen sizes.
   - Navbar collapses into a burger bar for improved navigation on smaller screens.
   - Masthead images are omitted from individual blog posts on smaller screens to enhance readability and aesthetics.

## Additional Security Features:

   - Prevention of brute force actions via URL.
   - Users are redirected to the sign-in page with an unauthorized action notification if they attempt unauthorized actions.
   - Prevention of users deleting other users' posts.
   - Prevention of users posting as other users.

##### [ Back to Top ](#table-of-contents)

# Future Features

- **Community Engagement:**
  - Implement a user interaction feature where users can follow each other, fostering a sense of camaraderie and enabling content discovery within the community.
  - Enable users to view each other's profiles, facilitating connections and allowing users to learn more about fellow travelers' interests and experiences.
  - Provide users with a log of their published posts on their profile page, promoting self-reflection and making it easier for users to revisit their past contributions.

- **Enhanced Recommendations:**
  - Introduce a recommendations section within posts, allowing users to share travel tips and insights with the community, enhancing the platform's value as a travel resource.
  - Enable users to save recommendations for future reference, creating personalized collections of travel advice tailored to their interests and preferences.
  - Utilize the Google Maps API to enrich the recommendations section, offering users visual representations of recommended locations and aiding in travel planning.

- **Improved Search Functionality:**
  - Implement a search bar to empower users to find specific content on the website, improving usability and content discoverability.
  - This feature expands the navigation options beyond existing filters, providing users with greater flexibility in exploring the diverse content available on the platform.

- **Improved UX:**
  - Introduce a landing page that serves as a log in/register page and contains info about Sojourn Scribbles to provide the user more immediately with a clear call to action and purpose for the website.  
  - The user would be directed to this page when they click to the website as opposed to the current home page post feed. 

##### [ Back to Top ](#table-of-contents)

# Technology Stack

- HTML - for page structure
- CSS - for custom styling
- Python - for the backend
- Javascript - for event listeners on buttons
- Django - framework used to build this project
- Jinja - templating language rendering logic within html documents
- Bootstrap 5 - front end framework used for styling
- Heroku PostgreSQL - used as the database
- Balsamiq - for wireframes
- Canva - for creating assets
- Font Awesome - for social media icons
- Lucidchart - for database ER diagrams
- Gencraft - for AI images
- Pexels - for free stock images
- Google Fonts- for custom font styling
- GitHub - for storing the code and for the Kanban board
- Heroku - for hosting and deployement of this project
- Cloudinary - hosting the static files 
- Git - for version control

##### [ Back to Top ](#table-of-contents)

# Testing and Validation

## Responsiveness

I used the dev tools on chrome to test the website for responsiveness. I captured screenshots to demonstrate responsive design across mobile, tablet and laptop based on the size configurations preset in dev tools.  
Some particular features to note:
-- Navbar collapses to a burger bar on smaller screen sizes
-- There is no image in the masthead within a blog post on smaller screen sizes
-- Content stacks vertically instaed of horizonstally on smaller screen sizes
-- The smaller the screen the less blog post cards visible on the home page

### The Profile Page

**Laptop**
![Screenshot of profile page view on laptop](/static/images/readme/lappro.png)

**Tablet**
![Screenshot of profile page view on tablet](/static/images/readme/tabpro.png)

**Mobile**
![Screenshot of profile page view on mobile](/static/images/readme/mobpro.png)

### Other Examples

**Laptop**
![Screenshot of about page view on laptop](/static/images/readme/lapabo.png)

**Tablet**
![Screenshot of a post view on tablet](/static/images/readme/tabpos.png)

**Mobile**
![Screenshot of the home page view on mobile](/static/images/readme/mobhom.png)

## Testing and Validation
- I used the [W3 HTML Validator](https://validator.w3.org/#validate_by_input+with_options) to check the HTML on each of my site pages by Direct Input. I have resolved the necessary errors (extra </div> tags and correcting how width is set in an img tag). *However* there are some error messages remaning which are due to the content being created using Django Summernote editor in the admin panel.  
  
- I used the [W3 CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) to check my CSS script by Direct Input. I found no errors! There are 5 warnigns which are just flagging vendor extensions.

![CSS validation results](/static/images/readme/css.png)  
  
- I used the [CI Python Linter](https://pep8ci.herokuapp.com/) to check all my python scripts. I found a few small errors like the below - mostly lines were too long or there was a missing blank space line. I have left some of the error messages as they are related to a too long line at the result of a comment.

![Python Linter Result](/static/images/readme/linter.png)

- I also used the Django automated testing within my Gitpod workspace. 

### Manual Testing Results

### HOME PAGE

| Test                                     | Result |
|-----------------------------------------|--------|
| Blog posts displayed as cards           | Pass   |
| Filters (user and country) functionality| Pass   |
| Ability to click on a blog card         | Pass   |
| Commenting functionality                | Pass   |
| Edit and delete comment functionality   | Pass   |
| User must be logged in to comment/edit/delete | Pass |
| User must be logged in to delete blog post  | Pass |
| User cannot delete/edit others' comments | Pass |
| Comments require admin approval         | Pass   |
| Prevention of deleting other users' posts  | Pass   |
| Prevention of posting as other users        | Pass   |

### ABOUT PAGE

| Test                                     | Result |
|-----------------------------------------|--------|
| Overview of Sojourn Scribbles           | Pass   |
| Feedback form functionality             | Pass   |
| Accessible without login                | Pass   |

### FOOTER/NAV BAR

| Test                                     | Result |
|-----------------------------------------|--------|
| Navigation links functionality          | Pass   |
| Social media links functionality        | Pass   |

### PROFILE PAGE

| Test                                     | Result |
|-----------------------------------------|--------|
| Access requires login                   | Pass   |
| Edit profile form functionality        | Pass   |
| Post creation functionality             | Pass   |
| Redirect after post submission          | Pass   |

### LOGIN PAGE

| Test                                    | Result |
|----------------------------------------|--------|
| Secure signup functionality            | Pass   |
| Redirect after successful login        | Pass   |

### REGISTRATION PAGE

| Test                                    | Result |
|----------------------------------------|--------|
| Secure login functionality             | Pass   |
| Redirect after successful registration | Pass   |

### LOGOUT PAGE

| Test                                    | Result |
|----------------------------------------|--------|
| Logout functionality                   | Pass   |
| Redirect after successful logout       | Pass   |

### SECURITY

| Test                                                             | Result |
|-----------------------------------------------------------------|--------|
| Prevention of brute force actions via URL                        | Pass   |
| Redirect to sign-in page after attempted unauthorized action | Pass   |
  
![Redirect after brute force attempt](/static/images/readme/bruteforce.png)

##### [ Back to Top ](#table-of-contents)

# Known Bugs

- **There is a bug with alert message in the profiles view.**  
The error message for the PostForm is not working as expected BUT thanks to the power of Django the user still receives red error messages within the form itself.  
The ProfilesForm success message was incorrectly displaying when there was an error submitting the PostForm. To avoid confusion for the user, until the bug is resolved I have turned off that alert message.  
  
![Alert message error](/static/images/readme/ealert.png)


- **There is a bug with handling input from Django Summernote to the Profile Form.**
 If you fill in the Profile Form from the admin panel the output is rendered with all of the coding tags visible and not formatted.  
 Thanks to Django, the users don't have access to the admin panel and can only create their profile from the form on the website so it is not posssible for them to experience this bug!
 ![Summernote Error](/static/images/readme/esummernote.png)

 - **There is a bug with the favicon site.webmanifest file**
 The below console error messages are related to the site.webmanifest file for my favicon. I tested removing the link to this file at the top of my base.html and the console was free of errors. However, based on some research I have decided to leave the file in because it's crucial for Progressive Web Apps (PWAs), providing essential metadata such as the application's name, icons, theme colors, and display mode to browsers. However, potential bugs or unexpected behavior may arise due to syntax errors, misconfigurations, or conflicts with other components. Acknowledging these issues emphasizes my commitment to resolving them, ensuring the application meets PWA standards and delivers an optimal user experience.
 ![site.webmanifest console error](/static/images/readme/ewebmanifest.png)

 - **There is a bug with image handling on the Profile page**
 I have a field to upload a profile image on the profile form, however there is a conflict with jQuery and my profile.js file. This conflict results in breaking the image handling - it does not display on the profile page nor is it uploaded to cloudinary.  
 I tried my best to resolve this issue but unfortunately it was not possible within the given time contraints based on the relative importance of the feature.  
 Some things I tired:  
  -- using jQuery no conflict var in different ways  
  -- loading the jQuery script in profile.js, base.html and profiles.html  
  -- restructuring the JS file  
  To avoid causing confusion for the user, I made the decision to remove the image upload field from the Profile form. The impact of this is that the user cannot customize their profile photo. Although the action is available in the admin panel so if the user is especially eager they can use the handly contact form to provide a link to their image!

##### [ Back to Top ](#table-of-contents)

# Deployment 

## Deployment Guide for the Sojourn Scribbles Website

### Deployment Steps:

#### Creating the Heroku App

- Begin by signing up or logging in to Heroku.
- In the Heroku Dashboard, click on 'New' and then select 'Create New App'.
- Choose a unique name for your project, like "Travelling Scribbles".
- Select the EU region.
- Click on "Create App".
- In the "Deploy" tab, choose GitHub as the deployment method.
- Connect your GitHub account and find/connect your GitHub repository.

#### Setting Up Environment Variables

- Create `env.py` in the top level of the Django app.
- Import `os` in `env.py`.
- Set up necessary environment variables in `env.py`, including the secret key and database URL.
- Update `settings.py` to use environment variables for secret key and database.
- Configure environment variables in the Heroku "Settings" tab under "Config Vars".
- Migrate the models to the new database connection in the terminal.
- Configure static files and templates directories in `settings.py`.
- Add Heroku to the `ALLOWED_HOSTS` list.

#### Creating Procfile and Pushing Changes

- Create a `Procfile` in the top level directory.
- Add the command to run the project in the `Procfile`.
- Add, commit, and push the changes to GitHub.

#### Heroku Deployment

- In Heroku, navigate to the Deployment tab and deploy the branch manually.
- Monitor the build logs for any errors.
- Upon successful deployment, Heroku will display a link to the live site.
- Make sure to resolve any deployment errors by adjusting the code as necessary.

### Forking the Repository

Forking the GitHub Repository allows you to create a copy of the original repository without affecting it. Follow these steps:

- Log in to GitHub or create an account.
- Visit the [repository link](https://github.com/katiejanecoughlan/sojourn-scribbles-V3).
- Click on "Fork" at the top of the repository.

### Creating a Clone of the Repository

Creating a clone enables you to make a local copy of the repository. Follow these steps:

- Navigate to the [Sojourn Scribbles repository](https://github.com/katiejanecoughlan/sojourn-scribbles-V3).
- Click on the <>Code button.
- Select the "HTTPS" option under the "Local" tab and copy the URL.
- Open your terminal and change the directory to your desired location.
- Use `git clone` followed by the copied repository URL.


##### [ Back to Top ](#table-of-contents)

# Resources

- [Code Institute Full Stack Development course materials](https://codeinstitute.net/) 
- [Django docs](https://www.djangoproject.com/)
- [Crispy forms docs](https://django-crispy-forms.readthedocs.io/en/latest/)
- [jQuery docs](https://learn.jquery.com/using-jquery-core/avoid-conflicts-other-libraries/#:~:text=Thus%2C%20if%20you%20are%20using,use%20jQuery%20in%20your%20page.)
- [Cloudinary docs](https://cloudinary.com/documentation/programmable_media_overview)
- [Bootstrap docs](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Stack overflow](https://stackoverflow.com/)
- [Dev Community](https://dev.to/)
- [Code Institude Slack](https://slack.com/)

##### [ Back to Top ](#table-of-contents)

# Credits and Acknowledgements

## Images

- The Sojourns Scribbles logo was created by me using [Canva](https://www.canva.com/)
- Profile images for the mock content were generated by AI using [gencraft](https://gencraft.com/)
- Post featured images for the mock content were taken from royalty free stock photos on [Pexels](https://www.pexels.com/)

## Code

- **Code Institute** course content for providing the knowledge and guidance to build the project
- GitHub user **TulaUnogi** for sharing a best practice README structure
- Course Facilitator **David Calikes** for his unwaving support and guidance during the process 
- Tutor **Martin McInerney** for his endless patience and support with trouble shooting issues
- Tutor **Kevin Loughrey** for his helpful SME sessions and constant support
- My mentor **Chris Quinn** for sharing his wisdom and guiding me in this project
- My fellow **cohort peers** for their support, help with trouble shooting issues and sharing the experience

##### [ Back to Top ](#table-of-contents)
