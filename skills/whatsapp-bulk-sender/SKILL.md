---
name: whatsapp-bulk-sender
description: Envia mensagens em massa para uma lista de contatos via Evolution API. Use quando o usuário fornecer uma lista de números e um texto.
---

# WhatsApp Bulk Sender Skill

## Goal
Enviar mensagens de forma segura para múltiplos destinatários, respeitando intervalos humanos para evitar bloqueios.

## Instructions
1. **Inputs**: Extraia a lista de números e a mensagem do usuário.
2. **Execução**: Utilize o script procedural `scripts/bulk_send.py`.
   - Comando: `python scripts/bulk_send.py --numbers "5511999999999,5511888888888" --message "Olá!"`
3. **Delay**: O script gerencia automaticamente delays entre 20 e 45 segundos.

## Constraints
- Máximo de 50 contatos por execução.
- Requer `EVOLUTION_URL` e `EVOLUTION_API_KEY` no arquivo `.env`.