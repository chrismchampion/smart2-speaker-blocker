Project goals:
    • Develop a smart filter to give users more control over speech data sent over the network, ensuring privacy in their home

Resources used:
    • Mini-ITX PC w/ Ubuntu
    • Ext. microphone and Bluetooth speaker
    • Amazon Echo Dot
    • Add. open-source software:
        ◦ PyPi SpeechRecognition library
        ◦ CMU PocketSphinx
        ◦ Simple Google™ TTS (with pico2wave offline speech synthesis back-end)

Program functionality/modes:
    • Normal operation/keyword evaluation mode – System relays all phrases to Alexa as long as they do not contain sensitive keywords, e.g., finance/security-related: password, pin, pin number, bank account, loan.
    • Total privacy mode (voice activated) – No information relayed to Alexa when activated
    • Time-based keyword mode – No information relayed to Alexa for a predetermined amount of time when keyword is heard. Example: halt system for a minute when expletives identified or “I hate...” (example - “I hate my wife” →Interaction relayed to and stored by Amazon → unwanted Amazon divorce book recommendation).
    • Argument mode – Privacy mode automatically activated when a certain dB is reached.

Other points:
    • Hardware vs. software mute buttons – s/w mute can be bypassed with malicious software (appears to be active but still sending data in the background)
    • Other devices on the market and vulnerabilities – Facebook Portal
    • Privacy Vulnerabilities of Encrypted IoT Traffic
    • Amazon stores recordings of past interactions; must be deleted manually – data collection details a profile of your lifestyle (interesting for marketers and cybercriminals who could obtain access with username/password obtained via security breaches (AWS, FB, etc.)
    • Amazon Terms of Service – Amazon can use all captured data?

Enhancement Ideas:
Append list (set?) of "redacted" keywords using voice recognition? --> no
thisset = set(("k1", "k2", ..., "kn"))

Trigger keyword,
e.g. "OK Heidi" -> get command & save to cmd.wav -> play audio "Hey, Alexa" + cmd.wav

1. Playing back everything in a phrase before and after a spec. keyword
2. Time-based privacy mode, e.g. "... girlfriend..." turns privacy mode on for 5 minutes (w/ countdown timer)

Notes:
Amazon Echo said to have analog h/w mute button that cuts of circuit flow to the mic. LED state tied electrically to the mic (same circuit).

Paper:
Check privacy statements / ToS -> Amazon can use all data they capture


https://ws680.nist.gov/publication/get_pdf.cfm?pub_id=923459
https://dl.acm.org/citation.cfm?id=3052562
https://arxiv.org/abs/1705.06809
https://arxiv.org/abs/1705.06805
https://arxiv.org/abs/1708.05044
