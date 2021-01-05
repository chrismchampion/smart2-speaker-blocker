# Smart^2 Speaker Blocker

##### Table of Contents  
- [Publication](#publication-preprint)
- [Project Goal](#project-goal)
- [Design](#design)
  * [Resources Used](#resources-used)
- [Implementation](#implementation)
  * [Smart^2 Usage Modes](#smart2-usage-modes)
    + [Normal Mode](#normal-operationkeyword-evaluation-mode)
    + [Privacy Mode](#total-privacy-mode-voice-activated)
    + [Time-based Keyword Mode](#time-based-keyword-mode)
    + ["Argument" Mode](#argument-mode)
- [Test Data Summary](#testing-data-summary)
- [Additional Points](#additional-points) 

## Publication (Preprint)

###### arXiv.org > Computer Science > Cryptography and Security

[The Smart^2 Speaker Blocker: An Open-Source Privacy Filter for Connected Home Speakers](https://arxiv.org/abs/1901.04879)

## Project Goal
Develop a smart filter to give users more control over speech data sent over the network, ensuring privacy in their home.

## Design

##### Design diagram
![Smart^2 design](/img/fig1-design.png?raw=true "Smart^2 design diagram")
> Fig. 1. The microphone of the smart speaker is insulated from external sounds, and can only hear sounds forwarded by the smart speaker blocker.

### Resources Used
* Off-the-shelf Mini-ITX PC
* Off-the-shelf external USB microphone and Bluetooth speaker
* Amazon Echo Dot (2nd Generation)
* Open-source software:
  * Ubuntu 16.04 LTS
  * CMU (Carnegie Mellon University) PocketSphinx
  * PyPi SpeechRecognition library
  * Simple Google™ TTS (with pico2wave offline speech synthesis back-end)

##### Components diagram
![Smart^2 components](/img/fig2-components.png?raw=true "Smart^2 components diagram")
> Fig. 2. Audio data comes in from the microphone and is converted to text by the speech-to-text engine. Text and audio is both passed to the filtering engine, which decides whether or not to play the audio back for the smart speaker.

## Implementation

### Smart^2 Usage Modes

#### Normal operation/keyword evaluation mode
System relays all phrases to Alexa as long as they do not contain sensitive keywords, e.g. finance or security-related keywords. Examples:
> "password", "pin", "pin number", "bank account", "loan"

#### Total privacy mode (voice activated)
No information relayed to Alexa when activated.

#### Time-based keyword mode
No information relayed to Alexa for a predetermined amount of time after keyword/phrase is recognized. Example for use case:
> 1. System recognizes key-phrase "I hate" in spoken sentence "I hate my mother-in-law".
> 2. System immediately stops relaying audio to Alexa for 30 seconds, thus redacting information "my mother-in-law".
> 3. Such information could potentially be stored by Amazon and used for (unwanted) product recommendations, e.g. family therapy self-help book.

#### Argument mode
Privacy mode automatically activated when a preset decibel (dB) value is reached.

##### Implementation diagram
![Smart^2 implementation](/img/fig2-components.png?raw=true "Smart^2 implementation diagram")
> Fig. 3. Our test setup consists of the Smart2 along with a separate networked computer which records both the raw audio and the output from the Smart2. Both sets of audio recordings were transcribed using the online Google speech-to-text API, and compared.

## Test Data Summary
- Latency expressed in terms of %, e.g. 20 seconds (Alexa) / 2 seconds (Smart2) = 10% overhead increase.
- Average of several runs taken.
- Time recorded in milliseconds (timestamp in ms, e.g. 5000).
- Future improvement to latency: Another thread for recording Alexa.

![Smart^2 processing time](/img/proc-time-table.png?raw=true "Smart^2 processing time table")

### Test 1: "How is the weather?"
Alexa | Smart^2
----- | -----
ca. 1.8 - 2.10 s + 8 s for response | ca. 6.5 s

Difference of ca. 4.40 - 4.70 s
* 4.4 / 9.8 = 0.449
* 4.7 / 10.1 = 0.4653

> Smart2 adds 45%-46.5% overhead.

### Test 2: "Play CNN news."
Alexa | Smart^2
----- | -----
ca. 2.5-3.0 s until Alexa replies | ca. 6.45 s

Difference of ca. 3.45 - 3.95 s

### Test 3: "Tell me a joke."
Alexa | Smart^2
----- | -----
ca. 1.7 s | ca. 6.8 s

Difference of ca. 5.10 s

### Test 4: "What's 5+5?"
Alexa | Smart^2
----- | -----
3.68 s | 7.46 s

Difference of ca. 3.78 s

> The processing time of Smart2 is roughly 3-4 seconds. Roughly the same time Alexa needs to process a request and respond.
> Potential to improve latency exists by recording Alexa in a concurrently running thread.

## Additional Points
* Hardware vs. software mute buttons: software mute can be bypassed with malware (microphone appears to be deactivated but still sending data in the background).
* Other devices on the market, e.g. Google Home, Facebook Portal, are susceptible to vulnerabilities.
* Privacy Vulnerabilities of Encrypted IoT Traffic.
* Amazon stores recordings of past interactions; must be deleted manually: data collection details a profile of your lifestyle (interesting for marketers and cybercriminals who could obtain access with username/password obtained via security breaches (AWS, FB, etc.).
* Amazon Terms of Service: Amazon can use all captured data.
* Amazon Echo said to have analog hardware mute button that cuts of circuit flow to microphone. LED state tied electrically to the mic (same circuit).