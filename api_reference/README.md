---
description: Learn more about documenting APIs in GitBook.
icon: terminal
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
metaLinks:
  alternates:
    - https://app.gitbook.com/s/M9ty6FYa3j98VSBHF9LN/
---

# Consume & Push APIs

**Version:** 2.0\
**Last Updated:** 2026-02-11 UTC

This documentation defines the enterprise integration specifications for:

1. Consume Position API (Device → Server ingestion)
2. Position Push API (Server → Client data delivery)
3. Events Push API (Server → Client data delivery)

***

### Architecture Overview

#### Data Ingestion Flow

Device → Middleware → Consume API → Processing Engine → Storage

#### Data Push Flow

Device → Platform → Client Endpoint

***

All timestamps are in UTC.\
Coordinate system: WGS‑84.
