# Azure AI Agents Grounding with Bing Search

## Overview
This repository provides a workaround for the **Bing Search API resource creation issue** in the Azure Portal. Since Microsoft has restricted new customers from adding Bing resources, this solution leverages the **Bing Grounding Tool** within **Azure AI Agents** to fetch real-time information.

## Use Case
The Bing Grounding Tool can be used to retrieve **real-time data** for various applications, including:
- **Live weather updates**
- **Current news headlines**
- **Stock market trends**
- **General knowledge queries**

## Workaround Solution
Instead of directly using the Bing Search API, this project demonstrates how to integrate **Bing Grounding Tool** within **Azure AI Agents**.

### Key Features:
✅ Uses **Azure AI Agents** for web search operations  
✅ Supports **real-time web data retrieval**  
✅ Compatible with **Azure AI Projects**  

## Setup & Usage
To set up and run the project, follow these steps:

### 1️⃣ Prerequisites
Ensure you have the following installed:
- Python 3.8+
- `azure-ai-projects`
- `azure-identity`
- `.env` file with your **Azure AI credentials**  

### 2️⃣ Install Dependencies
```bash
pip install azure-ai-projects azure-identity
```

### 3️⃣ Set Environment Variables
Create a `.env` file with the following details:
```env
PROJECT_CONNECTION_STRING=<your_connection_string>
DEPLOYMENT_NAME=<your_deployment_name>
BING_CONNECTION_NAME=<your_bing_connection_name>
```

### 4️⃣ Run the Script
Execute the script to retrieve real-time search results:
```bash
python bingsearchgrounding.py
```

### Example Queries
You can modify the script to fetch:
- `"What is the current weather in New York?"`
- `"Latest stock market trends"`
- `"Today's top news headlines"`

## Microsoft Restrictions
⚠️ **Important Notice:** Microsoft has restricted new customers from creating Bing Search API resources. This workaround is only applicable using **Azure AI Agents**.  
📌 Microsoft has also stated that **data sent via Bing Grounding Tool may be used to improve Microsoft products and services**.

## References
- [Microsoft Bing Grounding Tool Documentation](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview)
- [Discussion on Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/2156511/your-account-is-not-approved-for-this-resource-err)

## License
This repository is provided for educational and testing purposes. Use it at your own discretion.
