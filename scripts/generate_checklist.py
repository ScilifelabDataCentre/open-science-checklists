"""
generate_checklist.py

Converts a checklist JSON file into a Markdown file with collapsible

Run as follows:

python3 scripts/generate_checklist.py <<path/to/checklist/folder>>

"""
import json
from pathlib import Path
import argparse

# Priority levels, in the order items should appear. Anything not listed here is sorted alphabetically after these.
priority_order = ["Essential", "Recommended", "Advanced"]
# FAIR categories, in the order items should appear within a priority
fair_order = ["Findable", "Accessible", "Interoperable", "Reusable", "Best practice"]

def sort_key(item: dict) -> tuple:
    """Build the sort key for one item: (priority_rank, category_rank).
    """
    priority = item.get("priority", "")
    category = item.get("fair_category", "")

    priority_rank = (
        priority_order.index(priority) if priority in priority_order else len(priority_order)
    )
    category_rank = (
        fair_order.index(category) if category in fair_order else len(fair_order)
    )
    return (priority_rank, category_rank)


def generate_item(item: dict) -> str:
    """Render single checklist item as markdown block.
    """
    title = item["title"].strip()
    description = item["description"].strip()
    explanation = item["explanation"].strip()
    action = item["action"].strip()
    fair_category = item["fair_category"].strip()

    return (
        f"- [ ] **{title}** *{fair_category}*\n"
        f"  <details>\n"
        f"  <summary>Read more</summary>\n\n"
        f"  {description}\n\n"
        f"  **Why:** {explanation}\n\n"
        f"  **Action:** {action}\n\n"
        f"  </details>\n"
    )

def generate_itemlist(items: list) -> str:
    """Sort items by priority and FAIR category, and render them.
    """
    sorted_items = sorted(items, key=sort_key)
 
    parts = []
    previous_priority = None
 
    for item in sorted_items:
        priority = item.get("priority", "")
        if priority != previous_priority:
            parts.append(f"---\n## {priority}\n")
            previous_priority = priority
        parts.append(generate_item(item))
        
    return "\n".join(parts)

def generate_markdown(json_path: Path, output_path: Path) -> None:
    """Top level markdown generation function.
    """
    data = json.loads(Path(json_path).read_text(encoding="utf-8"))

    # Title and intro
    md = f"# {data['title']}\n\n"
    md += f"DOI: {data['doi']} | Version: {data['version']}\n\n"
    md += f"{data['description']}\n\n"
    md += f">[!TIP]\n>{data['disclaimer']}\n\n"

    # intro links
    # {"label": "SciLifeLab Data Stewardship Wizard", "url": "https://dsw.scilifelab.se/wizard"},

    links = data['links']
    for link in links:
        md += f"[→ {link['label']}]({link['url']})\n\n"

    # table of contents
    
    md += f"## Contents\n"
    for priority in priority_order:
        md += f"- [{priority}](#{priority.lower()})\n"


    # Items
    # Sorting and rendering is done in generate_itemlist - make changes
    # there if the sort order or item format should be updated.
    md += generate_itemlist(data["items"])

    Path(output_path).write_text(md, encoding="utf-8")
    print(f"Wrote {len(data['items'])} items to {output_path}")



if __name__ == "__main__":
    #get input and putput path from user
    parser = argparse.ArgumentParser()
    parser.add_argument("folder_path", help="Path to the checklist folder (must contain checklist_items.json)")
    parser.add_argument("--output", help="(Optional) Name for the output .md file (without folder path)")
    args = parser.parse_args()

    # check if folder exists
    folder = Path(args.folder_path)
    if not folder.exists() or not folder.is_dir():
        raise FileNotFoundError(f"Folder not found: {folder}")
    
    input_path = folder / "checklist_items.json"
    if not input_path.exists():
        raise FileNotFoundError(f"No checklist_items.json found in {folder}")

    # .md file named after folder name unless other name is specified
    output_name = args.output or f"{folder.name}.md"
    output_path = folder / output_name

    generate_markdown(input_path, output_path)