Here's a **README.md** file for your voice assistant project, ready to use in your GitHub repository:

---

# 🧠 Rajendra's – Voice-Controlled Personal Assistant

**GIRI** is a Python-based voice assistant that performs various tasks using voice commands. It can play songs, tell jokes, fetch Wikipedia summaries, open applications, set reminders, and even provide emotional comfort — all through natural conversation.

---

## 🎯 Features

* 🎧 Voice recognition using `SpeechRecognition` + Google API
* 🗣️ Text-to-speech output with `pyttsx3` (offline engine)
* 🎵 Play songs on YouTube via `pywhatkit`
* 📚 Get one-line Wikipedia summaries
* 😂 Random programming jokes via `pyjokes`
* ⏰ Custom voice-based reminder system
* 💻 Open Chrome or VS Code through voice
* ❤️ Comforting responses when user feels lonely
* 📝 Stores user and assistant dialogue in `chat_memory.txt`

---

## 🛠️ Installation

**1. Clone the repository:**

```bash
git clone https://github.com/yourusername/giri-voice-assistant.git
cd giri-voice-assistant
```

**2. Install dependencies:**

```bash
pip install -r requirements.txt
```

If `pyaudio` gives errors during installation, install it using a prebuilt wheel:

* Windows: [https://www.lfd.uci.edu/\~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
* macOS/Linux: Use `brew install portaudio` or your system's package manager.

---

## 📦 Requirements

Your `requirements.txt` should include:

```
speechrecognition
pyttsx3
pywhatkit
wikipedia
pyjokes
pyaudio
```

---

## ▶️ How to Use

Simply run the main script:

```bash
python giri.py
```

Start giving voice commands such as:

* `"Play Shape of You"`
* `"What’s the time?"`
* `"Who is Elon Musk?"`
* `"Tell me a joke"`
* `"Remind me to take a break in 10 minutes"`
* `"I feel lonely"`

To stop the assistant, say **“exit”** or **“stop”**.

---

## 🗂️ Project Structure

```
giri-voice-assistant/
├── giri.py                # Main assistant script
├── chat_memory.txt        # Conversation history (auto-generated)
└── README.md              # Project description
```

---

## 👨‍💻 Author

**Rajendra**
If you like this project, consider giving it a ⭐️ on GitHub!

---

## 🛡️ Disclaimer

This assistant uses Google’s free speech recognition API, which requires internet access. It is a local assistant otherwise and does **not** store or share data externally.

---

Let me know if you'd like to add a logo, screenshots, or setup instructions for a `.exe` version too!
