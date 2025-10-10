# Open Software Checklist

## This checklist provides essential steps for sharing and citing your research software. It covers everything from planning your software to ensuring others can find, understand, reuse, and contribute to your software, and how to ensure your work is credited.

## PLAN YOUR SOFTWARE

- [ ] **Develop a Software Management Plan (SMP):** Outline contributors, project name, versioning, coding standards, dependencies, testing, and sustainability. Use the Software Sustainability Institute’s [SMP guide and template](https://www.software.ac.uk/news/software-management-plans), Netherlands eScience Centers [Practical Guide to SMPs](https://zenodo.org/records/7589725) or the [Software Management Wizard (SMW)](https://smw.dsw.elixir-europe.org/wizard/) to create one.

---

## MAKE YOUR SOFTWARE FINDABLE AND ACCESSIBLE

- [ ] **Host Code in a Public Version-Controlled Repository:** Host your code on platforms like [GitHub](https://github.com/), [GitLab](https://about.gitlab.com/), or [CodeBerg](https://codeberg.org/) to track development history, enable tagged versioned releases, improve reusability, and support collaboration.

- [ ] **Archive and Assign a Persistent Identifier:**  Ensure long-term preservation by depositing a snapshot of a specific software release (e.g., v1.0.0) in repositories that assign a PID such as [Zenodo](https://zenodo.org/), [Software Heritage](https://www.softwareheritage.org/), or your local institutional repository (e.g., [SciLifeLab Data Repository](https://figshare.scilifelab.se/)). This complements hosting code in a public repository by providing a fixed reference that can be cited in publications and matched to data and results.

- [ ] **Provide Descriptive Metadata:** Include essential details such as title, authors, version, licence, and DOI. You can generate a codemeta.json file using tools like the [CodeMeta generator](https://codemeta.github.io/codemeta-generator/), which can then be added to public and preservation repositories (e.g. GitHub, Zenodo). One such file can be seen [here](https://github.com/cboettig/codemeta/blob/master/codemeta.json).

- [ ] **Cite Your Software in Publications:** Include a formal citation in the References section of the publication. For example using the following template inspired by [AGUs Software Citation Examples](https://www.agu.org/publications/authors/journals/data-software-for-authors):  
       _< Author(s)/contributor(s) or project name(s) >. (< Date published >). < Descriptive title / name of software >. < Software release/version > < Bracketed description type (e.g., [Software], [Collection], [ComputationalNotebook]) >. < Repository name / Publication venue >. < DOI >._
      Note: The bracketed description allows the publishers/indexers to appropriately tag the citation so that it is indexed and counted. 

- [ ] **Declare Software Availability in Publications:** Include a software availability statement in the body of the publication, describing where and how the software can be accessed. For example using the following adapted [AGUs Template](https://www.agu.org/publications/authors/journals/data-software-for-authors):  
       _< Version number > of the < software name > used for < brief context, description of what the software was used for > is preserved at < DOI, persistent identifier link >, available via < licence type, access conditions > and developed openly at < software development platform link >. [< Link to formal citation in References section >]_

  > **_Unsure about this process? You can walk through the depositing, describing, and citing your software using Zenodo’s Sandbox (testing environment). You can follow the steps outlined on the [Documentation](https://help.zenodo.org/docs/deposit/create-new-upload/) page, which guides you through producing metadata for your project._**


---

## MAKE YOUR SOFTWARE INTEROPERABLE

- [ ] **Use Standard Open File Formats:** Use open formats and standards to enable compatibility with other tools. See [DANS’s File Formats Overview](https://dans.knaw.nl/en/file-formats/) for recommended formats for long-term access.

- [ ] **Follow Code Formatting Standards:** Use recognised open standards, style guides, linters, and formatters to keep code clean and consistent. Common examples include Black and Pylint (Python). See the [Netherlands eScience Center Guide](https://guide.esciencecenter.nl/#/) for language-specific examples and [The Turing Way’s overview of static analysis tools](https://book.the-turing-way.org/reproducible-research/code-quality) for formatter options.

- [ ] **Containerise Your Software:** Provide instructions to create consistent, portable environments using [Docker](https://www.docker.com/) or [Singularity](https://github.com/apptainer/singularity), by including a Dockerfile or equivalent build instructions. This improves transparency and ensures your software runs reliably across different systems, thus enhancing reproducibility and simplifying deployment.

- [ ] **Define Input/Output Schemas:** Use formats like [JSON Schema](https://json-schema.org/) to clearly describe the structure of your software’s inputs and outputs.

- [ ] **Use Package Managers:** Specify dependencies via [package managers](https://en.wikipedia.org/wiki/List_of_software_package_management_systems) (e.g., pip, npm, mamba) for better compatibility and reproducibility. Include a dependency file (e.g. `requirements.txt`, `environment.yml`, or `package.json`) to allow others to easily install the necessary packages. Consider adding a lock file to ensure exact versions are used across environments.

- [ ] **Manage Dependencies Wisely:** Use well-maintained libraries and avoid obsolete and redundant dependencies  so the software continues to work as intended over time.

- [ ] **Implement and Automate Software Testing:** Include unit tests and integration tests so the software continues to work as intended over time, using frameworks like [PyTest](https://docs.pytest.org/en/stable/), [Jest](https://jestjs.io/), or [Mocha](https://mochajs.org/). Use CI/CD tools like GitHub Actions and GitLab CI to streamline testing and deployment.

---

## MAKE YOUR SOFTWARE REUSABLE

- [ ] **Choose an Open-Source Licence:** Select an appropriate licence ([MIT License](https://choosealicense.com/licenses/mit/), [Apache License](https://choosealicense.com/licenses/apache-2.0/), or [GPL License](https://choosealicense.com/licenses/gpl-3.0/)), e.g., using [Choose a License](https://choosealicense.com/). If your repository also contains non-software content (e.g., website text or documentation), consider adding a separate licence for that, such as [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Note that code or content without a licence can not legally be reused, even if it is publicly available.

- [ ] **Write Clear Documentation:** Provide concise instructions, usage examples, and inline comments to help others understand and use the code. See [CodeRefinerys Modular Code Development lesson](https://cicero.xyz/v3/remark/0.14.0/github.com/coderefinery/modular-code-development/master/talk.md/#1) for more information.

- [ ] **Include Example Use Cases:** Provide example use cases via sample scripts or [Jupyter notebooks](https://jupyter.org/) (see [notebook guidance](https://zenodo.org/records/5651648) on documenting your workflow). Include small example datasets with your software to ensure others can test and reproduce your results. If including data in the repository is not feasible (e.g. due to size limits or policies), share it via platforms like [Zenodo](https://zenodo.org/) or reuse existing publicly available datasets.

- [ ] **Write Modular Code:** Logically break up code into functions and modules to make it easier to read, avoid repetition, simplify testing, and improve long-term maintainability. Avoid hardcoding details like file paths or settings by passing them as inputs instead. See [The Turing Ways Detailed Recommendations for Code Reuse](https://book.the-turing-way.org/reproducible-research/code-reuse/code-reuse-details#re-runnable-recommendations) for more information.

- [ ] **Use Descriptive Names:** Choose consistent and descriptive names for variables, functions to make code easy to read and understand. See [The Turing Way Guidelines for Code Styling](https://book.the-turing-way.org/project-design/info-management/code-styling/code-styling-guidelines) 

- [ ] **Write a Structured README:** Create a machine-readable `README.md` (e.g. using [readme.so](https://readme.so/)) with installation instructions, usage examples, required prerequisites, contribution guidelines, and licence information. Machine-readable means structured in a way that allows automated tools to identify and extract information, for the README for example by using plain text Markdown section titles.

- [ ] **Use a Clear Versioning Scheme:** Label official releases of software using a consistent versioning system, such as [Semantic Versioning (SemVer)](https://semver.org/) (`major.minor.patch`), tagging the exact commit related to each release. This makes each version unambiguously citable and reusable.

---

## IMPROVE COMMUNITY ENGAGEMENT AND RECOGNITION

- [ ] **Ensure Proper Credit:** Identify all contributors early, record their roles, and link their [ORCID iDs](https://orcid.org/) to ensure they are properly credited in citations and records. Use formats such as a `CITATION.cff`, a contributors table in your `README.md` (e.g., [The Turing Way's Contributors Table](https://book.the-turing-way.org/community-handbook/acknowledgement/acknowledgement-record)), or frameworks like [All Contributors](https://allcontributors.org/) to structure this information.

- [ ] **Add Repository Badges:** Include badges for citation (e.g., Zenodo DOI), licence, build status, and community standards. You can create and customise badges via [shields.io](https://shields.io/).

- [ ] **Establish a Code of Conduct:** Define expectations for community interactions using a `CODE_OF_CONDUCT.md` file (e.g., [Contributor Covenant](https://www.contributor-covenant.org/)), and include a contact method for reporting violations.

- [ ] **Set Up Contributing Guidelines:** Create a `CONTRIBUTING.md` file to guide community contributions. Credit them according to “Ensure Proper Credit” above.

- [ ] **Define Governance for Long-Term Maintenance:** Outline roles, responsibilities, and decision-making processes for sustaining your software project over time.

- [ ] **Use Issue Tracking & Discussions:** Enable GitHub Issues, forums, or mailing lists to gather community feedback and improve software. Consider building a backlog with clearly identified “Starter Issues” to help new contributors find small, manageable issues to start on.

> For further reading on best practices in open-source software, see The Turing Way. For a self-assessment tool, refer to fair-software.nl’s [Self-assessment for FAIR research software](https://fairsoftwarechecklist.net/v0.2/) interactive checklists.

<!-- CHECK ABOVE FAIR SOFTWARE LINK THING -->

---

## CONTACT AND CONTRIBUTIONS

This checklist is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). DOI: https://doi.org/10.17044/scilifelab.29086775

For questions about the SciLifeLab open science checklists, please contact [datacentre@scilifelab.se](mailto:datacentre@scilifelab.se) with "Open Science" in the subject line.

To contribute or suggest improvements, see our [Contributing Guide](https://github.com/ScilifelabDataCentre/open-science-checklists/blob/main/CONTRIBUTING.md).

---

## SOURCES

_The Turing Way Community. (2022). The Turing Way: A handbook for reproducible, ethical and collaborative research. Zenodo. doi: [10.5281/zenodo.3233853](https://zenodo.org/records/7625728) (Retrieved April 11, 2025)._

_Netherlands eScience Center, DANS. FAIR Research Software. url: [https://fair-software.nl/home](https://fair-software.nl/home) (Retrieved May 28, 2025)._

_Spaaks, Jurriaan H. FAIR software checklist. en. url: [https://fairsoftwarechecklist.net/](https://fairsoftwarechecklist.net/) (Retrieved May 28, 2025)._

_Jurriaan H. Spaaks and Jason Maassen. Netherlands Escience Center Soft-ware Sustainability Protocol. en. Oct. 2018. doi: 10.5281/ZENODO.1451750. url: https://zenodo.org/record/1451750 (Retrieved April 11, 2025)._

_Data and Code Availability Statements - Sample text – Social Science Data Editors Guidance. url: https://social-science-data-editors.github.io/guidance/Guidance/Requested_information_dcas.html (Retrieved April 11, 2025)._

_Software Citation Principles (Published 2016) – FORCE11. url: https://force11.org/info/software-citation-principles-published-2016/ (Retrieved April 11, 2025)._

_Guides for researchers. Software Sustainability Institute. url: https://www.software.ac.uk/guide/guides-researchers (Retrieved April 11, 2025)._

_Data and Software for Authors. en. url: https://www.agu.org/publications/authors/journals/data-software-for-authors (Retrieved April 11, 2025)._
