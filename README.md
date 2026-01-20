# SmartRecruiter Connect

**Automate LinkedIn connection requests to recruiters using AI agents**

An intelligent automation tool that finds and connects with recruiters at target companies, solving the manual outreach problem faced by CS students and job seekers.

---

## 🎯 Problem Solved

As a CS student, I spent **2-3 hours every week** manually:
- Searching for recruiters at target companies
- Reading their profiles to verify they're actually recruiters
- Writing personalized connection notes
- Sending requests one-by-one

**SmartRecruiter Connect reduces this to 45 seconds.**

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **🤖 Agentic Search** | AI agent searches LinkedIn and identifies recruiters by title keywords |
| **🎯 Intelligent Filtering** | Automatically verifies if a profile is a recruiter (HR/Recruiter/Talent) |
| **✍️ Personalization** | Generates custom connection notes with name, company, and candidate info |
| **📱 Mobile Automation** | Uses DroidRun to control Android device - no API keys needed |
| **📊 Progress Tracking** | Logs all actions and generates summary reports |

---

## 🏗️ Architecture
SmartRecruiter Connect/
├── agents/
│   ├── prompts.py          # Agent instructions & goals
│   ├── search.py           # Agent 1: Finds recruiters
│   ├── filter.py           # Agent 2: Verifies profiles
│   └── connect.py          # Agent 3: Sends connection requests
├── data/
│   ├── companies.json      # Target companies
│   ├── recruiter_keywords.json  # Titles to match
│   └── message_template.txt     # Connection note template
├── candidate_profile.json  # Your information
├── main.py                 # Orchestration engine
├── test_search_simple.py   # Test search agent
├── test_connection.py      # Test connection agent
└── README.md              # This file


**Agent Workflow:**
1. **Search Agent** → Finds 1 recruiter at target company
2. **Filter Agent** → Opens profile and confirms recruiter title
3. **Connect Agent** → Sends personalized connection request

---

## 🛠️ Setup

### Prerequisites
- Python 3.8+
- Android device with LinkedIn app installed & logged in
- DroidRun configured (see [DroidRun Docs](https://docs.droidrun.ai))

### Installation

```bash
# Clone or create project structure
mkdir smartrecruiter-connect
cd smartrecruiter-connect

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install droidrun python-dotenv

# Ensure DroidRun is configured
# Follow: https://docs.droidrun.ai/quickstart

Configuration
Edit your profile (candidate_profile.json):
{
  "name": "Your Full Name",
  "university": "Your University",
  "year": "3rd",
  "skills": ["Python", "DSA", "DroidRun", "Your Skills"],
  "interest_area": "Your interest area"
}
Add target companies (data/companies.json):
[
  "Google",
  "OpenAI",
  "Microsoft"
]
Customize message (data/message_template.txt):
Hi {name},

I'm {student_name}, a {year} year CS student at {university} passionate about {interest_area}. I'm excited about opportunities at {company} and would love to connect.

Best,
{student_name}
