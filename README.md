# 📌 Hello_World_API
## Coding Round 2 _**The Hello World API Assignment**_ for Ignite Solution Campus Recruitment
### This is a simple REST API that returns a greeting message in the specified language.
### Let's clear some basics first!
<details>

<summary>What is a REST API</summary>
A REST API is a way of accessing and interacting with data over the internet. REST stands for Representational 
State Transfer, and it is a set of architectural principles for designing web services.
</details>
<details><summary>What is a GET request?</summary>
A GET request is a HTTP request that is used to retrieve data from a server. The /hello endpoint in this API uses a GET request to get the greeting message for the specified language.
</details>
<details>
    <summary>What is a query parameter?</summary>
    A query parameter is a piece of information that is appended to the URL of a web request. The language query parameter in this API is used to specify the language of the greeting message.
</details>
The code in hello_world.py defines a simple Flask application that exposes a single REST GET endpoint at /hello. The endpoint takes a query parameter called language and returns a greeting message in the specified language. The following table shows the supported languages and their corresponding greeting messages:


| Language |    Greeting message |
|----------|   ------------------|
| English  |    Hello world      |
| French   |    Bonjour le monde | 
| Hindi	   |    Namastey sansar  |



## Task A : Implementation of API on Local Machine
## Getting Started

These instructions will help you set up and run the project on your local machine. Make sure you follow these steps carefully to ensure a successful setup.

### Prerequisites

Before you begin, ensure you have the following tools installed:

- [Python](https://www.python.org/downloads/) - This project requires Python X.X or higher.
- [Git](https://git-scm.com/downloads) - You'll need Git to clone the repository and manage version control.

### Installation

1. Clone the repository to your local machine:

```
    git clone https://github.com/jayeshrajpoot/Hello_World_API/tree/master
```
2. Change the directory to your-name-name
```
    cd your-project-name
```
3. Create the virtual enviroment in your local machine
```
    python -m venv venv
```
4. Activate the virtual environment
```
    source venv/bin/activate  # On Windows: venv\Scripts\activate
```
5. Run the below command to install all the dependencies in your local virtual environment
```
    pip install -r requirements.txt
```
6. Run this command to start the flask server in your local machine
```
    python app.py
```
<details>
    <summary>How to use the "Hello World" API</summary>
To use the "Hello World" API, you can use a web browser or a REST client.

To use a web browser, open the following URL in your browser:

http://localhost:5000/hello?language=English

The language parameter should be set to the language of the greeting message you want to receive. For example, to get a greeting message in French, you would use the following URL:

http://localhost:5000/hello?language=French

To use a REST client, you can use the following request:

GET http://localhost:5000/hello?language=English

The response will be a JSON object with the following structure:
{
"message": "Hello world"
}
</details>

2. Open your web browser and go to http://localhost:5000 The page should look like this
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/a78411d9-ae2c-408f-b31c-bf0f3b35f6d5)


3. Now to test the API click on the address and edit it. According to the respective language and click enter 
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/0df61883-0fdc-4e4c-9e55-1d9ad11620e4)

4. Now a Hello World message will be displayed on the Client Browser 
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/63c8bbd1-048a-4207-b5b9-6fdf73138d13)

6. To get the _"Hello World"_ message in **French** and **Hindi** language we just need to change the language parameter to French and Hindi
# Task B : Through Web Page allow the user to choose a language and call the API

1. Click on all the buttons one by one and you should able to view the **"Hello World"** message in corresponding languages
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/7e945047-101e-4ba4-8ada-02957e8a6f69)

2. After clicking on **English** button
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/33411b8b-aeb9-49b9-a5c2-42cc1ec942c4)

3. After clicking on **French** button
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/eb5c6650-0095-4434-962e-cc160f3a6584)

4. After clicking on **Hindi** button
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/94c0f396-f20e-42eb-b668-7f3a4c0dabe1)

## Task C: Making use of AWS Lambda and AWS API Gateway to invoke a API endpoint and testing it using POSTMAN  
<details>
    <summary>AWS Lambda</summary>
    AWS Lambda is a serverless computing service that allows you to run code without provisioning or managing servers. Lambda functions can be triggered by events, such as HTTP requests, database changes, or file uploads.
</details>
    <details>
    <summary>AWS API Gateway</summary>
    AWS API Gateway is a fully managed service that makes it easy to create, publish, maintain, monitor, and secure APIs. API Gateway can be used to expose your Lambda functions to the public or to other AWS services.
</details>
<details>
    <summary>POSTMAN</summary>
    POSTMAN is a popular API development and testing tool. POSTMAN allows you to send HTTP requests to APIs, view the response, and debug errors.
</details>

## Steps to Integrate AWS Lambda and API Gateway to invoke an endpoint 
##### Step 1) Create a AWS Lambda function (choose Python X.X as environment)
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/d1555cf0-8426-4129-9198-d12c36920408)

##### Step 2) Add trigger as API Gateway
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/8e077d45-d250-4b81-96e7-6fe02965b743)

##### Step 3) Write the function code in lambda_function.py file
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/bfe1a359-9006-4ae1-bfe7-aefe12c9e1a3)

##### Step 4) Edit the Runtime settings 
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/32a2a408-1426-4cfc-887f-d3ac0b9cd1c4)

##### Step 5) Click on Deploy to save the changes in the lambda_function.py file
##### Step 6) Click on Configure test event 
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/3bcdfe3a-df6f-4d7c-b413-b0f279a66e79)

##### Step 7) Give the event name and provide the EventJson where queryStringParameters is an object and "language" : "English" is key value pair
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/b1ac422b-5c5d-45f0-90db-222a720b76bc)

##### Step 8) Click on Save and Invoke and view the Execution reults
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/727f396b-c1b0-4188-880b-d6f2b42e3730)

##### Step 9) Create a REST API using AWS API Gateway service
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/c3fb2c53-b16e-4b49-8c8b-b0de736c1309)

##### Step 10) Create Resource from Actions dropdown and in resource Create Method GET
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/fd70c727-dd37-406e-8d1e-9db64aaecc18)

##### Step 11) Click on Deploy API and select stage as dev
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/5bb16688-5452-4312-98be-098fe1e57c3a)

##### Step 12) A new Invoke URL will be provided by API Gateway
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/9c2d5de9-8fb2-4cd2-b281-4556a73aa748)

#### Step 13) Edit the Invoke URL and in front of stage name add /hello?language=Hindi
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/31623908-4dcc-48d9-b2a5-e6786bb78355)
If we change the language to English it'll display the "Hello World" message in English language and same for French language
#### Endpoint URL : https://hinysx6mjh.execute-api.us-east-1.amazonaws.com/dev/hello?language=Hindi

### Test the endpoint using POSTMAN

##### Select the GET Method and enter the endpoint we got from API Gateway and provide the language parameter.
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/b29aaaf5-144a-4160-8519-a004959583e9)

#### Testing the endpoint on French language parameter
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/3f6ddd9b-1d03-47f4-8062-d5666041853a)

##### If you get any error while following these steps you can refer the official AWS documentation 
