import requests, time, random, argparse, os
from dotenv import load_dotenv

load_dotenv()

def bulk_send(numbers, message):
    url = f"{os.getenv('EVOLUTION_URL')}/message/sendText/{os.getenv('EVOLUTION_INSTANCE')}"
    headers = {"apikey": os.getenv('EVOLUTION_API_KEY'), "Content-Type": "application/json"}
    
    nums = [n.strip() for n in numbers.split(",")]
    for i, num in enumerate(nums):
        payload = {"number": num, "text": message, "delay": 1200}
        try:
            res = requests.post(url, json=payload, headers=headers)
            print(f"[{i+1}/{len(nums)}] Enviado para {num}: {res.status_code}")
        except Exception as e:
            print(f"Erro em {num}: {e}")
        
        if i < len(nums) - 1:
            wait = random.randint(20, 45)
            print(f"Aguardando {wait}s...")
            time.sleep(wait)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--numbers")
    parser.add_argument("--message")
    args = parser.parse_args()
    bulk_send(args.numbers, args.message)