
# Skill -Clothes

## Description
We have built a chatbot which handles queries pertaining to dry-cleaning and custom-tailoring needs of the customers and asks customer for neccesory information before completing the order booking.

In order to achive this, we have created a BERT based multi intent classification model, which uses a pre-trained model on Hugging-Face dataset. This uses the concept of transfer learning and word embedding in order to maximise our learning from limited training data available for training the model.

Training data for the model has been created synthetically.

Our NLP based Intent classification model has three intents pertaining to diffrent skills-
1)dry_cleaning - "for handling customer queries related to dry cleaning and taking orders"
2)custom_tailoring -"for handling customer queries related to tailoring and taking orders"
3)buy_clothes- "for identifying sales related queries to inform the customer that company does not sale clothes but provide services like dry-cleaning and custom-tailoring"

## dry_cleaning-Chat bot flow
Step1- Identification of greeting and prompting the customer to mention their query

Step2 - Identification of customer intent using BERT classification model

step3 - Asking customer for mobile number and address

step4- Mention of pricing to the customer and asking for number of clothing items

step5- order booking

## Example of actual chat with bot - for dry_cleaning intent

" type your answer: hi

-> Welcome, to our Cloth service catbot.

 Here in chat you can ask for
 
 1. Dry Cleaning Services
 
 2. Tailoring Services
 
type your answer: dry cleaning

-> Welcome, to our chatbot to assist you with your dry cleaning needs.
 Please provide your mobile number and address/location to pick up the clothes
 
type your answer: 9901039005 , E1010 ozone evergreens

-> we charge $5 per clothing piece as flat rate. Please let us know how many clothes do you have

type your answer: 51

-> Thanks for connecting with us for you dry cleaning/tailoring needs"


## custom_tailoring-Chat bot flow
Step1- Identification of greeting and prompting the customer to mention their query

Step2 - Identification of customer intent using BERT classification model

step3 - Asking customer about gender and prompting with personalised queries which are followed next.

step4- checking with customer on what they want to get tailored and letting them know about the prices

step5- asking about the sizes and fitting prefrences.

step5- order booking

## Example of actual chat with bot - for custom_tailoring intent

" type your answer: hi

-> Welcome, to our Cloth service catbot.
 Here in chat you can ask for
 1. Dry Cleaning Services
 2. Tailoring Services
 
type your answer: tailoring

-> Welcome to our custom tailoring services, we would need some more information to process your order. Who is this for
 1) Male
 2) Female
 
type your answer: male

-> Great, what do you want to get tailored
 1. Upper Wear   $50/piece
 2. Lower Wear   $40/piece
 3. Suits, Formals etc. 150/pair
 
 Please let us know what do you want to get tailored
 
type your answer: shirt

-> Great, We will tailor a brilliant upper wear for you, Please let us know your chest size and choice of fit slim/regular

type your answer: 39

-> Thanks for connecting with us for your tailoring needs, we have your information, we will deliver it to you"


## buy_clothes-Chat bot flow

Step1- Identification of greeting and prompting the customer to mention their query

Step2 - Identification of customer intent using BERT classification model

step3 - Letting the customer know that this is not a sales bot but provide specific cothing services like dry cleaning and custom-tailoring

## Example of actual chat with bot - for buy_clothes intent

" type your answer: hi

-> Welcome, to our Cloth service catbot.
 Here in chat you can ask for
 1. Dry Cleaning Services
 2. Tailoring Services
 
type your answer: buy clothes

-> Welcome, to our chat bot service, we are sorry to inform that we do not sell clothes, we provide specialised services such as dry cleaning and custom tailoring"

## Quickstart

```bash
pip install -r requirements.txt
```
Run interactive mode
```bash
python run_interactive.py
```

```
## Resources
#TODO: resources
* Execution time: 2:28
* RAM: 8GB
