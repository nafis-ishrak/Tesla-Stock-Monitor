# Project Name: Tesla Stock Change Notifier

## Overview
The objective of this project was to create a notification service that sends a text message to the user’s mobile device when Tesla’s stock has experienced a greater than 5% change in its closing price. The text message includes relevant news about Tesla within that time period. The project utilized the Alphavantage API to obtain the closing prices of Tesla stock, the News API to retrieve the top headlines related to Tesla for a given time period, and the Twilio API to send a text message to the user’s phone.

## Tools and Technologies Used
The following tools and technologies were used for this project:
- Python programming language
- Alphavantage API for stock price data
- News API for news headlines data
- Twilio API for SMS notification
- Requests library for making API calls
- JSON library for parsing API responses

## Methodology
The project used the Alphavantage API to obtain the closing prices of Tesla stock. The program then checked if the stock price had experienced a greater than 5% change in its closing price. If the stock price had changed by more than 5%, the program utilized the News API to retrieve the top headlines related to Tesla for a given time period.

Finally, the Twilio API was utilized to send a text message to the user’s phone. The text message included the stock price change percentage and the relevant news headlines about Tesla within that time period.

## Results
The notification service successfully sent text messages to the user’s phone when Tesla’s stock had experienced a greater than 5% change in its closing price. The text messages included relevant news headlines about Tesla within that time period.

## Conclusion
In conclusion, this project demonstrates the potential of using APIs to create a notification service that can provide real-time updates on stock prices and relevant news headlines. The results of this analysis can be used to inform future research on the use of APIs for real-time data analysis and notification services.

## References
- Alphavantage API documentation: https://www.alphavantage.co/documentation/
- News API documentation: https://newsapi.org/docs
- Twilio API documentation: https://www.twilio.com/docs
- Requests documentation: https://docs.python-requests.org/en/latest/
- JSON documentation: https://docs.python.org/3/library/json.html










