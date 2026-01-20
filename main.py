# main.py - UPDATED
import asyncio
import json
from droidrun import DroidrunConfig
from agents.search import search_recruiters
from agents.filter import filter_profile
from agents.connect import send_connection_request  # Changed import
from dotenv import load_dotenv

load_dotenv()

class SmartRecruiterConnect:
    def __init__(self):
        # Load all data (same as before)
        with open('data/companies.json', 'r') as f:
            self.companies = json.load(f)
        
        with open('data/recruiter_keywords.json', 'r') as f:
            self.keywords = json.load(f)
        
        with open('data/message_template.txt', 'r') as f:
            self.message_template = f.read()
        
        with open('candidate_profile.json', 'r') as f:
            self.candidate = json.load(f)
        
        self.config = DroidrunConfig()
        self.results = []

    def personalize_message(self, name, company):
        """Create connection request note"""
        return self.message_template.format(
            name=name,
            student_name=self.candidate['name'],
            year=self.candidate['year'],
            university=self.candidate['university'],
            skills=", ".join(self.candidate['skills']),
            interest_area=self.candidate['interest_area'],
            company=company
        )

    async def process_company(self, company):
        """Process ONE company and send ONE connection request"""
        print(f"\n🔍 Processing {company}...")
        
        # Step 1: Find ONE recruiter
        profiles = await search_recruiters(company, self.config)
        
        if not profiles:
            print(f"  ❌ No recruiter found")
            return False
        
        # Step 2: Analyze profile
        profile = profiles[0]
        result = await filter_profile(profile['url'], self.keywords, self.config)
        
        if not result['is_recruiter']:
            print(f"  ✗ Not a recruiter: {result['title']}")
            return False
        
        print(f"  ✓ Confirmed: {result['title']}")
        
        # Step 3: Send connection request (CHANGED)
        message = self.personalize_message(result['name'], company)
        success = await send_connection_request(result['name'], message, self.config)
        
        if success:
            print(f"  ✓ Request sent to {result['name']}!")
            self.results.append({
                'company': company,
                'recruiter': result['name'],
                'status': 'success'
            })
            return True
        else:
            print(f"  ❌ Failed to send request")
            return False

    async def run(self):
        print("🚀 Starting SmartRecruiter Connect - Connection Mode")
        print("Targeting 1 company for demo\n")
        
        # Only first company
        for company in self.companies[:1]:
            await self.process_company(company)
        
        # Print summary
        print("\n📊 DEMO SUMMARY")
        print("-" * 30)
        for r in self.results:
            print(f"✓ {r['company']}: Connected with {r['recruiter']}")
        
        print(f"\n🎉 Demo complete! Sent {len(self.results)} connection request(s).")

if __name__ == "__main__":
    app = SmartRecruiterConnect()
    asyncio.run(app.run())