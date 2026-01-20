# agents/search.py
import asyncio
import re
from droidrun import DroidAgent

def parse_single_profile(steps):
    """Extract ONE profile from DroidRun steps"""
    for step in steps:
        result_text = str(step.get('result', '')) + str(step.get('output', ''))
        
        # Look for LinkedIn profile pattern
        match = re.search(r'(?:https?://)?(?:www\.)?linkedin\.com/in/([a-zA-Z0-9\-]+)', result_text)
        if match:
            profile_url = f"https://linkedin.com/in/{match.group(1)}"
            
            # Try to extract name from nearby text
            name = "Recruiter"
            name_match = re.search(r'([A-Za-z\s]{3,30})(?:\||\n|$)', result_text)
            if name_match and len(name_match.group(1).strip()) < 25:
                name = name_match.group(1).strip()
            
            return [{'url': profile_url, 'name': name}]
    
    # Demo fallback
    print("  ⚠️ No profile found, using demo data")
    return [{'url': 'https://linkedin.com/in/demo-recruiter', 'name': 'Demo Recruiter'}]

async def search_recruiters(company_name, config):
    """Search for ONE recruiter at a company"""
    print(f"  🔎 Finding a recruiter at {company_name}...")
    
    agent = DroidAgent(
        goal=f"Find ONE recruiter at {company_name} on LinkedIn. Search, switch to People tab, find first person with recruiting title. Return URL and name.",
        config=config
    )
    
    result = await agent.run()
    
    if result.success:
        profiles = parse_single_profile(result.steps)
        print(f"  ✓ Found: {profiles[0]['name']}")
        return profiles
    else:
        print(f"  ❌ Failed: {result.reason}")
        return []