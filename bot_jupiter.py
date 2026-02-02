import requests
import json
import time

# JUPITER V6 API ENDPOINT
JUPITER_QUOTE_API = "https://quote-api.jup.ag/v6/quote"

# Token Mints (Solana Mainnet)
SOL_MINT = "So11111111111111111111111111111111111111112"
USDC_MINT = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"

def get_jupiter_quote(input_mint, output_mint, amount_lamports, slippage_bps=50):
    """
    Récupère une cotation (quote) via l'agrégateur Jupiter.
    Ne nécessite pas de signature, juste une lecture publique.
    """
    params = {
        "inputMint": input_mint,
        "outputMint": output_mint,
        "amount": amount_lamports,  # En unités atomiques (lamports pour SOL)
        "slippageBps": slippage_bps
    }
    
    try:
        response = requests.get(JUPITER_QUOTE_API, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"❌ Erreur Jupiter: {e}")
        return None

def run_demo():
    print("--- 🔵 VIBESHIP FinTech Agent: Jupiter Integration Demo ---")
    
    # Scénario : On veut échanger 1 SOL contre de l'USDC
    amount_sol = 1.0
    amount_lamports = int(amount_sol * 1_000_000_000) # 1 SOL = 10^9 Lamports
    
    print(f"📡 Récupération d'une quote pour {amount_sol} SOL -> USDC...")
    
    quote = get_jupiter_quote(SOL_MINT, USDC_MINT, amount_lamports)
    
    if quote:
        out_amount = int(quote.get('outAmount', 0))
        out_usdc = out_amount / 1_000_000 # USDC a 6 décimales
        price_impact = quote.get('priceImpactPct', '0')
        
        print(f"✅ Quote reçue !")
        print(f"   Montant estimé : {out_usdc:.2f} USDC")
        print(f"   Impact prix    : {price_impact}%")
        print(f"   Route          : {len(quote.get('routePlan', []))} hops via DEXs")
        print("---")
        print("💡 Note: Pour exécuter ce trade, l'Agent DevOps doit configurer")
        print("   le Wallet sécurisé et signer la transaction retournée par /swap.")
    else:
        print("⚠️ Impossible de récupérer la quote.")

if __name__ == "__main__":
    run_demo()
