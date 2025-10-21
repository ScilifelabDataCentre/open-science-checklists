import argparse
import json
from pathlib import Path
from collections import defaultdict

# TODO: add descriptions of functions, script, readme

CATEGORY_ORDER = ["Planning", "Findable", "Accessible", "Interoperable", "Reusable"]

# EDITABLE TEXT BELOW- Update this section if checklist metadata changes, the doi is extracted from the json automatically
# TODO: add how to cite? or is this enough?
CONTACT_TEMPLATE = """\
## CONTACT AND CONTRIBUTIONS

This checklist is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). DOI: {doi}

For questions about the SciLifeLab open science checklists, please contact [datacentre@scilifelab.se](mailto:datacentre@scilifelab.se?subject=Open%20Science) with 'Open Science' in the subject line.

To contribute or suggest improvements, see our [Contributing Guide](https://github.com/ScilifelabDataCentre/open-science-checklists/blob/main/CONTRIBUTING.md).
"""

def generate_markdown(json_path, output_path):
    """
    top level md generation function. calls item generation and source generation

    """
    # TODO: add check that the json follows the correct stucture!

    data = json.loads(Path(json_path).read_text())

    # TITLE AND INTRO
    md = f"# {data['title']}\n\n"
    md += f"{data['description']}\n\n"
    md += f"---\n\n"

    # ITEMS
    # Item sorting and grouping is done in separate function generate_itemlist - make changes there if the items format should be updated
    md += generate_itemlist(data["items"])

    # CONTACT AND CONTRIBUTIONS
    # Editable section defined at top of script 
    md += CONTACT_TEMPLATE.format(doi=data["doi"])

    # SOURCES
    # APA source generation is done in separate function generate_sources - make changes there if the source format should be updated
    md += generate_sources(data["sources"])

    Path(output_path).write_text(md)

def generate_itemlist(items):
    """
    generate the checklist items, sorted and grouped in order of CATEGORY_ORDER
    """
    md_list = ""

    # Grouping items by category
    grouped = defaultdict(list)
    for item in items:
        category = item.get("category")
        if not category:
            raise ValueError(f'Missing category for item: "{item["title"]}"')
        grouped[category].append(item)

    # Sort categories by FAIR order (but planning goes first), others go last
    sorted_categories = CATEGORY_ORDER + sorted(
        [c for c in grouped if c not in CATEGORY_ORDER]
    )

    for category in sorted_categories:
        if category not in grouped: # If no item in one of the defined categories, continue
            continue
        md_list += f"## {category.upper()}\n\n"
        for item in grouped[category]:
            md_list += f"- [ ] **{item['title']}:** {item['description']}\n"
        md_list += "\n"
    
    # TODO: implement the note thing

    return md_list

def generate_sources(sources):
    """
    APA style sources
    """
    lines = ["## SOURCES\n"]
    for src in sources:
        authors = src["authors"]
        year = src["year"]
        title = src["title"]
        publisher = src["publisher"]
        doi = src.get("doi")
        retrieved = src.get("retrieved")

        line = f"{authors} ({year}). *{title}*. {publisher}."
        if doi:
            line += f" https://doi.org/{doi.lstrip('https://doi.org/')}"
        if retrieved:
            line += f" (Retrieved {retrieved})"
        lines.append(line + "\n")

    return "\n".join(lines)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("folder_path", help="Path to the checklist folder (must contain checklist_items.json)")
    parser.add_argument("--output", help="Optional name for the output .md file (without folder path)")

    args = parser.parse_args()
    folder = Path(args.folder_path)
    if not folder.exists() or not folder.is_dir():
        raise FileNotFoundError(f"Folder not found: {folder}")
    
    json_path = folder / "checklist_items.json"
    if not json_path.exists():
        raise FileNotFoundError(f"No checklist_items.json found in {folder}")

    # .md file named after folder name unless other name is specified
    output_name = args.output or f"{folder.name}.md"
    output_path = folder / output_name

    generate_markdown(json_path, output_path)

