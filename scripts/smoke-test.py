import urllib.request

base = "http://localhost:8001"
files = [
    "content/science/chemistry/topics.json",
    "content/science/chemistry/composition-of-matter.md",
    "content/science/chemistry/structure-and-bonding.md",
    "content/science/chemistry/states-and-reactions.md",
    "content/science/chemistry/common-reactions.md",
    "content/science/chemistry/chemistry-in-life.md",
    "questions/science/chemistry/composition-of-matter.json",
    "questions/science/chemistry/structure-and-bonding.json",
    "questions/science/chemistry/states-and-reactions.json",
    "questions/science/chemistry/common-reactions.json",
    "questions/science/chemistry/chemistry-in-life.json",
]
passed = 0
for f in files:
    try:
        r = urllib.request.urlopen(f"{base}/{f}")
        print(f"PASS: {f.split('/')[-1]} ({r.status})")
        passed += 1
    except Exception as e:
        print(f"FAIL: {f.split('/')[-1]} - {e}")
print(f"\n{passed}/{len(files)} passed")
