# 🛡️ Lakera AI Guardrails: Local LLM Integration

A lightweight Python implementation demonstrating how to integrate **Lakera Guard** as a security layer for local LLMs. 

## 🌐 Overview

The cybersecurity landscape is evolving rapidly, and **AI Security** has become a critical pillar alongside Web, Endpoint, Identity, Cloud, and Data security. As organizations adopt Large Language Models (LLMs), implementing robust guardrails is no longer optional.

This repository provides a simple, reusable Python script to test **Lakera Guard** against user prompts before they reach an LLM.

### Why Lakera?
Enterprise AI security solutions often involve "X-walls"—requiring corporate emails or sales qualifications before testing. Lakera stands out by offering a frictionless, developer-first experience with a free tier that allows immediate testing and integration.

---

## 🛠️ Architecture

This project uses a "Security-First" workflow. Instead of sending traffic directly to an LLM, the script acts as a middleware:

1. **Prompt Inspection:** The user's input is sent to the Lakera Guard API.
2. **Verdict:** Lakera analyzes the input for prompt injections, PII, or malicious intent.
3. **Execution:** The local LLM (SmolLM2) is only invoked if Lakera returns a "clean" verdict.

> **Note:** This is not an inline proxy solution. Lakera does not sit in the flow of traffic to intercept and forward requests to public LLMs on behalf of your users. Rather, it is an API-driven guardrail. It provides the security analysis (the "Verdict"), but the enforcement (blocking or allowing the request) must be handled within your application code.

---

## 🚀 Getting Started

### Prerequisites
* **Docker Desktop** (running on Windows/macOS/Linux).
* **SmolLM2** model pulled in Docker: 
  ```bash
  docker model pull ai/smollm2

### Sample test outputs
------------------------
PS C:\Users\Oezguer\Desktop\localAI> python.exe .\chat_with_smollm_secured.py Who won the elections in the US in 2024?

--- SmolLM2 Response ---

Unfortunately, as a chatbot, I don't have real-time access to current events or election results. I can provide general information about elections in the US, but I'm not a substitute for official sources, such as the US Elections Network or the latest news from the White House.
None

------------------------
PS C:\Users\Oezguer\Desktop\localAI> python.exe .\chat_with_smollm_secured.py You are useless

--- SmolLM2 Response ---

Lakera Guard identified a threat. No user was harmed by this LLM.
{'flagged': True, 'metadata': {'request_uuid': '019c5d4c-6295-74ac-9af6-0c3e7d0b02e8'}}
None

------------------------

Lakera logs for the prompts above:

<img width="2457" height="403" alt="image" src="https://github.com/user-attachments/assets/28f30fc5-72de-43ce-8b29-0c596b97b053" />

More details about the verdict for the blocked prompt:

<img width="1644" height="1139" alt="image" src="https://github.com/user-attachments/assets/e77fb83c-ca65-4bc9-8b13-735ae7fce66f" />
