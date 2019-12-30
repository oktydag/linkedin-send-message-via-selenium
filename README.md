# linkedin-send-message-via-selenium

- This application creates a Chrome Web Browser and open Linkedin with your account and send messages to person you determine via Selenium in Python.

 # Getting Started

## 1. Download or clone this repo with

```
git clone https://github.com/oktydag/linkedin-send-message-via-selenium.git

```


# Steps For Run
## 1.  virtualenv

Create a virtualenv and activate it.

```
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```

Activate venv for **Windows**

```
$ cd venv
$ source Scripts/activate
```

**virtualenv** is a tool to create isolated Python environments. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

## 2.  Install Selenium and ChromeDriver

```
$ pip install selenium
```


Selenium is a free (open source) automated testing suite for web applications across different browsers and platforms. It is quite similar to HP Quick Test Pro (QTP now UFT) only that Selenium focuses on automating web-based applications. Testing done using Selenium tool is usually referred as Selenium Testing.


You can install the **ChromeDriver** from https://sites.google.com/a/chromium.org/chromedriver/downloads . Please take care of your chrome version and operation system before installing.


## 3. Change User Iterations

In **user_iterations.py** , you can find **your_username** and **your_password** field to fill with your Linkedin Account informations.

You can also see **person_you_want_to_send_message** and **message_you_want_to_send** to sending your message text and person name that you want to send your message.

## 4. Run the main.py in venv

```
$ (venv) python main.py
```


## 5. See The Result

You will see the steps like these; 

- Chrome that is being controlled by automated test software will be opened because of **Selenium WebDriver**.
- Going to Login Page in Linkedin
- You will see your account information is written according to information in **user_iterations**
- Your Linkedin Dashboard will be shown.
- You will see that your messages will be shown.
- Click automaticly to new message 
- You will see that your message and its owner will be written according to information in **user_iterations**

Good Watch !

## 6. Plus

You can use Selenium to your require tests such as testing whether the sending messages button works successfully, user login/logout operations with token etc. For more detail, visit https://selenium.dev/ .
