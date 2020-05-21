# CovidBot

[![Pull Requests Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)
[![Setup Automated](https://img.shields.io/badge/setup-automated-blue?logo=gitpod)](https://gitpod.io/from-referrer/)

<img src="https://github.com/rahulbordoloi/CovidBot/blob/master/covid24.jpg" width="800" height="500">

A Simple Static Bot/Agent which will act as a guide for self assessment of probable risks from corona virus and increase awareness about the pandemic.

This project is made using Google Dialogflow. 

Telgram Link: https://t.me/r07_CovidBot                                                            
Dialogflow Web Deployment: https://bot.dialogflow.com/CovidBot

If you want to run this on your dialogflow console, download this Zip File and Export it in your Dialogflow Console.

## Bot Integration
To integrate this bot in your webpage, copy the Javascript code from below and paste it just above the closing of body tag (</body>) on every page you want the chat widget to appear.
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

Rough Webpage Deployment - http://rahulbordoloi.me/covid19pro/

## Contributing [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

If you are the helping and contributing one, your efforts and suggestion are always welcomed.

Next Patch - Updating DB and APIs
