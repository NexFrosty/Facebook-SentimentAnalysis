# Sentiment Analysis of Facebook Reviews

## Project Overview

This project develops a sentiment analysis system for Facebook app reviews to filter out emojis and bot-generated content for more accurate user feedback. This refined feedback assists in enhancing the app's relevance and user satisfaction.

## Problem Statement

Facebook accumulates many user reviews, including genuine feedback, bot-generated texts, and emoji reactions. Accurately analyzing these reviews is challenging due to inauthentic sentiments and unconventional expressions.

## Objectives

1. Extract user review data from the Facebook platform through web scraping.
2. Clean the data by removing duplicates and irrelevant characters like emojis and special symbols.
3. Analyze the sentiments of the reviews to categorize them into positive or negative sentiments.
4. Develop and assess a machine learning model that accurately classifies review sentiments.

## Methodology

### Data Acquisition

- **Web Scraping**: Implemented in Python to gather review data from Facebook.

### Data Preprocessing and Analysis

- **RapidMiner**: Used for cleaning the data and preparing it for analysis by removing unwanted characters and duplicates.

### Sentiment Analysis

- **Extraction and Classification**: Conducted in RapidMiner using NLP techniques to determine the sentiment expressed in each review.

### Machine Learning Modeling

- **Model Development and Evaluation**: Models like SVM, Decision Trees, Naive Bayes, and Random Forest are developed and evaluated in RapidMiner.

## Technologies Used

- **Python**: For web scraping.
- **RapidMiner**: For data preprocessing, sentiment extraction, and machine learning modeling.

## Installation and Setup

Clone the repository and run `webscrape.py` to webscrape Facebook reviews into excel file

For preprocessing, sentiment analysis, and machine learning modeling, use the corresponding RapidMiner processes provided in the repository.

## Conclusion

The SVM model proved to be the most accurate in classifying sentiments. This project demonstrates the utility of combining web scraping with advanced data analytics to enhance the understanding of user feedback on social platforms.

