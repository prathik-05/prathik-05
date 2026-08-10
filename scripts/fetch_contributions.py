import json
import os
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

USERNAME = "prathik-05"
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
JSON_PATH = DATA_DIR / "contributions.json"

class ContributionHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.days = []
        
    def handle_starttag(self, tag, attrs):
        if tag == "td":
            attr_dict = dict(attrs)
            if "class" in attr_dict and "ContributionCalendar-day" in attr_dict["class"]:
                date = attr_dict.get("data-date")
                level = attr_dict.get("data-level", "0")
                if date:
                    self.days.append({
                        "date": date,
                        "level": int(level)
                    })

def fetch_contributions():
    url = f"https://github.com/users/{USERNAME}/contributions"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            html_content = response.read().decode("utf-8")
            parser = ContributionHTMLParser()
            parser.feed(html_content)
            days_data = parser.days
    except Exception as e:
        print(f"Fetch note: {e}, generating fallback calendar grid")
        # Generate 371 default calendar days if offline
        days_data = [{"date": "", "level": 0} for _ in range(371)]

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump({"username": USERNAME, "days": days_data}, f, indent=2)
        
    print(f"Contributions saved to {JSON_PATH} ({len(days_data)} days)")

if __name__ == "__main__":
    fetch_contributions()
