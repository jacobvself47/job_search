import os
import requests
import time
import csv

api_key = os.getenv("GOOGLE_API_KEY")
cse_id = os.getenv("GOOGLE_SE_ID")


# Replace with your values


def google_job_search(total_results=50, output_file="results.csv"):
    query = (
        'security OR cybersecurity OR GRC OR "governance risk compliance" OR "security risk"'
        'SOC2 OR "SOC 2" OR CISSP '
    )

    url = "https://customsearch.googleapis.com/customsearch/v1"
    results_shown = 0
    results_per_page = 10
    dateRestrict = "d1"

    results = []

    while results_shown < total_results:
        start_index = results_shown + 1
        params = {
            "q": query,
            "key": api_key,
            "cx": cse_id,
            "num": results_per_page,
            "start": start_index,
            "dateRestrict": dateRestrict
        }

        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"❌ Error: {response.status_code} - {response.text}")
            break

        data = response.json()
        items = data.get("items", [])
        if not items:
            print("No more results.")
            break

        for i, item in enumerate(items):
            index = results_shown + i + 1
            title = item.get("title", "")
            link = item.get("link", "")
            results.append([index, title, link])

        results_shown += len(items)

        # Optional delay to avoid quota issues
        time.sleep(1)

    # Write to CSV
    with open(output_file, mode="w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Index", "Title", "URL",])
        writer.writerows(results)


# Run it
google_job_search()
