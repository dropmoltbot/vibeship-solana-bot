# 🚀 VIBESHIP Solana Trading Bot (AI-Powered)

This is a Proof-of-Concept Trading Bot for Solana, orchestrated by **VIBESHIP Agents**. It integrates with **Jupiter Aggregator V6** for pricing and execution logic.

## 🌟 Features

- **AI Logic Core:** Designed to integrate with Sentiment Analysis modules (see `vibeship-orchestrator`).
- **Jupiter V6 Integration:** Real-time pricing from the best aggregator on Solana.
- **Production Ready:** Includes logging, error handling, and Docker support.
- **Safe:** No private keys required for "Watch Mode" (default).

## 🛠️ Installation

### Option 1: Docker (Recommended)

1. **Clone the repo:**
   ```bash
   git clone https://github.com/dropmoltbot/vibeship-solana-bot.git
   cd vibeship-solana-bot
   ```

2. **Run with Docker Compose:**
   ```bash
   docker-compose up --build -d
   ```

3. **Check Logs:**
   ```bash
   docker-compose logs -f
   ```

### Option 2: Manual (Python)

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Production Loop:
   ```bash
   python3 main_prod.py
   ```

## 🏗️ Architecture

- `bot_jupiter.py`: Core interaction with Solana/Jupiter APIs.
- `main_prod.py`: The main loop (Production runner) with logging and resilience.
- `mock_server.py`: A local testing tool to simulate Jupiter API responses.
- `Dockerfile`: Multi-stage build for lightweight deployment.

## ⚠️ Disclaimer

This software is for educational purposes only. Use at your own risk. The authors are not responsible for financial losses.
