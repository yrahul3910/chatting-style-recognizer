# Chatting Style Recognizer
A project using a Naive Bayes multinomial event model classifier to recognize the sender in an online chat using the scikit-learn library. This was a submission by me and Bhavana KV to the inGenius hackathon, 2016. We used the Ruby script from
https://github.com/tvdstaaij/telegram-history-dump
to dump the Telegram chat histories used to train the algorithm, and wrote code to segregate the messages based on who sent it in one-on-one chats.

# Source Files
classify.py - The main source file that uses the scikit-learn (sklearn) library.
code.cpp - C++ code to segregate messages by each sender into two files.
