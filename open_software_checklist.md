# Open Science Software Checklist
This checklist provides essential steps for sharing and citing your research software. It covers everything from planning your software to ensuring others can find, understand, reuse, and contribute to your software, and how to ensure your work is credited.
---
## PLAN YOUR SOFTWARE
- [ ] **Develop a Software Management Plan (SMP):** Outline contributors, project name, versioning, coding standards, dependencies, testing, and sustainability. Use the Software Sustainability Institute’s [SMP guide and template](https://www.software.ac.uk/news/software-management-plans), Netherlands eScience Centers [Practical Guide to SMPs](https://zenodo.org/records/7589725) or the [Data Stewardship Wizard](https://www.google.com/url?q=https://ds-wizard.org/&sa=D&source=apps-viewer-frontend&ust=1746702292321693&usg=AOvVaw1zXHFgAwjVEXEgmEcLiYWE&hl=en) to create one.
___
## FOLLOW DEVELOPMENT BEST PRACTICES
- [ ] **Follow Coding Standards:** Use linters and formatters to maintain clean, consistent code. Common examples include Black and Pylint (Python). For more, see The Turing Way’s [overview of static analysis tools](https://ttw-rtd.readthedocs.io/en/latest/reproducible-research/code-quality.html) by language.
- [ ] **Write Modular & Documented Code:** Ensure usability and maintainability by following open standards and providing clear documentation.See language specific standards summarised in the [Netherlands eScience Center Guide](https://guide.esciencecenter.nl/#/), and documentation conventions in [The Turing Ways Code Documentation](https://book.the-turing-way.org/reproducible-research/code-documentation/code-documentation-code).
- [ ] **Implement and Automate Software Testing:** Include unit tests, integration tests, and continuous testing to improve software reliability, using frameworks like [PyTest](https://docs.pytest.org/en/stable/), [Jest](https://jestjs.io/), or [Mocha](https://mochajs.org/). Use CI/CD tools like GitHub Actions and GitLab CI to streamline testing and deployment.
- [ ] **Manage Dependencies Wisely:** Use well-maintained libraries and avoid obsolete and redundant dependencies for long-term software sustainability. 
___