import asyncio
from agent import get_weather_and_time

async def test():
    print("Testing London (DST)...")
    print(get_weather_and_time("London"))
    
    print("\nTesting New York (DST)...")
    print(get_weather_and_time("New York"))
    
    print("\nTesting Sydney (DST)...")
    print(get_weather_and_time("Sydney"))

if __name__ == "__main__":
    asyncio.run(test())
