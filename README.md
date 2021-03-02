# Django_Portfolio

This is a Resume/Personal Website built over Django.
I have used Django, HTML, CSS, Javascript for design and development. The contact support uses **Celery** for mail and notification handling.

## How to get started:
------------------------
### 1. Download the code.
First you need to download my repo or simply clone it on your local system.
```bash
git clone https://github.com/RitvikDayal/Django_Portfolio.git
```

### 2. Setup the Virtual Environment.
------------------------
I suggest you to use a virtual environment during testing and development.

1. Open **Terminal(Ctrl + Alt + T) or Window Command Prompt**

2. Now lets create a virtual environment.
        
    For Linux users:    `virtualenv venv`
    For Window Users:   `py -m venv venv`

3. Activating the virtual environment.

    Windows: `venv\Scripts\activate`
    Linux: `Source venv/bin/activate`

4. Installing Enivroment requiremnts

    My requiremnts.txt include libraries and dependencies for heroku deployement.

    ```bash
    pip install -r requirements.txt
    ```

### 3. Setting Up Environment Variables.
------------------------
It is a good practise to hide secrets in OS environment to prevent breaches. You can change this by replacing my os environment calls in settings.py in my project folder **core**

1. start python shell: Window - `py` / Linux: `python` or `python3`

2. setting up some variables:
    ```python3
    >>import os
    >>import secrets
    >>os.environ["SECRET_KEY"] = secrets.token_hex(20)
    >>os.environ["DEBUG"] = "True"
    >>os.environ["USER_EMAIL"] = "Your Email address"
    >>os.environ["USER_EMAIL_PASSWORD"] = "YOUR EMAIL PASSWORD"
    >>os.environ["RECAPTCHA_PUBLIC_KEY"] = "YOUR SITE KEY"
    >>os.environ["RECAPTCHA_PRIVATE_KEY"] = "YOUR_SECRET_KEY"
    >>quit()
    ```

    I am sorry for giving you this trouble but it is better to prevent than to cure. In future update I will try to add either a script or an interface for this configuration.

    REACPTACHA keys can be genrated from: [Here](https://developers.google.com/recaptcha/docs/v3)

### 4. Lets Start the server.
------------------------
for stating the server type the following in your command prompt
```bash
python manage.py runserver
```

Now the site works perfectly but it will not send Emails till now.

## SETTING UP CELERY
------------------------
You can setup your celery environment following this amazing video by a youtube channel: Very Academy: 
[Playlist](https://www.youtube.com/playlist?list=PLOLrQ9Pn6caz-6WpcBYxV84g9gwptoN20)

I recommend to watch complete playlist or the first 3 videos atleast for your understanding of Celery and RabbitMQ.

## Suggestions:

1. Check files like email.py, github.py, views.py for replacing dummy information and ensure proper working of the app.

2. Replace static files with same name in the static folders for not running into bugs or errors during development or deployement.

3. Configure allowed host list at line 15 in settings.py in project folder for security resons. by default it set to all `'*'`.

4. I have tried to leave no bugs but if you find any security flaw or bug please raise a fix request as Isuue to this repo.

# TO DO.
------------------------
Ther are few things left to do.

1. I will make a youtube video for better understanding of how you can use this template to make your own personal website.

2. I will try to make another branch of this project without celery so that you can deploy apps with full functioning and more easily.

3. I will be adding a feedback app for the projects for visitors on my website.

4. Find an alternate to street smart fix for github repo images.

5. Add a well designed HTML Emali template.

## Note:
I welcome all of your suggestion you can mention them as issues to this repo laso if you want to contribute I am still learning how contribution works over here so feel free to reach me at **ritvikr1605@gmail.com**.

# REQUEST:
Please give a star to the repo and share it for better outreach.

Thankyou ;-)
