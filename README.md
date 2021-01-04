# Smart^2 Speaker Blocker

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

## Additional Points
* Hardware vs. software mute buttons: software mute can be bypassed with malware (microphone appears to be deactivated but still sending data in the background).
* Other devices on the market, e.g. Google Home, Facebook Portal, are susceptible to vulnerabilities.
* Privacy Vulnerabilities of Encrypted IoT Traffic.
* Amazon stores recordings of past interactions; must be deleted manually: data collection details a profile of your lifestyle (interesting for marketers and cybercriminals who could obtain access with username/password obtained via security breaches (AWS, FB, etc.).
* Amazon Terms of Service: Amazon can use all captured data.
* Amazon Echo said to have analog hardware mute button that cuts of circuit flow to microphone. LED state tied electrically to the mic (same circuit).