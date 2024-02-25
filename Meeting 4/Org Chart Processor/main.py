import json


def iterate_org_chart(org_chart):
    print(org_chart["name"])
    if "subordinates" in org_chart:
        for subordinate in org_chart["subordinates"]:
            iterate_org_chart(subordinate)


# Load JSON data from file
with open("companies.json", "r") as file:
    data = json.load(file)


# Iterate over each organization chart
for index, org_chart in enumerate(data, start=1):
    print(f"\nOrg Chart {index}:")
    iterate_org_chart(org_chart)
