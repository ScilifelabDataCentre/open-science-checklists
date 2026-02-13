
<img src="assets/SciLifeLab_symbol_green.png" alt="SciLifeLab Symbol" width="60" align="right">

# SciLifeLab Open Science Checklists
These checklists are developed by the Open Science Team at SciLifeLab Sweden, in collaboration with partner universities and subject matter experts (internal and external)*, to support compliance with the FAIR principles when publishing articles and software.

Please note that these checklists are in development and are <ins>intended to be guiding resources which do not require every item to be completed.</ins>

<sub>*Checklists have been reviewed and contributed to by the SciLifeLab _Seshat_, _Berserkers_, _RDM_, and _Freya_ teams, as well as Stockholm University and the Netherlands eScience Center.</sub>

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## How to Cite this Resource

These Checklists are licenced under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). 

**Official versions are archived on Figshare.** These may not reflect the most current updates due to the evolving nature of this resource. Please cite the specific checklist you used:

* **SciLifeLab Open Access Checklist**  
DOI: https://doi.org/10.17044/scilifelab.29086706

* **SciLifeLab Open Science Software Checklist**  
DOI: https://doi.org/10.17044/scilifelab.29086775

IFF referencing the development version on GitHub, you may also cite this repository using the included `CITATION.cff` file.

## Generating Markdown and PDF Checklists

To generate the MArkdown version of a checklist from a `.json` file, we use the Python scripts in the `scripts/` folder.

From the root of the repo run:

```bash
python scripts/generate_md.py <checklist folder>
```
This will generate a Markdown file named `<checklist folder>.md` inside the same folder. To specify a custom output filename instead, use:

```bash
python scripts/generate_md.py <checklist folder> --output <filename>.md
```

### JSON Format

Checklists are defined in `.json` files using the following structure, which is expected for generation to work:

```json
{
  "title": string,                // Title of the checklist
  "description": string,          // Checklist description/introduction
  "doi": string,                  // DOI of the published version of the checklist
  "items": [
    {
      "title": string,            // Bolded "prompt" part of checkloist item
      "description": string,      // Explanation or guidance for the item
      "category": string,         // Section in which it will be displayed (e.g. "Findable", "Accessible" etc)
      "rating": integer,          // Priority level (1 = highest, 3 = lowest)
      "note": string              // Optional note, rendered as a blockquote under the item
    }
  ],
  "sources": [
  {
    "authors": string,         // Author(s) or organisation
    "year": integer,           // Year of publication
    "title": string,           // Title of the source
    "publisher": string,       // Publisher or platform
    "doi": string,             // DOI of the source
    "retrieved": string        // Date retrieved (YYYY-MM-DD)
  }
]
}
```