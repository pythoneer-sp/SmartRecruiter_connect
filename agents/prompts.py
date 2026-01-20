# agents/prompts.py

# Agent 1: Search (stays similar)
SEARCH_RECRUITERS_PROMPT = """
Search LinkedIn for ONE recruiter at {company_name}. 
1. Open LinkedIn search
2. Type "{company_name}" 
3. Switch to "People" tab
4. Find the FIRST person with a recruiting title (HR/Recruiter/Talent)
5. TAP their name to open profile
6. Stop when profile loads

Return only the person's name you found.
"""

# Agent 2: Send connection request (NEW)
SEND_CONNECTION_PROMPT = """
On this LinkedIn profile:
1. Click the "Connect" button (usually near top)
2. If prompted, click "Add a note" or "Personalize invitation"
3. Paste this note: {message}
4. Click "Send invitation"
5. Return success/failure

Note: {message}
"""