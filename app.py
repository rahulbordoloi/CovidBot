# For Flask

from flask import Flask, request, make_response
import json
import requests
import os
from flask_cors import cross_origin

# For Mail

import smtplib
import imghdr
from email.message import EmailMessage

app = Flask(__name__)

# Geting and sending response to dialogflow

@app.route('/webhook', methods=['POST'])
@cross_origin()

def webhook():

    req = request.get_json(silent=True, force=True)

    #print("Request:")
    #print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    #print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def apireqCountry(country_name):

        url = "https://covid-193.p.rapidapi.com/statistics"
        querystring = {"country": country_name}
        headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "310ca9873bmsh00386ba3e0d270bp178cc1jsn4acd867aed05"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        #print(response.text)
        js = json.loads(response.text)
        #print("******", js)
        result = js.get('response')[0]
        #print(result.get('cases'))
        #print("*" * 20)
        # return result.get('cases') , result.get('deaths'),result.get('tests')
        deaths = result.get('deaths')
        tests = result.get('tests')
        cases = result.get('cases')

        webhookresponse = "-----Covid Report----- " + "\n" + " New Cases : " + str(cases.get('new')) + "\n" + " Active Cases : " + str(cases.get('critical')) + "\n" + " Critical Cases : " + str(cases.get('critical')) + "\n" + " Recovered Cases : " + str(cases.get('recovered')) + "\n" + " Total Cases : " + str(cases.get('total')) + "\n" + " Total Deaths : " + str(deaths.get('total')) + "\n" + " New Deaths : " + str(deaths.get('new')) + "\n" + " Total Test Done : " + str(tests.get('total')) + "\n" + "Last updated : " + str(result.get('time')) + "\n" + "\n-------END-------" + "\n" 
        return webhookresponse

def apireqWorld():
        url = "https://covid-19-statistics.p.rapidapi.com/reports/total"
        headers = {
            "x-rapidapi-host": "covid-19-statistics.p.rapidapi.com",
            "x-rapidapi-key": "310ca9873bmsh00386ba3e0d270bp178cc1jsn4acd867aed05"
        }
        response = requests.request("GET", url, headers=headers)
        print(response.text)
        js = json.loads(response.text)
        #print("******", js)
        result = js.get('data')

        webhookresponse = "-----World wide Report----- \n\n" + " Confirmed Cases :" + str(result.get('confirmed')) + "\n" + " Deaths Cases : " + str(result.get('deaths')) + "\n" + " Recovered Cases : " + str(result.get('recovered')) + "\n" + " Active Cases : " + str(result.get('active')) + "\n" + " Fatality Rate : " + str(result.get('fatality_rate') * 100) + "%" + "\n" + " Last updated : " + str(result.get('last_update')) + "\n" + "-------END-------" +  "\n"
        return webhookresponse

def apireqIndianS():
        url = "https://covid19-data.p.rapidapi.com/india"
        headers = {'x-rapidapi-host': "covid19-data.p.rapidapi.com", 'x-rapidapi-key': "482a8f8516msh16204eb9d1f4f68p1a9146jsnf33914c7300e"}
        response = requests.request("GET", url, headers=headers)
        #print(response.text)
        js = json.loads(response.text)
        #print("******", js)
        # #result = js.get('response')
        x = js

        print(len(js))

        webhookresponse1 = ''
        
        for i in range(0,38):
            webhookresponse = x[i]
            #print(webhookresponse['state'])
            #js = json.loads(webhookresponse.text)

            #print(str(js.state))
            webhookresponse1 += "---------\n" + " State :" + str(webhookresponse['state']) + "\n" + " Confirmed Cases : " + str(webhookresponse['confirmed']) + "\n" + " Death Cases : " + str(webhookresponse['deaths']) + "\n" + " Active Cases : " + str(webhookresponse['active']) + "\n" + " Recovered Cases : " + str(webhookresponse['recovered']) + "\n---------"
        
        y = "------State Wise Report------ \n\n" + webhookresponse1 + "\n\n-------END------- \n"
        return y
        #print("***World wide Report*** \n\n" + webhookresponse2 + "\n\n*******END********* \n")
        #print("***World wide Report*** \n\n" + webhookresponse3 + "\n\n*******END********* \n")

# Processing the request from dialogflow

