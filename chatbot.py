responses = {
    "hi": "Hello! How can I assist you today?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "I'm just a WPS_Helpdesk_bot, but I'm here to help you!",
    #"bye": "Goodbye! Have a great day!",
    "exit": "Goodbye! Have a great day!",
    "courier": "1.Raise a courier\n2.Track a courier.",
    "raise a courier" : "1.Domectic Courier\n2.International Courier",
    #"domectic" : "https://apps.powerapps.com/play/e/default-63545f27-3232-4d74-a44d-cdd457063402/a/3108a0e6-adc0-46c2-b416-89c7bae71141?tenantId=63545f27-3232-4d74-a44d-cdd457063402",
    #"domectic courier" : "https://apps.powerapps.com/play/e/default-63545f27-3232-4d74-a44d-cdd457063402/a/3108a0e6-adc0-46c2-b416-89c7bae71141?tenantId=63545f27-3232-4d74-a44d-cdd457063402",
    "international" : "https://mydhl.express.dhl/in/en/home.html#/createNewShipmentTab",
    "international courier" : "https://mydhl.express.dhl/in/en/home.html#/createNewShipmentTab",
    "track a courier" : "1.Blue Dart\n2.DHL\nType your courier vendor Name",
    "track" : "1.Blue Dart\n2.DHL\nType your courier vendor Name",
    #"blue dart" : "https://www.bluedart.com/",
    #"blue dart" : "Please enter your AWB No",
   # "dhl": "http://www.dhl.co.in/en/express/tracking.html ",
    #"ticket":"https://sso.mainstreamsasp.com/PRD00659CRS/Dashboard.aspx",
    #"ticket on si7":"https://sso.mainstreamsasp.com/PRD00659CRS/Dashboard.aspx",
     
    
}
def get_response(user_input):
    # Convert user input to lowercase for consistency
        user_input = user_input.lower()
    
    # Check if the input is in the predefined responses
        if user_input in responses:
             return responses[user_input]
        else:
             return "I'm sorry, I didn't understand that. Can you please rephrase?"


        
      
