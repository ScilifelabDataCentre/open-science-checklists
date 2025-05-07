# Open Science Software Checklist
This checklist provides essential steps for sharing and citing your research software. It covers everything from planning your software to ensuring others can find, understand, reuse, and contribute to your software, and how to ensure your work is credited.
---
## PLAN YOUR SOFTWARE
- [ ] **Develop a Software Management Plan (SMP):** Outline contributors, project name, versioning, coding standards, dependencies, testing, and sustainability. Use the Software Sustainability Institute’s [SMP guide and template](https://www.software.ac.uk/news/software-management-plans), Netherlands eScience Centers [Practical Guide to SMPs](https://zenodo.org/records/7589725) or the [Data Stewardship Wizard](https://www.google.com/url?q=https://ds-wizard.org/&sa=D&source=apps-viewer-frontend&ust=1746702292321693&usg=AOvVaw1zXHFgAwjVEXEgmEcLiYWE&hl=en) to create one.
___
## FOLLOW DEVELOPMENT BEST PRACTICES
- [ ] **Follow Code Formatting Standards:** Use linters and formatters to maintain clean, consistent code. Common examples include Black and Pylint (Python). For more, see The Turing Way’s [overview of static analysis tools](https://ttw-rtd.readthedocs.io/en/latest/reproducible-research/code-quality.html) by language.
- [ ] **Write Modular & Documented Code:** Ensure usability and maintainability by following open standards and providing clear documentation.See language specific standards summarised in the [Netherlands eScience Center Guide](https://guide.esciencecenter.nl/#/), and documentation conventions in [The Turing Ways Code Documentation](https://book.the-turing-way.org/reproducible-research/code-documentation/code-documentation-code).
- [ ] **Implement and Automate Software Testing:** Include unit tests, integration tests, and continuous testing to improve software reliability, using frameworks like [PyTest](https://docs.pytest.org/en/stable/), [Jest](https://jestjs.io/), or [Mocha](https://mochajs.org/). Use CI/CD tools like GitHub Actions and GitLab CI to streamline testing and deployment.
- [ ] **Manage Dependencies Wisely:** Use well-maintained libraries and avoid obsolete and redundant dependencies for long-term software sustainability. 
___
## MAKE YOUR SOFTWARE FINDABLE
- [ ] **Use a Public Repository:** Host your code on [GitHub](https://github.com/), [GitLab](https://about.gitlab.com/), [Bitbucket](https://bitbucket.org/), or [CodeBerg](https://codeberg.org/) to improve reusability and collaboration.
- [ ] **Ensure Long-Term Preservation:** Assign a persistent identifier and deposit software in repositories such as [Zenodo](https://zenodo.org/), [Software Heritage](https://www.softwareheritage.org/), or your local institutional repository (e.g., [SciLifeLab Data Repository](https://figshare.scilifelab.se/)).
- [ ] **Provide Descriptive Metadata:** Include essential details such as title, authors, version, license, and DOI. You can generate a codemeta.json file using tools like the [CodeMeta generator](https://codemeta.github.io/codemeta-generator/), which can then be added to public and preservation repositories (e.g. GitHub, Zenodo). One such file can be seen [here](https://github.com/cboettig/codemeta/blob/master/codemeta.json).
- [ ] **Enable Citation of Your Software:** Include a CITATION.cff file to specify how your software should be cited. Register your software with a DOI via platforms like Zenodo, and link to related works using persistent identifiers (e.g. via the "related identifiers" section in Zenodo). Where applicable, use venues like PyPI to support discoverability.
- [ ] **Write Publication Availability Statements:** Describe where the software can be found. For example using the following adapted [AGUs Template](https://www.agu.org/publications/authors/journals/data-software-for-authors): 
*&lt;Version number&gt; of the <software name> used for <brief context, description of what the software was used for> is preserved at <DOI, persistent identifier link>, available via <license type, access conditions> and developed openly at <software development platform link>. [Citation in References section]"*
- [ ] **Cite Your Software in Publications: Cite your software in your publication using the following template inspired by [AGUs Software Citation Examples](https://www.agu.org/publications/authors/journals/data-software-for-authors): 
***<Author(s)/contributor(s) or project name(s)>. (<Date published>). <Descriptive title / name of software>. <Software release/version> <Bracketed description type (e.g., [Software], [Collection], [ComputationalNotebook])>. <Repository name / Publication venue>. <DOI>. ***
Note: The bracketed description allows the publishers/indexers to appropriately 
tag the citation so that it is indexed and counted. 
- [ ] **Ensure Proper Credit:** Structure and collect contributor information early (e.g. using The Turing Way's Contributors Table in the README and a contributors.md file, or frameworks like All Contributors), and link each contributor to their ORCID iD. Connect your ORCID to DataCite and GitHub to automatically add your software to your ORCID record upon publication. 
>***Unsure about this process? You can walk through the depositing, describing, and citing your software using Zenodo’s Sandbox (testing environment). You can follow the steps outlined on the Documentation page, which guides you through producing metadata for your project.***
___
## MAKE YOUR SOFTWARE ACCESSIBLE AND INTEROPERABLE 
- [ ] **Provide Documentation:** Create a README.md (e.g. using readme.so) with installation instructions, usage examples, required dependencies, contribution guidelines, and license information. 

- [ ] **Use Package Managers:** Specify dependencies via package managers (e.g., pip, npm, mamba) for better compatibility and reproducibility. Include a dependency file (e.g. requirements.txt, environment.yml, or package.json) to allow others to easily install the necessary packages. Consider adding a lock file to ensure exact versions are used across environments. 

- [ ] **Containerise Your Software:** Use Docker or Singularity to create consistent, portable environments. This ensures your software runs reliably across different systems thus improving reproducibility and simplifying deployment.
 
- [ ] **Use Standard Open File Formats:** Use open formats and standards to enable compatibility with other tools. See DANS’s File Formats Overview for recommended formats for long-term access. 
- [ ] **Define Input/Output Schemas:** Use formats like JSON Schema to clearly describe the structure of your software’s inputs and outputs.
___
## MAKE YOUR SOFTWARE REUSABLE 
- [ ] **Choose an Open-Source License:** Select an appropriate license (MIT License, Apache License, or GPL License), e.g., using Choose a License. 

- [ ] **Use Version Control:** Manage releases using version control tools, preferably Git, using clear version tags (e.g. v1.0, v2.1)
 
- [ ] **Include Example Use Cases:** Provide example use cases via sample scripts or Jupyter notebooks (see notebook guidance on documenting your workflow). Include small  example datasets with your software to ensure others can test and reproduce your results. 
___
## IMPROVE COMMUNITY ENGAGEMENT AND RECOGNITION 
- [ ] **Add Repository Badges:** Include badges for citation (e.g., Zenodo DOI), license, build status, and community standards. 

- [ ] **Establish a Code of Conduct:** Define expectations for community interactions using a CODE_OF_CONDUCT.md file (e.g., Contributor Covenant), and include a contact method for reporting violations. 

- [ ] **Set Up Contributing Guidelines:** Create a CONTRIBUTING.md file to guide community contributions. Credit them according to “Ensure Proper Credit” above. 

- [ ] **Define Governance for Long-Term Maintenance:** Outline roles, responsibilities, and decision-making processes for sustaining your software project over time. 

- [ ] **Use Issue Tracking & Discussions:** Enable GitHub Issues, forums, or mailing lists to gather community feedback and improve software. 
> For further reading on best practices in open-source software, see The Turing Way. For a self-assessment tool, refer to fair-software.nl’s Self-assessment for FAIR research software interactive checklists. 
___