## Test Notes

Express increase in terms of %, e.g. 20 seconds (Alexa) / 2 seconds (Smart2) = 10% overhead increase.

### Test 1: "How is the weather?"
* Alexa: ca. 1.8 - 2.10s + 8 sec for response
* Smart2: ca. 6.5s

Difference of ca. 4.40 - 4.70 s
> 4.4/9.8 = 0.449
> 4.7/10.1 = 0.4653
> Smart2 adds 45%-46.5% overhead.

### Test 2: "Play CNN news."
Alexa - ca. 2.5 - 3.0s until Alexa replies
Smart2 - ca. 6.45s
	Difference of ca. 3.45 - 3.95

3. Tell me a joke.
Alexa - ca. 1.7s
Smart2 - ca. 6.8s
	Difference of ca. 5.10s
20



Do average of several runs

Record Smart2 in ms. (timestamp in ms eg 5000)

Another thread for recording alexa

What's 5+5?
Alexa - 3.68
Smart2 - 7.46

The processing time of Smart2 is roughly 3-4 seconds...
Roughly the seame time Alexa needs to process req. and respond.

Ask questions that will and won't go through to compare processing time.

Avg response time of when you finish the question to if-else clause...

measure 20 times and take avg...

q1 - pass		what's 5*5?
q2 - pass		how is the weather?
q3 - doesn't pass 	"my password is barbara backwards"
