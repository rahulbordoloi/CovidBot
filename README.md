# CovidBot

[![Pull Requests Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)
[![Setup Automated](https://img.shields.io/badge/setup-automated-blue?logo=gitpod)](https://gitpod.io/from-referrer/)

<i>A Simple Static Bot/Agent which will act as a guide for self assessment of probable risks from corona virus and increase awareness about the pandemic.</i>

<img src="https://github.com/rahulbordoloi/CovidBot/blob/master/corona.jpg" width="800" height="500">

## Goal

It's a Simple Bot/Agent which will act as a guide for self assessment of probable risks from corona virus and increase awareness about the pandemic. It answers any type of questions related to the pandemic and also tells you about the pandemic's statistics when asked for. The Bot can be also be asked about myths and rumours related and it also has the capability to mail a detailed report regarding the pandemic to the user. 

## Technological Stack

This project is made using Google Dialogflow and the Language and Framework used for Backend Fulfillment is Python.

For Front-End Development: Dialogflow Console. <br>
For Back-End Development: Python, Flask, Ngrok, Postman, Restful API, HTML, Javascript, CSS, Bootstrap, Pivotal Web Services, Kommunicate.io integration, Google Colab, Heroku, Git, SMTP services. 

## Dependencies - 

If you're working on a Local Machine, install the dependencies from your terminal with -
 ```
 pip install -r requirements.txt
 ```
 ## Development -
 
For developmental purposes and local hosting I've used ```ngrok``` framework and ```flask``` api. The Coder Editor in which I've developed the code is ```VS Code```.

<b>For Front-End Development,</b><br>

1.Use the Dialogflow console to develop and design all the neccessary intents and entities according to your purpose.

<b>For Back-End Development and webhook connection, </b><br>

1. Open your terminal, and then run your Flask app as ```python app.py```.
2. It will now get hosted in your local system with the IP as ```127.0.0.1/5000``` ie hosted on port 5000. (you can explicitely specify the port number though).
3. Now, run ```ngrok http [port-number]```. In my case, port-number = 5000.
4. If your deployment is successful, it will provide you with an IP address. Feed that IP address as ```ip-address/webhook``` into your dialogflow fulfillment console.
5. Now, test the API using ```POSTMAN```. If it's alright, we're good to go.
6. Set-up all necessary developments required such as STMP Server, fulfillment texts etc.
7. After sucessfull completion of steps 1-6, deploy the ```CovidBot``` to a cloud services platform. I've used Pivotal Web Services here. In your terminal, after install of pivotal-cli type ```cf login``` to login into your credentials and then ```cf push``` to push your local repository. After sucessful deployment, a valid IP address of the deployment will be given and then update the fulfillment link in the Dialogflow console as ```[ip-address]/webhook```. 
 
## Live Build -

Telegram Link: https://t.me/r07_CovidBot                                                            
Web Deployment: https://rahulbordoloi.me/CovidBot/ <br>
Dialogflow Web Demo: https://bot.dialogflow.com/CovidBot <br> 
Fb Messenger: http://m.me/CovidBot (development phase) <br>
Twitter Bot: http://twitter.com/DevR07 (development phase) <br>

If you want to run this on your dialogflow console, download ```CovidBot.zip``` file and export it in your Dialogflow Console. <br>
Refer ```/docs``` directory for the backend files.


## Demo

![](web.gif)
<img src="https://github.com/rahulbordoloi/CovidBot/blob/master/ss.JPG" width="800" height="500">

## Bot Integration

To integrate this bot in your webpage, copy the following Javascript code from below and paste it just above the closing of ```<body>``` tag on every page you want the chat widget to appear. <br>
<b>Using kommunicate.io -</b>
```
<!--Chatbot Script-->
        <script type="text/javascript">
                /* NOTE : Use web server to view HTML files as real-time update will not work if you directly open the HTML file in the browser. */
                (function(d, m) {
                    var kommunicateSettings = {
                        "appId": "233bd45d08e21830167f3c8c53313aa1",
                        "popupWidget": true,
                        "automaticChatOpenOnNavigation": true
                    };
                    var s = document.createElement("script");
                    s.type = "text/javascript";
                    s.async = true;
                    s.src = "https://widget.kommunicate.io/v2/kommunicate.app";
                    var h = document.getElementsByTagName("head")[0];
                    h.appendChild(s);
                    window.kommunicate = m;
                    m._globals = kommunicateSettings;
                })(document, window.kommunicate || {});
            </script>
```
Refer [kommunicate](https://kommunicate.io) if you want to host your own chatbot.

<b>Using Dialogflow Messenger -</b>

```<script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>
<df-messenger
  chat-icon="https://storage.googleapis.com/cloudprod-apiai/8d81cb42-c711-46b5-aaa1-6ca8be92b8b3_x.png"
  intent="WELCOME"
  chat-title="CovidBot"
  agent-id="8ccaee6e-900c-4418-a3c9-a57f231925bb"
  language-code="en"
></df-messenger>
```

## References -

* [kommunicate](https://kommunicate.io) for chatbot integration.
* [rapid-api](https://rapidapi.com) for corona-stats api.

## Contributing [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

If you are the helping and contributing one, your efforts and suggestion are always welcomed.
