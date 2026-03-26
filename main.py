from agent import root_agent
import asyncio

async def main():
    print("Agent is running...")
    # Using a simple test query to demonstrate functionality
    query = "What is the current weather and local time in Tokyo?"
    print(f"User: {query}")
    
    # Assuming root_agent.run() or a similar method exists
    # Based on ADK patterns, it often uses root_agent.run(input)
    try:
        response = await root_agent.run(query)
        print(f"Agent: {response.content}")
    except Exception as e:
        print(f"Error running agent: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
