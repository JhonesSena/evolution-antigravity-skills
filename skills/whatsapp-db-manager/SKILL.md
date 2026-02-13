---
name: whatsapp-db-manager
description: Sincroniza informações de contatos (nome e número) com o banco de dados PostgreSQL. Use para registrar leads ou atualizar o cadastro de alunos/clientes.
---

# WhatsApp DB Manager Skill

## Instructions
1. **Schema**: Se for a primeira vez, execute o arquivo SQL em `resources/schema.sql`.
2. **Sync**: Capture o `remoteJid` e o `pushName` e execute:
   - Comando: `python scripts/sync_contact.py --jid "5511..." --name "Jhones"`

## Constraints
- Use apenas o campo `id` como chave primária conforme definido no schema.