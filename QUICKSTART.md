# Quick Start Guide for Automated Spot Trading Bot

## Introduction
Welcome to the Automated Spot Trading Bot! This guide will walk you through the necessary steps to set up and run the bot for beginners.

## Step 1: Install Python
1. **Download Python**: Go to the [Python official website](https://www.python.org/downloads/) and download the latest version for your operating system.
2. **Install Python**: Follow the installation instructions specific to your OS. Make sure to check the box that says "Add Python to PATH" during installation.

## Step 2: Clone the Repository
Open your terminal (Command Prompt on Windows, Terminal on macOS/Linux) and run the following command:
```bash
git clone https://github.com/musawirkhan873-oss/automated-spot-trading-bot.git
```
Navigate into the cloned directory:
```bash
cd automated-spot-trading-bot
```

## Step 3: Set Up a Virtual Environment
It is recommended to use a virtual environment to manage dependencies:
```bash
# For Windows:
python -m venv venv

# For macOS/Linux:
python3 -m venv venv
```
Activate the virtual environment:
```bash
# For Windows:
venv\Scripts\activate

# For macOS/Linux:
source venv/bin/activate
```

## Step 4: Install Dependencies
Ensure you have `pip` updated, then run:
```bash
pip install -r requirements.txt
```

## Step 5: Get Binance API Keys
1. Go to the [Binance website](https://www.binance.com/) and create an account if you don't have one.
2. Once logged in, go to the API Management section.
3. Create a new API key, label it accordingly, and note down both the API key and Secret. Keep them secure!

## Step 6: Configure the Bot
1. In the cloned directory, locate the `config.py` file (or similar configuration file).
2. Open it in a text editor and input your Binance API keys:
   ```python
   API_KEY = 'your_api_key_here'
   API_SECRET = 'your_api_secret_here'
   ```

## Step 7: Run the Bot in Paper Trading Mode
To start the bot for paper trading, run the following command:
```bash
python main.py --mode paper
```
This will ensure that you're testing the bot without using real funds.

## Conclusion
Congratulations! You have successfully set up the Automated Spot Trading Bot. Happy trading!