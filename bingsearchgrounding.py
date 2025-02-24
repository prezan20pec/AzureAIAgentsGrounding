import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import BingGroundingTool
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv(Path(".env"))

# Initialize project client
project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.getenv("PROJECT_CONNECTION_STRING"),
)

# Get Bing connection ID
conn_id = project_client.connections.get(connection_name=os.getenv("BING_CONNECTION_NAME")).id

# Initialize Bing grounding tool
bing_tool = BingGroundingTool(connection_id=conn_id)

# Create AI agent with Bing search capabilities
agent = project_client.agents.create_agent(
    model=os.getenv("DEPLOYMENT_NAME"),
    name="my-assistant",
    instructions="You are a helpful assistant",
    tools=bing_tool.definitions,
    headers={"x-ms-enable-preview": "true"},
)

# Function to fetch real-time information
def fetch_info(query):
    thread = project_client.agents.create_thread()
    project_client.agents.create_message(thread_id=thread.id, role="user", content=query)
    run = project_client.agents.create_and_process_run(thread_id=thread.id, assistant_id=agent.id)
    if run.status == "failed":
        return f"Error: {run.last_error}"
    return project_client.agents.list_messages(thread_id=thread.id)

# Example queries
queries = [
    "What is the current weather in New York?",
    "Latest stock market trends",
    "Today's top news headlines"
]

for q in queries:
    print(f"Query: {q}")
    print(fetch_info(q))

# Cleanup - Delete the assistant
project_client.agents.delete_agent(agent.id)
