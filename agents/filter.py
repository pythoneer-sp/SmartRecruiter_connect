# agents/filter.py
import asyncio
import json
from droidrun import DroidAgent

async def filter_profile(profile_url, keywords, config):
    """Analyze profile and check if it's a recruiter"""
    agent = DroidAgent(
        goal=f"Open LinkedIn profile {profile_url} and analyze the job title. Check if title contains any of these keywords: {keywords}. Return name, title, and whether it's a recruiter.",
        config=config,
        max_steps=10
    )
    
    result = await agent.run()
    
    # Mock response for demo - in real implementation, parse the agent output
    return {
        "name": "Sample Recruiter",
        "title": "Technical Recruiter",
        "is_recruiter": True,
        "confidence": "high"
    }