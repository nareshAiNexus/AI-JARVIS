# 🤖 Jarvis AI Assistant

**Jarvis AI Assistant** is a desktop-based Python voice assistant. It listens to your voice commands and responds through speech and a GUI chat window. Jarvis can play YouTube videos, tell the time, and answer questions using the local LLaMA3 model via Ollama.

---

## ✨ Features

* 🎙️ Real-time voice recognition using Google Speech Recognition
* 🗣️ Text-to-speech responses using `pyttsx3`
* 🔍 General knowledge answers using locally hosted `llama3` via `ollama`
* 📺 Play YouTube content with voice (`play [song name]`)
* 🕒 Time updates (`what is the time`)
* 🖱️ Right-click copy from chat history
* 💬 Scrollable chat GUI using Tkinter
* 🧵 Background listening with multithreading

---

## 🛠️ Requirements

Make sure Python is installed. Then install the following dependencies:

```bash
pip install speechrecognition pyttsx3 pywhatkit wikipedia
```

Additionally, install and run [Ollama](https://ollama.com/download), and download the LLaMA3 model:

```bash
ollama run llama3
```

---

## 🚀 Getting Started

1. **Clone this repository**:

```bash
git clone https://github.com/yourusername/jarvis-ai-assistant.git
cd jarvis-ai-assistant
```

2. **Run the assistant**:

```bash
python main.py
```

3. **Give voice commands**, such as:

* `Play Believer by Imagine Dragons`
* `What is the time?`
* `Tell me about the moon landing`
* `Exit` or `Goodbye` to quit

---

## 📁 Project Structure

* `main.py`: Main script containing GUI, voice processing, and LLaMA3 integration
* Uses subprocess to call:

  ```bash
  ollama run llama3 "<your-query>"
  ```
* Multithreading ensures the GUI remains responsive

---

## ⚙️ Customization

* Change the voice (male/female) in `main.py` via:

  ```python
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female
  ```

* You can add more command handling in the `respond()` function

---

## ❗ Troubleshooting

* Ensure your microphone is enabled and accessible
* If `ollama` throws an error, verify the model is downloaded and `ollama` is running
* Run the script in an environment where audio output is allowed

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

Feel free to fork and experiment!
