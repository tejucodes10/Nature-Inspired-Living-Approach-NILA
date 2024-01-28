# 🚗 Route Optimizer Kiosk Bot

Demo Screenshot - https://drive.google.com/file/d/1B_EyqoDGxea9SGq79dOOUGiDSDq0Ruuo/view?usp=sharing
![llm](https://github.com/tejucodes10/Team-FinSAT-Pragyan-24-Hackathon-PS-3/assets/119094222/2d2818f9-9293-4819-a636-31fdcf88b05c)

## Overview

Make It Mine is an eco-conscious route optimizer kiosk bot designed to guide users in finding environmentally friendly routes for their journeys. Deployable in major transportation hubs like bus stands and railway stations, this bot empowers individuals to plan trips in an energy-optimized manner.

## 🚀 Implementation with Pathway and LLMs

This project harnesses the power of the Pathway open-source framework, providing a robust backbone for high-throughput and low-latency real-time data processing. With Pathway handling infrastructure and low-level details, developers can focus on implementing business logic in Python and seamlessly integrate advanced language models (LLMs) for enhanced interactions.

## 🏁 Quick Start

Get the Make It Mine Route Optimizer Kiosk Bot up and running in just 5 minutes:

1. Install project dependencies inside an isolated virtual environment using Python Poetry:

    ```bash
    $ make init
    ```

2. Create an `.env` file and input the required credentials, including the OpenAI API Key and Discord Webhook:

    ```bash
    $ cp .env.example .env
    ```

3. Run the virtual assistant:

    ```bash
    $ make run
    ```

4. Initiate the first request to the bot:

    ```bash
    $ make request
    ```

5. Simulate the push of the first event to the data warehouse:

    ```bash
    $ make push_first_event
    ```

6. Simulate the push of the second event to the data warehouse:

    ```bash
    $ make push_second_event
    ```

## 🌟 Features

- **Energy-Optimized Route Planning:** Make It Mine suggests routes optimized for energy efficiency, promoting eco-friendly transportation.

- **Kiosk Deployment:** Easily deploy the bot in major transportation hubs, such as bus stands and railway stations, making it accessible to travelers.

- **Seamless Integration with LLMs:** Pathway's compatibility with LLMs ensures a smooth integration process, enabling the bot to leverage advanced language models for enhanced interactions.

## 🤖 Usage

Users can approach the kiosk and interact with the bot using natural language. For example:

- **User:** "I want to go to Velachery from Sholinganallur."
- **Bot:** Recommends the most energy-optimized route, considering various factors such as traffic and environmental impact.

## 🤝 Contribution

Contributions to the Make It Mine Route Optimizer Kiosk Bot project are highly welcomed. Feel free to fork the repository, make improvements, and submit pull requests.

## 🌐 ESG and UN Sustainable Goals Alignment

Make It Mine aligns strongly with Environmental, Social, and Governance (ESG) principles and UN Sustainable Development Goals. The bot's emphasis on energy-efficient route planning contributes to sustainability objectives.

## 🎉 Praise for Pathway

This project acknowledges and praises the effectiveness of the Pathway framework. For detailed information, please refer to the [Pathway documentation](https://pathway-docs.example).

Pathway's LLM (Large Language Model) App is a Python library that helps you create and launch AI-powered applications based on the most up-to-date knowledge available in your data sources. You can use it to answer natural language queries asked by your users, or to run data transformation pipelines with LLM's.

## Why LLM App?
Simplicity - Simplifies your AI pipeline by consolidating capabilities into one platform. No need to integrate and maintain separate modules for your Gen AI app: Vector Database (e.g. Pinecone/Weaviate/Qdrant) + Framework for LLM chaining + Cache (e.g. Redis) + API Framework (e.g. Fast API).
Real-time data syncing - Syncs both structured and unstructured data from diverse sources, enabling real-time Retrieval Augmented Generation (RAG).
Easy alert setup - Configure alerts for key business events with simple configurations. Ask a question, and get updated when new info is available.
Scalability - Handles heavy data loads and usage without degradation in performance. Metrics help track usage and scalability. Learn more about the performance of the underlying Pathway data processing framework.
Monitoring - Provide visibility into model behavior via monitoring, tracing errors, anomaly detection, and replay for debugging. Helps with response quality.
Security - Designed for the enterprise with capabilities like Personally Identifiable Information (PII) detection, content moderation, permissions, and version control. Run this in your private cloud with local LLMs.
Unification - You can cover multiple aspects of your choice with a unified application logic: back-end, embedding, retrieval, LLM tech stack.


![image](https://github.com/tejucodes10/Team-FinSAT-Pragyan-24-Hackathon-PS-3/assets/119094222/05fa14cf-19fd-4b0d-b72a-fb21377f08ea)
