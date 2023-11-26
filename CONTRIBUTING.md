
# Contributing

The following resources and rules are adopted by the [ACSECompendium](https://github.com/joe-stifler/acse_compendium) repository to ensure consistency and quality in our codebase. Links are aggregated from various sources, in special our ACSE module classes. Feel free to suggest changes and improvements to this document.

## Main Book Reference:

There are many great books out there. But one of my favorite ones is [Software Engineering at Google](https://abseil.io/resources/swe-book/). This book is a collection of best practices and lessons learned from Google's experience in developing software collaboratively. At some point I'll try to summarize the main points of this book in this document. But for now, I highly recommend reading it.

## Standards, Rules, and Advices:

### 1. Git:
My main advice here is... learn how to quickly use [VS Code extension](https://code.visualstudio.com/docs/sourcecontrol/overview). It'll save you a lot of time and effort. Check [Git Cheat Sheet](https://training.github.com/downloads/github-git-cheat-sheet.pdf) for a quick reference on the most commonly used Git commands. But also, learn how to use [Git CLI](https://git-scm.com/docs) because it's always good to know the basics. 

### 2. Branch Methodology:
This repository adopts [Github Flow](https://githubflow.github.io/) as the branch methodology. The `main` branch is the primary and only source of truth. Check [Version Control and Branch Management](https://abseil.io/resources/swe-book/html/ch16.html) for an in-depth discussion on the topic.

### 3. Commit Message Convention:
Following the [Conventional Commits](https://www.conventionalcommits.org/) standards, this repository adopts the following commit message convention:

```
<type>: <short summary> ( <pull-request-reference> )
  │           │                       |
  |           |                       └─⫸ The PR reference number.
  |           |
  │           └─⫸ Summary in present tense. Not capitalized. No period at the end.
  │
  └─⫸ Commit Type: feat|feat!|fix|fix!|perf|perf!|refactor|refactor!|test|bench|build|ci|docs|style|chore
```

#### Commit Types:

| Type       | Description                                          | Example                                                        |
|------------|------------------------------------------------------|----------------------------------------------------------------|
| feat       | add a new feature                                    | `feat: add linear algebra solver for Computational Mathematics module` |
| feat!      | a breaking change to a feature                       | `feat!: add linear algebra solver for Computational Mathematics module` |
| fix        | a bug fix                                            | `fix: correct data preprocessing bug in ML project`            |
| fix!       | a breaking change to a bug fix                       | `fix!: correct data preprocessing bug in ML project`           |
| perf       | a code change that improves performance              | `perf: optimize pipeline for reduced training time`            |
| perf!      | a breaking change to a performance improvement       | `perf!: optimize pipeline for reduced training time`           |
| refactor   | a code change that neither fixes a bug nor adds a feature | `refactor: optimize pipeline for reduced training time`        |
| refactor!  | a breaking change to a refactoring                  | `refactor!: optimize pipeline for reduced training time`       |
| test       | adding missing tests or correcting existing tests   | `test: add unit tests for data preprocessing pipeline`         |
| bench      | improvements to benchmarks                          | `bench: improve performance of data preprocessing pipeline`    |
| build      | changes to build system or external dependencies    | `build: update dependencies for Data Science module`           |
| ci         | changes to CI configuration files and scripts       | `ci: update CI configuration for Data Science module`          |
| docs       | documentation only changes                          | `docs: update README for Modern Programming Methods`           |
| style      | changes that do not affect the meaning of the code  | `style: update code formatting for Data Science module`        |
| chore      | changes to the build process or auxiliary tools and libraries | `chore: update dependencies for Data Science module`        |


#### Rules:
```markdown
1) must follow the commit naming convention.
2) must be concise and descriptive.
3) must be written in English.
4) must start with a verb in imperative mood.
5) must be written in present tense.
6) must not end with a period.
```

### 4. Branch Naming Convention:
The branching naming convention uses the same types specified in the commit message convention. Its format is specified as follows:

```
<type>/<issue-reference>/<description>
  │           │                |
  |           |                └─⫸ A short description of the branch's purpose.
  |           |
  │           └─⫸ The github issue/ticket number. Use `no-ref` if no issue.
  │
  └─⫸ Branch Type: feat|feat!|fix|fix!|perf|perf!|refactor|refactor!|test|bench|build|ci|docs|style|chore
```

#### Examples:

```markdown
fix/no-ref/update-dependencies

fix/issue-27/fix-data-sync-error

test/no-ref/refactor-math-algorithms

feature/issue-15/implement-regression-analysis
```

### 5. Pull Requests (PRs) and Code Reviews:

Pull Requests are used to propose and review changes to the codebase. The person asked as a reviewer is responsible for reviewing the changes, ensuring that only high-quality code is merged into the main branch. The person who opened the PR is responsible for addressing the feedback and making sure that the PR is ready to be merged. Besides, according to [Software Engineering at Google - Code Review Chapter](https://abseil.io/resources/swe-book/html/ch09.html), the code review process is also a great opportunity to share knowledge, learn from each other, and document the changes for the posterity. Now, to ensure that everybody follows the same standards, this repository adopts the following PR template and rules:

**PR Title:**
```
- follows the same same commit naming convention.
```

**PR Description:**
```markdown
## Why this PR?
- Explain the need for this change.

## What Changes?
- Summarize the proposed changes.

## Tests added?
- Mention test status.

## Breaking changes created?
- Note any potential public interface disruptions.

## Additional context:
- Provide any additional information.
```

### Example:

**PR Title:**
```markdown
perf: optimize pipeline for reduced training time (#1234)
```

**PR Description:**
```markdown
## Why this PR?
- This PR addresses a critical performance issue in our machine learning model training process.
- During testing, we identified a significant bottleneck in data preprocessing, leading to excessive training times.

## What Changes?
- In the `DataPreprocessing` class located in the `data_processing.py` module, we've optimized the data loading and transformation process with:
    - Multi-threading strategies for parallel data loading, reducing I/O wait times.
    - Memory-efficient data chunking and caching strategies, minimizing memory usage during processing.
- These enhancements collectively result in a 40% reduction in training time for our machine learning models, while preserving model accuracy.

## Tests added?
- Yes, we've included comprehensive unit tests for the updated preprocessing pipeline to ensure it functions correctly and does not introduce regressions.

## Breaking changes created?
- No, this optimization does not introduce any breaking changes.
- Existing code that relies on the data preprocessing pipeline should continue to work as expected.

## Additional context:
- This PR is related to issue #1234 and has been reviewed by our data science team.
- It significantly improves the efficiency of our model training pipeline and aligns with our goal of reducing model development time.
```

### Rules:
- PRs titles must follow the commit naming convention.
- PRs must have a description that follows the PR template.
- PRs must be linked to a GitHub issue.
- PRs must be reviewed by at least one team member that understands the changes.
- PRs must be tagged with the appropriate labels.
- PRs must be assigned to the appropriate team member.
- PRs must be linked to the appropriate milestone.
- PRs must be linked to the appropriate project.
- PRs must pass all automated checks before merging.
- PRs must always be merged using the `Squash and Merge` method.
- PRs must be up to date with the `main` branch before merging.

### 6. Issues:

TODO

### 7. Code Style:

TODO

### 8. Continuous Integration and Deployment:

TODO

### 9. Semantic Versioning and Releases:

TODO

### 10. Collaboration and Communication:

TODO


## Relevant Resources:
### 1. Git:
- [Git Documentation](https://git-scm.com/docs): official Git documentation.
- [VS Code Git Extension](https://code.visualstudio.com/docs/sourcecontrol/overview): VS Code extension for Git.
- [Pro Git](https://git-scm.com/book/en/v2): free online book on Git.
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf): quick reference on the most commonly used Git commands.


### 2. Branch Methodology:
- [GitHub Flow](https://githubflow.github.io/): a lightweight, branch-based workflow suitable for various projects.
- [Please stop recommending Git Flow!](https://georgestocker.com/2020/03/04/please-stop-recommending-git-flow/): a critique of Git Flow.
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
- [Version Control and Branch Management](https://abseil.io/resources/swe-book/html/ch16.html): a chapter from [Software Engineering at Google](https://abseil.io/resources/swe-book) on version control and branch management.

### 3. Branch Naming Convention:
- [Conventional Commits](https://www.conventionalcommits.org/): a specification for commit messages.
- [A Simplified Convention for Naming Branches and Commits in Git](https://dev.to/varbsan/a-simplified-convention-for-naming-branches-and-commits-in-git-il4): a simplified version of the Conventional Commits specification.

### 4. Commit Message Convention:
- [Conventional Commits](https://www.conventionalcommits.org/): a specification for commit messages.
- [Angular Commit Message Guidelines](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines): a guide for commit messages from the Angular project.

### 5. Pull Requests (PRs) and Code Reviews:
- [GitHub PRs](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests): official GitHub documentation on PRs.
- [GitHub PR Templates](https://docs.github.com/en/github/building-a-strong-community/creating-a-pull-request-template-for-your-repository): official GitHub documentation on PR templates.
- [GitHub PR Labels](https://docs.github.com/en/github/managing-your-work-on-github/applying-labels-to-issues-and-pull-requests): official GitHub documentation on PR labels.
- [GitHub PR Assignees](https://docs.github.com/en/github/managing-your-work-on-github/assigning-issues-and-pull-requests-to-other-github-users): official GitHub documentation on PR assignees.
- [GitHub PR Milestones](https://docs.github.com/en/github/managing-your-work-on-github/about-milestones): official GitHub documentation on PR milestones.
- [GitHub PR Projects](https://docs.github.com/en/github/managing-your-work-on-github/about-project-boards): official GitHub documentation on PR projects.
- [GitHub PR Checks](https://docs.github.com/en/actions/guides/about-continuous-integration): official GitHub documentation on PR checks.
- [Github Merge Methods](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github): official GitHub documentation on PR merge methods.

### 6. Issues:

TODO

### 7. Code Style:
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html): this guide describes the Python style conventions adopted by Google.

- [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html): this guide describes the C++ style conventions adopted by Google.

### 8. Continuous Integration and Deployment:

TODO

### 9. Semantic Versioning and Releases:

TODO

## Further Discussions:

### Why Adopt Standards?
Adopting standards in software development is crucial for maintaining consistency, improving code readability, and facilitating collaboration. As outlined in [Style Guides and Rules](https://abseil.io/resources/swe-book/html/ch08.html), consistent standards help mitigate the complexity that comes with collaborative projects. Moreover, standardization aids in automation processes like [Semantic Versioning](https://semver.org/) and [Releases](https://github.com/semantic-release/semantic-release), making the development workflow more efficient and predictable.

### GitHub Flow
GitHub Flow is a lightweight, branch-based workflow suitable for various projects. It emphasizes collaboration, review, and prompt integration.

**Workflow Steps:**
1. **Creating a Branch**: Separate from the default for new features or fixes.
2. **Making Changes**: Implement and commit changes to the branch.
3. **Opening a Pull Request (PR)**: For discussion and review.
4. **Review and Revision**: Address feedback and revise as needed.
5. **Merging to the Default Branch**: Once approved, merge the changes.
6. **Deleting the Branch**: Indicates completion of the work.

This process encourages continuous integration and regular updates, ensuring efficient review and integration of changes.



## Glossary:

- **Git:** An open-source, distributed version-control system.
- **GitHub:** A platform for hosting and collaborating on Git repositories.
- **Commit:** A Git object representing a snapshot of the entire repository. Compressed into a unique SHA identifier.
- **Branch:** A lightweight, movable pointer to a commit. Allows parallel development of features or fixes.
- **Clone:** A local copy of a repository with all commits and branches.
- **Remote:** A common repository on GitHub for team collaboration.
- **Fork:** A copy of a repository on GitHub owned by a different user.
- **Pull Request:** A space to compare and discuss differences in a branch. Includes reviews, comments, tests, and more.
- **HEAD:** Represents the current working directory. Can be moved to different branches, tags, or commits using `git checkout`.

Content borrowed from [Git Cheat Sheet](https://training.github.com/downloads/github-git-cheat-sheet.pdf).

## ⚠️ this file was created with the help of ChatGPT.
