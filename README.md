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
