"""
Write a mood assessor program
"""
import datetime
import os


def assess_mood():
    moods = ['happy', 'relaxed', 'apathetic', 'sad', 'angry',]
    client_mood = input("Your mood today: ")
    while client_mood not in moods:
        client_mood = input("Your mood today:")
    def mood_to_num():
        if client_mood == 'happy':
            return 2
        elif client_mood == 'relaxed':
            return 1
        elif client_mood == 'apathetic':
            return 0
        elif client_mood == 'sad':
            return -1
        elif client_mood == 'angry':
            return -2
    if client_mood in moods:
        mood_to_num()
        open("mood_diary.txt", "w")
