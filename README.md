# 📌 Hello_World_API
## Coding Round 2 _**The Hello World API Assignment**_
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


3. Now to test the API click on the address and edit it. According to the respective language and click enter 
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/0df61883-0fdc-4e4c-9e55-1d9ad11620e4)

4. Now a Hello World message will be displayed on the Client Browser 
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/63c8bbd1-048a-4207-b5b9-6fdf73138d13)

# Task B : Through Web Page allow the user to choose a language and call the API

1. Click on all the buttons one by one and you should able to see the respective message for respective languages
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/7e945047-101e-4ba4-8ada-02957e8a6f69)

2. For English
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/33411b8b-aeb9-49b9-a5c2-42cc1ec942c4)

3. For French
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/eb5c6650-0095-4434-962e-cc160f3a6584)

4. For Hindi
![image](https://github.com/jayeshrajpoot/Hello_World_API/assets/53878260/94c0f396-f20e-42eb-b668-7f3a4c0dabe1)


