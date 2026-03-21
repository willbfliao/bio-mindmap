import json, os, glob

# Validate JSON files
print("=== JSON Validity ===")
for pattern in ["questions/science/chemistry/*.json", "content/science/chemistry/topics.json"]:
    for f in glob.glob(pattern):
        try:
            json.load(open(f))
            print(f"OK: {f}")
        except Exception as e:
            print(f"ERROR: {f} - {e}")

# Validate Markdown root nodes
print("\n=== Markdown Root Nodes ===")
for f in glob.glob("content/science/chemistry/*.md"):
    with open(f) as fh:
        for line in fh:
            if line.startswith("# "):
                print(f"{os.path.basename(f)} -> {line.strip()}")
                break

# Topic ID consistency
print("\n=== Topic ID Consistency ===")
topics = json.load(open("content/science/chemistry/topics.json"))
errors = 0
for cat in topics["categories"]:
    for t in cat["topics"]:
        tid = t["id"]
        md_ok = os.path.exists(f"content/science/chemistry/{tid}.md")
        qj_ok = os.path.exists(f"questions/science/chemistry/{tid}.json")
        qdata = json.load(open(f"questions/science/chemistry/{tid}.json")) if qj_ok else {}
        qcount = len(qdata.get("questions", []))
        qid_match = qdata.get("topicId", "") == tid
        answers_valid = all(q.get("answer") in "ABCD" for q in qdata.get("questions", []))
        explanations = all(q.get("explanation") for q in qdata.get("questions", []))
        ok = md_ok and qj_ok and qcount == t["questionCount"] and qid_match and answers_valid and explanations
        status = "OK" if ok else "ERROR"
        if not ok:
            errors += 1
        print(f"{status}: {tid} | md={md_ok} | json={qj_ok} | questions={qcount}/{t['questionCount']} | topicId={qid_match} | answers={answers_valid} | explanations={explanations}")

# Count ## branches per md
print("\n=== Mind Map ## Branch Count ===")
for f in glob.glob("content/science/chemistry/*.md"):
    with open(f) as fh:
        h2_count = sum(1 for line in fh if line.startswith("## "))
    name = os.path.basename(f)
    ok = "OK" if 3 <= h2_count <= 7 else "WARN"
    print(f"{ok}: {name} has {h2_count} ## branches")

print(f"\n=== Summary: {errors} errors ===")
