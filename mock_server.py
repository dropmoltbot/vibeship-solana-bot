from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import random
import time

PORT = 8080

class MockJupiterHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/v6/quote"):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            # Simulation de prix SOL fluctuant autour de $100
            base_price = 100.0
            variation = random.uniform(-2.0, 2.0)
            current_price = base_price + variation
            
            # 0.5 SOL = 50 USDC (approx)
            in_amount = 500_000_000 # 0.5 SOL en lamports
            out_amount = int((in_amount / 1_000_000_000) * current_price * 1_000_000)
            
            mock_response = {
                "inputMint": "So11111111111111111111111111111111111111112",
                "inAmount": str(in_amount),
                "outputMint": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
                "outAmount": str(out_amount),
                "otherAmountThreshold": str(int(out_amount * 0.995)),
                "swapMode": "ExactIn",
                "slippageBps": 50,
                "platformFee": None,
                "priceImpactPct": f"{random.uniform(0.01, 0.1):.4f}",
                "routePlan": [{"swapInfo": {"label": "Raydium"}, "percent": 100}],
                "contextSlot": 123456789,
                "timeTaken": 0.0123
            }
            
            self.wfile.write(json.dumps(mock_response).encode())
            print(f"[MOCK-SERVER] Served Quote: 0.5 SOL -> {current_price/2:.2f} USDC")
        else:
            self.send_response(404)
            self.end_headers()

def run_server():
    print(f"🌟 Starting Jupiter Mock Server on localhost:{PORT}...")
    server = HTTPServer(('localhost', PORT), MockJupiterHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        server.server_close()

if __name__ == '__main__':
    run_server()
