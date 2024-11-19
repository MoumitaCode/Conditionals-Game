# Welcome the user and explain what to them about what to do
print("Hello User, Welcome to Moumita's Horoscope Reading! ")
print("Type in your zodiac sign, and I'll tell you your fortune for today.")

# Ask the user what their zodiac sign is
sign = input("What's your zodiac sign? ")

# Tell them their horoscope based on their input
if sign == "Aries":
    print("Take the lead today.")
elif sign == "Taurus":
    print("Slow down and enjoy the simple things. Today is for peace.")
elif sign == "Gemini":
    print("Communication is everything. Reach out to someone new.")
elif sign == "Cancer":
    print("Make sure to pampare yourself sometimes.")
elif sign == "Leo":
    print("Shine with confidence!")
elif sign == "Virgo":
    print("Stay organized. Your attention to detail will pay off.")
elif sign == "Libra":
    print("Talk to yourself it’s the only conversation you can win!")
elif sign == "Scorpio":
    print("Deep feelings are in focus. Embrace them and grow.")
elif sign == "Sagittarius":
    print("Explore something new today.")
elif sign == "Capricorn":
    print("Hard work will pay off. Stay focused on your goals.")
elif sign == "Aquarius":
    print("Think outside the box.")
elif sign == "Pisces":
    print("Dream big but don't forget reality :) ")
else:
    print("Hmm, I didn't recognize that sign. Double-check the spelling and try again!")