def processRequest(req):
    
    #sessionID=req.get('responseId')

    result = req.get("queryResult")
    #user_says=result.get("queryText")
    parameters = result.get("parameters")
    #world = parameters.get("world")
    country = parameters.get("geo-country")
    print(country)
    #cust_contact = parameters.get("cust_contact")                                 
    user_email=parameters.get("cust_email")
    user_name= parameters.get("cust_name")
    user_country=parameters.get("cust_country")
    intent = result.get("intent").get('displayName')
    print(intent)

    if (intent == 'countries'):                                                   # for the country-intent

        #country = parameters.get("geo-country")
        if(country=="United States"):
            country = "USA"

        fulfillmentText = apireqCountry(country)

        return {

            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            fulfillmentText
                        ]

                    }
                },
                {
                    "text": {
                        "text": [
                            # "Do you want to ask any more Questions? Feel Free to ask any more :)"
                             "Do you want me to Mail you the detailed report for COVID-19 to your e-mail address? Type. \n 1. Mail \n 2. No "
                            # "Do you want me to send the detailed report to your e-mail address? Type.. \n 1. Yes \n 2. No "
                            # "We have sent the detailed report of {} Covid-19 to your given mail address.Do you have any other Query?".format(cust_country)
                        ]

                    }
                }
            ]
        }
    
    elif (intent == 'worldwide'):                                                # for the worldwide-intent

        fulfillmentText = apireqWorld()
        
        return {

            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            fulfillmentText
                        ]

                    }
                },
                {
                    "text": {
                        "text": [
                            "Do you want to ask any more Questions? Feel Free to ask any more :)"
                            # "Do you want me to send the detailed report to your e-mail address? Type.. \n 1. Yes \n 2. No "
                            # "We have sent the detailed report of {} Covid-19 to your given mail address.Do you have any other Query?".format(cust_country)
                        ]

                    }
                }
            ]
        }

    elif (intent == 'indian_states'):                                           # for the indian-state-wise-intent

        fulfillmentText = apireqIndianS()

        return {

            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            fulfillmentText
                        ]

                    }
                },
                {
                    "text": {
                        "text": [
                            "Do you want to ask any more Questions? Feel Free to ask any more :)"
                            # "Do you want me to send the detailed report to your e-mail address? Type.. \n 1. Yes \n 2. No "
                            # "We have sent the detailed report of {} Covid-19 to your given mail address.Do you have any other Query?".format(cust_country)
                        ]

                    }
                }
            ]
        }

    elif intent == 'send_email':                                                                         # for the sending=mail-intent

        url = "https://covid-193.p.rapidapi.com/statistics"
        querystring = {"country": user_country}
        headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "310ca9873bmsh00386ba3e0d270bp178cc1jsn4acd867aed05"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        #print(response.text)
        js = json.loads(response.text)
        #print("******", js)
        result = js.get('response')[0]
        #print(result.get('cases'))
        #print("*" * 20)
        # return result.get('cases') , result.get('deaths'),result.get('tests')
        deaths = result.get('deaths') 
        tests = result.get('tests')
        cases = result.get('cases')

        # for mail

        """e_total = str(cases.get('total'))
        e_new = str(cases.get('new')) 
        e_active = str(cases.get('critical'))
        e_critical = str(cases.get('critical'))
        e_recovered = str(cases.get('recovered'))
        e_deaths = str(deaths.get('total'))"""

        EMAIL_ADDRESS = os.environ.get('dev-id')             # Enter your GMail Here
        EMAIL_PASSWORD = os.environ.get('dev-pw')            # Enter your GMail's Password Here

        # contacts = ['test@mail.com', 'example@gmail.com']  // list of emails you wanna send

        msg = EmailMessage()
        msg['Subject'] = 'COVID Report !'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = user_email    # csv for multiple - ', '.join()
        
        #msg.set_content('Hello {},\nHere is your Detailed COVID-19 Report as you Requested. I have also attached The Prevention and Security measures issued by Indian Govt. PFA \nHave a Nice Deay Ahead. :) Do feel free to contact me at rahulbordoloi24@gmail if you need any further assistance. \n\nThanks & Regards,\nCovidBot'.format(user_name))
        
        e_file = open("base.html", "r")
        e_cont = e_file.read()

        msg.add_alternative(e_cont.format(user_name = str(user_name), user_country = str(user_country), e_total = str(cases.get('total')), e_new = str(cases.get('new')), e_active = str(cases.get('critical')), e_critical = str(cases.get('critical')), e_recovered = str(cases.get('recovered')), e_deaths = str(deaths.get('total'))), subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        fulfillmentText = "Hello " + user_name  + " the mail has been sent to " + user_email + "."
        
        return {
            "fulfillmentText": fulfillmentText
        }

    
    else:
        fulfillmentText="Sorry, Servers Busy at the Moment. Please try again Later."
        return {
            "fulfillmentText": fulfillmentText
        }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    #print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
