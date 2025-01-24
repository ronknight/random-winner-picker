<h1 align="center">🎉 <a href="https://github.com/ronknight/random-winner-picker">Random Winner Picker</a></h1>

<h4 align="center">🛠️ A Python-based tool to fairly and randomly select a winner from a list of participants.</h4>

<p align="center">
<a href="https://twitter.com/PinoyITSolution"><img src="https://img.shields.io/twitter/follow/PinoyITSolution?style=social"></a>
<a href="https://github.com/ronknight?tab=followers"><img src="https://img.shields.io/github/followers/ronknight?style=social"></a>
<a href="https://github.com/ronknight/random-winner-picker/stargazers"><img src="https://img.shields.io/github/stars/BEPb/BEPb.svg?logo=github"></a>
<a href="https://github.com/ronknight/random-winner-picker/network/members"><img src="https://img.shields.io/github/forks/BEPb/BEPb.svg?color=blue&logo=github"></a>
<a href="https://youtube.com/@PinoyITSolution"><img src="https://img.shields.io/youtube/channel/subscribers/UCeoETAlg3skyMcQPqr97omg"></a>
<a href="https://github.com/ronknight/random-winner-picker/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/ronknight/random-winner-picker/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="https://github.com/ronknight"><img src="https://img.shields.io/badge/Made%20with%20%F0%9F%A4%8D%20by%20-%20Ronknight%20-%20red"></a>
</p>

<p align="center">
  <a href="#project-overview">Project Overview</a> •
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

---

## 📜 Project Overview
The Random Winner Picker is a simple yet powerful Python application designed to randomly and fairly pick a winner from a provided list of participants. Ideal for giveaways, contests, or any scenario where a random selection is required.

---

## ✨ Features
- **Fair Random Selection**: Ensures unbiased and random selection of winners.
- **Customizable Input**: Accepts a list of participants via text file or manual entry.
- **Lightweight and Easy to Use**: Minimal dependencies and straightforward setup.
- **Extensible**: Codebase designed for easy modification and additional features.

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ronknight/random-winner-picker.git
   cd random-winner-picker
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

1. Prepare your list of participants in a CSV file (e.g., `data.csv`), with each participant's email listed in the first column.
   Example of `data.csv`:
   ```csv
   email
   alice@example.com
   bob@example.com
   charlie@example.com
   ```

2. Run the script:
   ```bash
   python app.py
   ```

3. The script will:
   - Load the participant data from the specified CSV file.
   - Simulate a "spinning wheel" animation to pick a random winner.
   - Display the winner in the console output.

4. Example Output:
   ```
   Welcome to the Random Winner Picker! 🎲
   Spinning the wheel: 100%|################| 30/30 [00:09<00:00,  3.28it/s]

   🎉 And the winner is... 🎉

   🌟 alice@example.com! Congratulations! 🌟
   ```

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your branch:
   ```bash
   git commit -m "Add new feature"
   git push origin feature-name
   ```
4. Open a pull request on GitHub.

---

## 📜 License

This project is licensed under the [MIT License](https://github.com/ronknight/random-winner-picker/blob/master/LICENSE).

---

## ❤️ Acknowledgements
Special thanks to the open-source community for inspiring and supporting this project.

---

## ⚠️ Disclaimer
This tool is designed for educational and entertainment purposes. The developer assumes no responsibility for misuse.

