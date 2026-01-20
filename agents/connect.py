# agents/connect.py
import asyncio
from droidrun import DroidAgent

async def send_connection_request(name, message_text, config):
    """Send connection request with personalized note"""
    print(f"  🤝 Sending connection request to {name}...")
    
    agent = DroidAgent(
        goal=f"Click Connect button on this LinkedIn profile. Add a note and paste exactly: {message_text}. Then send.",
        config=config
    )
    
    result = await agent.run()
    
    if result.success:
        print(f"    ✓ Connection request sent!")
        return True
    else:
        print(f"    ❌ Failed: {result.reason}")
        return False