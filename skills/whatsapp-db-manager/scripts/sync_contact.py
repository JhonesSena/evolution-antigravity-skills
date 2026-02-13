import argparse
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def sync_contact(jid, name):
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        cur = conn.cursor()
        
        # Limpar JID para salvar apenas o número
        clean_id = jid.split('@')[0]
        
        query = """
        INSERT INTO wa_contacts (whatsapp_id, name, last_interaction)
        VALUES (%s, %s, CURRENT_TIMESTAMP)
        ON CONFLICT (whatsapp_id) 
        DO UPDATE SET name = EXCLUDED.name, last_interaction = CURRENT_TIMESTAMP;
        """
        
        cur.execute(query, (clean_id, name))
        conn.commit()
        print(f"✅ Contato {clean_id} sincronizado.")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"❌ Erro no DB: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--jid", required=True)
    parser.add_argument("--name", required=True)
    args = parser.parse_args()
    sync_contact(args.jid, args.name)