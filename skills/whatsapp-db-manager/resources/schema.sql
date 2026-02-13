CREATE TABLE IF NOT EXISTS wa_contacts (
    id SERIAL PRIMARY KEY,
    whatsapp_id VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(255),
    last_interaction TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    source VARCHAR(50) DEFAULT 'EvolutionAPI'
);