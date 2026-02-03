---
title: graph TD    subgraph "Paren...
---



```mmd
graph TD
    subgraph "Parent Level"
        PW[("💰 Main Enterprise Wallet<br/>(Balance: $10,000)")]
    end

    subgraph "Child Level (Shared Access)"
        C1[Branch A]
        C2[Branch B]
        C3[Branch C]
    end

    C1 -- "Draws Funds" --> PW
    C2 -- "Draws Funds" --> PW
    C3 -- "Draws Funds" --> PW

    style PW fill:#e1f5fe,stroke:#01579b,stroke-width:2px
// Some code
```
