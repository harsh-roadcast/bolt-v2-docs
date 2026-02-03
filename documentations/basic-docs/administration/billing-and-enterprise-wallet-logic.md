---
description: >-
  The system manages financial transactions through an internal Wallet system,
  supporting two distinct enterprise models.
---

# Billing & Enterprise Wallet Logic

### Centralized Billing Model

**Concept:** The Parent Organization acts as the "Bank."

* **Logic:** All Child Branches share a single pool of funds.
* **Case:** Even if a Child Branch has no individual budget, it can perform transactions (like license upgrades) as long as the Parent Wallet has a balance.

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

### Decentralized Billing Model

**Concept:** Each node is a "Siloed Entity."

* **Logic:** Every Branch must maintain its own independent wallet.
* **Case (Critical Security):** If a Child Branch has a $0 balance, a purchase attempt will trigger an instant failure. The system **will not** fallback to the Parent Wallet, ensuring strict budget isolation between franchises or independent units.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

