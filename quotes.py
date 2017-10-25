#! /usr/bin/python3
from random import SystemRandom
import sys
quotesLight = ["That's not how the Force works!",
"These aren’t the droids you’re looking for...",
"When 900 years old, you reach… Look as good, you will not.",
"IT'S A TRAP!",
"Do or no not, there is no try.",
"Only a Sith deals in absolutes."]
quotesDark = ["No. I am your Father.",
"I find your lack of faith disturbing.",
"You underestimate my power...",]
r = SystemRandom()
argument = sys.argv[1]
if argument == "j":
	print(quotesLight[r.randrange(len(quotesLight))])	
elif argument == "s":
	print(quotesDark[r.randrange(len(quotesDark))])
else:
	print("Error. You broke some shit.")
