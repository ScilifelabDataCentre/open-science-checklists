# SciLifeLab Open Code Checklist

[![DOI](https://img.shields.io/badge/DOI-10.17044/scilifelab.29086775.v2-blue)](https://doi.org/10.17044/scilifelab.29086775.v2) ![Version](https://img.shields.io/badge/version-v2-lightgrey) ![Licence](https://img.shields.io/badge/licence-CC%20BY%204.0-green)

This checklist provides essential steps for sharing and citing research code. It covers planning your code, ensuring others can find, understand, reuse, and contribute to it, and enabling your work to be credited. Click each box to read about what should be done, why it matters, and how to implement it.

> [!TIP]
> For larger software projects, or if you want more comprehensive guidance in documenting your code, use the interactive Software Management Plan (SMP) available through the Data Stewardship Wizard. An SMP helps you plan your project and guides you through documenting how your software is developed, maintained, and sustained.

[→ SciLifeLab Data Stewardship Wizard](https://dsw.scilifelab.se/wizard)

[→ Learn more about sharing code and workflows](/topics/sharing-code-workflows/)

## Contents
- [Essential](#essential)
- [Recommended](#recommended)
- [Advanced](#advanced)
---
## Essential (5 items)

*Start here. These steps are the minimum needed to share your code properly.*

- [ ] **Add an open licence** `Findable`

  <details>
  <summary>Read more</summary>

  Add a licence to your code so others know how they can use, share, and modify it. Without a licence, your code cannot legally be reused, even if it is publicly available. Common options are the [MIT Licence](https://choosealicense.com/licenses/mit/) and [Apache Licence](https://choosealicense.com/licenses/apache-2.0/). If your repository also contains other content like text or figures, add a separate licence for those, such as [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

  #### Why it matters

  Without a licence, others cannot legally reuse your code, even if they can see it.

  #### What to do

  Add a `LICENSE` file to your repository. On GitHub, you can do this by selecting **"Add file → Choose a license template"**. SciLifeLab's standard is the MIT Licence. If your repository includes other materials like text or figures, add a separate licence for those, for example *CC BY 4.0* (copy the legal text from [CC BY 4.0 legal text](https://creativecommons.org/licenses/by/4.0/legalcode.txt) since GitHub does not offer 4.0). Name your code licence `LICENCE-CODE` and your content licence `LICENCE-CONTENT`, and list both clearly in your `README`.

  </details>

- [ ] **Add metadata** `Findable`

  <details>
  <summary>Read more</summary>

  Metadata is basic information about your code: who wrote it, what version it is, what licence it uses, and how to cite it. The simplest way to add this is a `CITATION.cff` file. For more detail you can also create a `codemeta.json` file using the [CodeMeta generator](https://codemeta.github.io/codemeta-generator/)

  #### Why it matters

  Without metadata, your code is harder to find, cite, and attribute correctly.

  #### What to do

  Add a `CITATION.cff` file to your repository with at least: title, authors, contributor roles and ORCID iDs (where available), version, licence, and keywords. Add the your persistent identifier (such as a DOI) once you have one.

  </details>

- [ ] **Get a persistent identifier** `Findable`

  <details>
  <summary>Read more</summary>

  Archive your code in a repository that gives it a persistent identifier (like a DOI), such as [Zenodo](https://zenodo.org/), [Software Heritage](https://www.softwareheritage.org/), or the [SciLifeLab Data Repository](https://figshare.scilifelab.se/). This is separate from your GitHub repository and gives people a stable link to cite in papers.

  #### Why it matters

  Links to GitHub repositories can break or change if the repo is renamed or moved. A persistent identifier is permanent and always points to the right version.

  #### What to do

  Upload your code to [Zenodo](https://zenodo.org/) to get a DOI. One way is to connect your GitHub repository to Zenodo and create a release. Follow the steps here: https://help.zenodo.org/docs/github/

  </details>

- [ ] **Put code in a public repository with version control** `Accessible`

  <details>
  <summary>Read more</summary>

  Upload your code to a platform like GitHub, GitLab, or Codeberg. These platforms track every change you make, let you create versioned releases, and make it easy for others to find and use your code.

  #### Why it matters

  If your code isn't in a public repository, others can't access it, and you can't easily track how it changed over time or which version was used to produce a specific result.

  #### What to do

  Upload your code to a public version-controlled repository on a platform like GitHub.

  </details>

- [ ] **Write a README** `Reusable`

  <details>
  <summary>Read more</summary>

  A `README.md` explains what the code does, how to install and run it, and how to cite it. Use plain Markdown section headings so the file is easy to read both by humans and automated tools.

  #### Why it matters

  Without a README, it is hard for anyone (including you, later) to understand what the code does or how to use it.

  #### What to do

  Add a `README.md` to your repository. At minimum include a title, a short description, and sections for 'Installation', 'Licence', and 'Citing this resource'. You can use [readme.so](https://readme.so/) to build one by filling in pre-made sections.

  </details>

## Recommended (8 items)

*These steps make your code easier to use, understand, and build on.*

- [ ] **Cite your code in publications** `Findable`

  <details>
  <summary>Read more</summary>

  When you publish a paper that uses your code, include a formal citation in the references section so readers can find it.

  #### Why it matters

  A citation in the references section means the readers know exactly where to go to find the software when reading the paper.

  #### What to do

  Add a citation to your references section using this template (inspired by AGU's Software Citation Examples): _< Author(s)/contributor(s) or project name(s) >. (< Date published >). < Descriptive title / name of software >. < Software release/version > < Bracketed description type (e.g., [Software], [Collection], [ComputationalNotebook]) >. < Repository name / Publication venue >. < DOI >._

  </details>

- [ ] **Format your code according to standards** `Interoperable`

  <details>
  <summary>Read more</summary>

  Use a standard style guide or formatter for your programming language to keep your code clean and consistent. Common tools for Python include Black and Pylint. See the [Netherlands eScience Center Guide](https://guide.esciencecenter.nl/#/) for language-specific examples and [The Turing Way's overview of static analysis tools](https://book.the-turing-way.org/reproducible-research/code-quality) for more options.

  #### Why it matters

  Inconsistent formatting makes code harder to read and makes small errors hard to detect.

  #### What to do

  Look up the standard style guide for your programming language and follow it, or install a formatter or linter that applies it automatically.

  </details>

- [ ] **List your dependencies** `Interoperable`

  <details>
  <summary>Read more</summary>

  List all the packages your code needs to run, and ideally which versions, in a file like `requirements.txt` or `environment.yml`. This lets others install everything they need in one step and reduces the risk of version conflicts.

  #### Why it matters

  If you don't list your dependencies, others may not be able to run your code at all, and outdated packages can cause bugs or security issues.

  #### What to do

  Create a `requirements.txt`, `environment.yml`, or similar, file listing all required packages. See the [list of package managers](https://en.wikipedia.org/wiki/List_of_software_package_management_systems) for options in your language. Where possible, also specify version ranges (e.g. `wordfreq>=3.0,<4.0`).

  </details>

- [ ] **Use open file formats** `Interoperable`

  <details>
  <summary>Read more</summary>

  Store your data and outputs in open, widely used formats so others can open them without proprietary or specialist software. See [DANS's File Formats Overview](https://dans.knaw.nl/en/file-formats/) for recommended formats for long term access.

  #### Why it matters

  Proprietary formats (like .xlsx or .mat) may not be readable by everyone, and can become inaccessible if the software is no longer available.

  #### What to do

  Check [DANS's File Formats Overview](https://dans.knaw.nl/en/file-formats/) and convert your files to recommended open formats where possible (e.g. `.csv` instead of `.xlsx`, `.txt` instead of `.docx`).

  </details>

- [ ] **Add usage examples** `Reusable`

  <details>
  <summary>Read more</summary>

  Include a small example that shows how to run your code on real or example data. This can be a short script, a section in the `README.md`, or a [Jupyter notebook](https://jupyter.org/) (see [notebook guidance](https://zenodo.org/records/5651648)). Include a small example dataset if possible, or link to one on [Zenodo](https://zenodo.org/) if the data is too large to include in the repository.

  #### Why it matters

  Without an example, others may not know how to run your code or what format the input data should be in.

  #### What to do

  Add a short script or Jupyter notebook that runs the code on a small example dataset and shows the expected output. Put the example dataset in the repository, or link to it if it is too large.

  </details>

- [ ] **Document your code** `Reusable`

  <details>
  <summary>Read more</summary>

  Add inline comments inside your code and write docstrings for your functions so others can understand what each part does. For more guidance, see [CodeRefinery's Modular Code Development lesson](https://cicero.xyz/v3/remark/0.14.0/github.com/coderefinery/modular-code-development/master/talk.md/#1).

  #### Why it matters

  Without comments and docstrings, others (and future you) will struggle to understand or build on the code.

  #### What to do

  Write a short comment above each logical block of code explaining what it does. Write a docstring for every function describing its inputs, outputs, and purpose. For larger projects, consider a dedicated documentation site using GitHub Pages or ReadTheDocs.

  </details>

- [ ] **Use a clear folder structure** `Best practice`

  <details>
  <summary>Read more</summary>

  Organise your files into clearly named folders so others can find their way around your project. A common approach is to separate source code and data into folders like `src/` and `data/`.

  #### Why it matters

  A messy or flat file structure makes it hard to navigate and understand what a project contains.

  #### What to do

  Organise your repository into named folders by type, for example `src/` for code, `data/` for input data, and `results/` for outputs. Add a short note about the structure to your `README.md`.

  </details>

- [ ] **Use clear and consistent names** `Best practice`

  <details>
  <summary>Read more</summary>

  Give your variables, functions, and files names that clearly describe what they do. Follow a consistent naming style throughout your code. See [The Turing Way Guidelines for Code Styling](https://book.the-turing-way.org/project-design/info-management/code-styling/code-styling-guidelines) for examples.

  #### Why it matters

  Unclear or inconsistent names make code hard to read and maintain, for you and for anyone else working with it.

  #### What to do

  Use short but descriptive names that reflect what a variable or function does. Pick a naming style (e.g. `snake_case` in Python or `camelCase` in JavaScript) and stick to it throughout.

  </details>

## Advanced (11 items)

*Most useful for larger projects, or code that others will actively contribute to or maintain.*

- [ ] **Add a software availability statement** `Findable`

  <details>
  <summary>Read more</summary>

  A software availability statement is a short paragraph in the body of your paper that tells readers where to find your code and under what conditions.

  #### Why it matters

  Many journals require this, and it helps readers find your code without having to search for it.

  #### What to do

  Add a short statement to your paper using this template (inspired by AGU's Software Citation Examples): _< Version number > of the < software name > used for < brief context, description of what the software was used for > is preserved at < DOI, persistent identifier link >, available via < licence type, access conditions > and developed openly at < software development platform link >. [< Link to formal citation in References section >]_

  </details>

- [ ] **Describe your inputs and outputs** `Interoperable`

  <details>
  <summary>Read more</summary>

  Make it clear what data your code expects as input and what it returns as output: what format, what type, what it contains. You can do this in docstrings, in your documentation, or formally using something like [JSON Schema](https://json-schema.org/).

  #### Why it matters

  If it is not clear what the code expects and returns, others cannot easily use or adapt it.

  #### What to do

  For each function, document the expected inputs and outputs in the docstring (type, purpose, format). For the overall tool, describe the data structure in your documentation. For formal use, consider defining it with JSON Schema.

  </details>

- [ ] **Add badges to your README** `Reusable`

  <details>
  <summary>Read more</summary>

  Badges are small indicators you can add to your `README.md` to show things like your licence, DOI, and whether your tests are passing. You can create custom badges via [shields.io](https://shields.io/).

  #### Why it matters

  Badges give users a quick overview of key information.

  #### What to do

  Add badges for your licence and persistent identifier (and more) to your `README.md`. Get them from platforms (GitHub, Zenodo) or create custom ones via [shields.io](https://shields.io/).

  </details>

- [ ] **Add a code of conduct** `Best practice`

  <details>
  <summary>Read more</summary>

  A code of conduct communicates how people should interact in your project and what to do if something goes wrong.

  #### Why it matters

  Without a code of conduct, contributors may not know how to report issues or what behaviour is expected.

  #### What to do

  Add a `CODE_OF_CONDUCT.md` file using a template like the [Contributor Covenant](https://www.contributor-covenant.org/). Include a contact email or form for reporting violations or concerns.

  </details>

- [ ] **Add contributing guidelines** `Best practice`

  <details>
  <summary>Read more</summary>

  A `CONTRIBUTING.md` file tells people how they can contribute to your code; how to report issues, suggest changes, and submit pull requests.

  #### Why it matters

  Without contributing guidelines, people who want to help may not know how to do so.

  #### What to do

  Add a `CONTRIBUTING.md` file explaining how to open issues, suggest changes, and submit pull requests. You can also include information on coding style, the review process, and how contributors will be credited.

  </details>

- [ ] **Add tests** `Best practice`

  <details>
  <summary>Read more</summary>

  Write tests that check your code still works correctly when you make changes. Use a testing framework like [PyTest](https://docs.pytest.org/en/stable/), [Jest](https://jestjs.io/), or [Mocha](https://mochajs.org/). You can also set up automated testing with GitHub Actions so tests run every time you push new code.

  #### Why it matters

  Without tests, it is easy to accidentally break something when making changes and not notice until much later.

  #### What to do

  Write simple unit tests for your key functions using a framework like PyTest. Optionally, set up GitHub Actions to run the tests automatically whenever you update the code.

  </details>

- [ ] **Containerise your code** `Best practice`

  <details>
  <summary>Read more</summary>

  A container (e.g. using [Docker](https://www.docker.com/) or [Singularity](https://github.com/apptainer/singularity)) packages your code together with everything it needs to run, so it works the same way on any computer.

  #### Why it matters

  Code that works on your machine can behave differently on other systems.

  #### What to do

  Add a Dockerfile or equivalent to your repository.

  </details>

- [ ] **State whether and by whom the code will be maintained** `Best practice`

  <details>
  <summary>Read more</summary>

  Be clear about whether your code will be actively maintained after publication, and if so, who is responsible. This helps users know what to expect if they find a bug or want to build on your work.

  #### Why it matters

  Without this information, users don't know whether to expect updates, bug fixes, or support. Unmaintained code can also develop security issues over time that put anyone using it at risk.

  #### What to do

  Add a short note to your `README.md` saying whether the code will be maintained and who to contact. If it will not be maintained, say that too - it is very useful information.

  </details>

- [ ] **Use issue tracking** `Best practice`

  <details>
  <summary>Read more</summary>

  Use GitHub Issues (or a similar tool) to log bugs, feature requests, and tasks. This makes it easy for others to report problems and for you to keep track of what needs doing. Adding a few "good first issue" labels can help new contributors get started.

  #### Why it matters

  Without issue tracking, problems can get lost and it is hard for others to know how to contribute or report bugs.

  #### What to do

  Enable GitHub Issues in your repository and add your first issue. Use labels like "bug", "enhancement", or "good first issue" to organise.

  </details>

- [ ] **Use version tags** `Best practice`

  <details>
  <summary>Read more</summary>

  Tag your releases with a version number so people can refer to and cite a specific version of your code. A common system is [Semantic Versioning](https://semver.org/): `major.minor.patch` (e.g. `v1.2.0`).

  #### Why it matters

  Without version tags, users cannot tell which version they are using or cite a specific version in a paper.

  #### What to do

  Tag each release in your repository using a consistent version number. You can do this via the GitHub interface or the command line. For smaller projects, uploading to Zenodo for each new version is enough.

  </details>

- [ ] **Write modular code** `Best practice`

  <details>
  <summary>Read more</summary>

  Break your code into small, reusable functions instead of writing everything in one long script. Avoid hardcoding file paths or settings directly in the code - pass them as arguments instead. See [The Turing Way's Recommendations for Code Reuse](https://book.the-turing-way.org/reproducible-research/code-reuse/code-reuse-details#re-runnable-recommendations) for more information.

  #### Why it matters

  Long scripts that do everything in one place are hard to read, test, and update. Changing one part can easily break something else.

  #### What to do

  Split your code into functions, each doing one clear thing. Pass inputs like file paths or settings as arguments rather than hardcoding them.

  </details>

---

## Sources

The Turing Way Community. (2022). *The Turing Way: A handbook for reproducible, ethical and collaborative research*. Zenodo. https://doi.org/10.5281/zenodo.3233853 (Retrieved April 11, 2025.)

Software Sustainability Institute. *Guides for researchers*. Software Sustainability Institute. https://www.software.ac.uk/guide/guides-researchers (Retrieved April 11, 2025.)

Spaaks, J. H. and Maassen, J.. (2018). *Netherlands eScience Center Software Sustainability Protocol*. Zenodo. https://doi.org/10.5281/zenodo.1451750 (Retrieved April 11, 2025.)

Social Science Data Editors. *Data and Code Availability Statements - Sample text*. Social Science Data Editors Guidance. https://social-science-data-editors.github.io/guidance/Guidance/Requested_information_dcas.html (Retrieved April 11, 2025.)

FORCE11. (2016). *Software Citation Principles*. FORCE11. https://force11.org/info/software-citation-principles-published-2016/ (Retrieved April 11, 2025.)

American Geophysical Union. *Data and Software for Authors*. AGU. https://www.agu.org/publications/authors/journals/data-software-for-authors (Retrieved April 11, 2025.)

