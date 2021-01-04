# Smart^2 Speaker Blocker

## Project Goal
Develop a smart filter to give users more control over speech data sent over the network, ensuring privacy in their home.

## Resources Used
* Mini-ITX PC w/ Ubuntu
* Ext. microphone and Bluetooth speaker
* Amazon Echo Dot
* Open-source software
  * PyPi SpeechRecognition library
  * CMU PocketSphinx
  * Simple Google™ TTS (with pico2wave offline speech synthesis back-end)

## Smart^2 Usage Modes
### Normal operation/keyword evaluation mode
System relays all phrases to Alexa as long as they do not contain sensitive keywords, e.g. finance or security-related keywords. Examples:
> "password", "pin", "pin number", "bank account", "loan"

### Total privacy mode (voice activated)
No information relayed to Alexa when activated.

### Time-based keyword mode
No information relayed to Alexa for a predetermined amount of time after keyword/phrase is recognized. Example for use case:
> 1. System recognizes key-phrase "I hate" in spoken sentence "I hate my mother-in-law".
> 2. System immediately stops relaying audio to Alexa for 30 seconds, thus redacting information "my mother-in-law".
> 3. Such information could potentially be stored by Amazon and used for (unwanted) product recommendations, e.g. family therapy self-help book.

### Argument mode
Privacy mode automatically activated when a certain dB is reached.

## Additional Points
* Hardware vs. software mute buttons – s/w mute can be bypassed with malicious software (appears to be active but still sending data in the background)
* Other devices on the market and vulnerabilities – Facebook Portal
* Privacy Vulnerabilities of Encrypted IoT Traffic
* Amazon stores recordings of past interactions; must be deleted manually – data collection details a profile of your lifestyle (interesting for marketers and cybercriminals who could obtain access with username/password obtained via security breaches (AWS, FB, etc.).
* Amazon Terms of Service – Amazon can use all captured data.
* Amazon Echo said to have analog h/w mute button that cuts of circuit flow to the mic. LED state tied electrically to the mic (same circuit).
