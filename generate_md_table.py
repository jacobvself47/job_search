import csv

with open('results.csv') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

md = []
header = rows[0]
md.append("| " + " | ".join(header) + " |")
md.append("|" + "|".join(["-" * len(h) for h in header]) + "|")
for row in rows[1:]:
    md.append("| " + " | ".join(row) + " |")

# Write to file
with open("email_body.md", "w") as out:
    out.write("\n".join(md))