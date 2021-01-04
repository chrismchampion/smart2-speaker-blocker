## Test Notes

- Latency expressed in terms of %, e.g. 20 seconds (Alexa) / 2 seconds (Smart2) = 10% overhead increase.
- Average of several runs taken.
- Time recorded in milliseconds (timestamp in ms, e.g. 5000).
- Future improvement to latency: Another thread for recording Alexa.

### Test 1: "How is the weather?"
Alexa | Smart^2
----- | -----
ca. 1.8 - 2.10s + 8 sec for response | ca. 6.5s

Difference of ca. 4.40 - 4.70 s
* 4.4/9.8 = 0.449
* 4.7/10.1 = 0.4653

**Smart2 adds 45%-46.5% overhead.**

### Test 2: "Play CNN news."
Alexa | Smart^2
----- | -----
ca. 2.5-3.0s until Alexa replies | ca. 6.45s

Difference of ca. 3.45 - 3.95 s

### Test 3: "Tell me a joke."
Alexa | Smart^2
----- | -----
ca. 1.7s | ca. 6.8s

Difference of ca. 5.10s

### Test 4: "What's 5+5?"
Alexa | Smart^2
----- | -----
3.68 | 7.46

Difference of ca. 3.78s

> The processing time of Smart2 is roughly 3-4 seconds. Roughly the same time Alexa needs to process a request and respond.
> Potential to improve latency exists by recording Alexa in a concurrently running thread.