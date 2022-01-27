from df_engine.core import Actor
from df_engine.core.keywords import RESPONSE
from df_engine.core.keywords import GLOBAL,TRANSITIONS, RESPONSE
import re
import df_engine.conditions as cnd
import scenario.condition as cust_cnd
plot = {
    "global": {
        "start": {
            RESPONSE: "",
            TRANSITIONS: {
                "intro": cnd.regexp(r"hi|hello", re.IGNORECASE),
            }
        },
        "intro": {
            RESPONSE: "Welcome, to our Cloth service catbot.\n Here in chat you can ask for \n 1. Dry Cleaning Services  \n 2. Tailoring Services".format(), 
            TRANSITIONS: {
                ("dry_cleaning", "start"): cust_cnd.dry_cleaning,
                ("custom_tailoring", "start"): cust_cnd.custom_tailoring,
                ("buy_clothes", "start"): cust_cnd.buying_clothes,
                ("global", "fallback"): cust_cnd.fallback,
            }
        },     
        "fallback": {
            RESPONSE: "Sorry we failed to understand, Please try again...",
            TRANSITIONS: {
                ("global", "intro"): cnd.true()
            }
        }
    },
    "custom_tailoring":{
        "start":{
            RESPONSE: "Welcome to our custom tailoring services, we would need some more information to process your order. Who is this for \n 1) Male \n 2) Female".format(), 
            TRANSITIONS: {
                    ("male","start"): cnd.regexp(r".*(male|man|boy|son|dad|boyfriend|1)", re.IGNORECASE),
                    ("female","start"): cnd.regexp(r".*(female|lady|girl|daughter|1)", re.IGNORECASE),                    
                }
        },
        "book_success":{
            RESPONSE: "Thanks for connecting with us for your tailoring needs, we have your information, we will deliver it to you" .format(), 
            TRANSITIONS: {
                ("global", "intro"): cnd.true()
            }
    },
    },
    "male":{
        "start":{
            RESPONSE: "Great, what do you want to get tailored \n 1. Upper Wear   $50/piece \n 2. Lower Wear   $40/piece \n 3. Suits, Formals etc. 150/pair \n Please let us know what do you want to get tailored" .format(), 
            TRANSITIONS: {
                    ("male","upper"): cnd.regexp(r".*(upper|shirt|coat|1)", re.IGNORECASE),
                    ("male","lower"): cnd.regexp(r".*(pant|trouser|jeans|2)", re.IGNORECASE),
                    ("male","pair"): cnd.regexp(r".*(suit|pair|formals|3)", re.IGNORECASE),                                                         
                }
            },
        "upper":{
            RESPONSE: "Great, We will tailor a brilliant upper wear for you, Please let us know your chest size and choice of fit slim/regular " .format(), 
            TRANSITIONS: {
                ("custom_tailoring","book_success"): cnd.regexp(r"[1-9][0-9]?$|^100", re.IGNORECASE)
            } 
        },
        "lower":{
            RESPONSE: "Great, We will tailor a brilliant lower wear for you, Please let us know your waist size and choice of fit slim/regular" .format(), 
            TRANSITIONS: {
                ("custom_tailoring","book_success"): cnd.regexp(r"[1-9][0-9]?$|^100", re.IGNORECASE)
            }   
        },
        "pair":{
            RESPONSE: "Great, We will tailor a brilliant pair for you, Please let us know your waist and chest size and choice of fit slim/regular" .format(), 
            TRANSITIONS: {
                ("custom_tailoring","book_success"): cnd.regexp(r"[1-9][0-9]?$|^100", re.IGNORECASE)
            }   
        }

    },
    "female":{
        "start":{
            RESPONSE: "Great, what do you want to get tailored \n 1. Upper Wear   $40/piece \n 2. Lower Wear   $30/piece \n 3. Suits, Formals etc. 120/pair \n Please let us know what do you want to get tailored" .format(), 
            TRANSITIONS: {
                    ("female","upper"): cnd.regexp(r".*(upper|shirt|top|tshirt|1)", re.IGNORECASE),
                    ("female","lower"): cnd.regexp(r".*(pant|trouser|jeans|2)", re.IGNORECASE),
                    ("female","pair"): cnd.regexp(r".*(suit|pair|formals|3)", re.IGNORECASE),                                                         
                }
            },
        "upper":{
            RESPONSE: "Great, We will tailor a beautiful upper wear for you, Please let us know your chest/breast size and choice of fit slim/regular " .format(), 
            TRANSITIONS: {
                ("custom_tailoring","book_success"): cnd.true()
            } 
        },
        "lower":{
            RESPONSE: "Great, We will tailor a beautiful lower wear for you, Please let us know your waist size and choice of fit slim/regular" .format(), 
            TRANSITIONS: {
                ("custom_tailoring","book_success"): cnd.regexp(r"[1-9][0-9]?$|^100", re.IGNORECASE)
            }   
        },
        "pair":{
            RESPONSE: "Great, We will tailor a beautiful pair for you, Please let us know your waist and chest/breast size and choice of fit slim/regular" .format(), 
            TRANSITIONS: {
                ("custom_tailoring","book_success"): cnd.true()
            }   
        }

    },              
    "dry_cleaning":{
        "start":{
            RESPONSE: "Welcome, to our chatbot to assist you with your dry cleaning needs.\n Please provide your mobile number and address/location to pick up the clothes".format(),
            TRANSITIONS: {
                ("dry_cleaning","cleaning_charges"): cnd.true()
            },
        },
        "cleaning_charges":{
            RESPONSE: "we charge $5 per clothing piece as flat rate. Please let us know how many clothes do you have" .format(), 
            TRANSITIONS: {
                ("dry_cleaning", "book_success"): cnd.true()
            }             
        },

         "book_success":{
            RESPONSE: "Thanks for connecting with us for you dry cleaning/tailoring needs" .format(), 
            TRANSITIONS: {
                ("global", "intro"): cnd.true()
            }             
        },
    },
    "buy_clothes":{
         "start":{
            RESPONSE: "Welcome, to our chat bot service, we are sorry to inform that we do not sell clothes, we provide specialised services such as dry cleaning and custom tailoring".format(),  
            TRANSITIONS: {
                ("buy_clothes","book_success"): cnd.true()
            },          
        },
        "book_success":{
            RESPONSE: "Thanks for contacting us. Please let us know know when you need help with dry cleaning or tailoring services" .format(), 
            TRANSITIONS: {
                ("global", "intro"): cnd.true()
            }             
        },
    }
}


actor = Actor(plot, start_label=("global", "start"), fallback_label=("global", "fallback"))