# Contributing to Concept Explainer

Thank you for your interest in contributing to Concept Explainer! This guide provides instructions for both human contributors and AI assistants.

## General Workflow

1. Create an issue describing the problem or enhancement
2. Create a feature branch
3. Make your changes
4. Create a pull request
5. Wait for review

## Creating Issues

When creating issues, follow these guidelines:

### Using GitHub Web Interface
- Use clear, descriptive titles
- Use markdown formatting for better readability
- Structure your issue with clear sections (e.g., Current Situation, Proposed Changes)
- Add appropriate labels (e.g., enhancement, bug, documentation)

### Using GitHub CLI (gh)
- Use the `--body-file` option instead of `--body` for proper formatting:
```bash
# Create a markdown file first
cat > issue_body.md << 'EOL'
## Description

Your properly formatted markdown here...
EOL

# Create the issue using the file
gh issue create --title "Your Title" --body-file issue_body.md --label enhancement
```

- Never use escaped newlines (`\n`) in the body text as they will be displayed literally
- Ensure proper spacing between sections for readability

## Making Changes

### Branch Naming
- Use prefixes for your branches:
  - `feature/` for new features
  - `fix/` for bug fixes
  - `docs/` for documentation changes
  - `update/` for dependency updates
  - `refactor/` for code refactoring

### Commit Messages
- Use conventional commit format:
  - `feat:` for new features
  - `fix:` for bug fixes
  - `docs:` for documentation changes
  - `chore:` for maintenance tasks
  - `refactor:` for code refactoring
- Keep commit messages clear and descriptive
- Reference issues in commit messages when applicable

## Creating Pull Requests

### Using GitHub CLI (gh)
- Create a properly formatted markdown file for the PR body:
```bash
# Create PR body file
cat > pr_body.md << 'EOL'
Closes #<issue-number>

## Changes Made
- Change 1
- Change 2

## Testing Done
- [ ] Test 1
- [ ] Test 2
EOL

# Create PR using the file
gh pr create --title "type: descriptive title" --body-file pr_body.md --label enhancement
```

### PR Guidelines
- Link to related issues using "Closes #X" or "Relates to #X"
- Include a clear description of changes
- Add a testing checklist
- Update documentation if needed
- Ensure all tests pass
- Request review when ready

## For AI Assistants

### Best Practices
1. Always use `--body-file` with `gh` commands for proper markdown formatting
2. Create temporary files for issue/PR bodies, then clean them up
3. Use proper markdown formatting in all documentation
4. Include specific sections in issues and PRs:
   - Current Situation/Problem
   - Proposed Changes
   - Benefits
   - Testing Required
5. When updating dependencies:
   - List specific version changes
   - Document any API changes required
   - Include migration steps if needed

### Common Pitfalls to Avoid
1. Don't use escaped newlines (`\n`) in command line arguments
2. Don't use echo with multiple lines for issue/PR creation
3. Don't forget to clean up temporary files
4. Don't create duplicate issues/PRs - check existing ones first
5. Don't forget to update documentation when making changes

## Code Style

- Follow PEP 8 for Python code
- Use type hints where applicable
- Keep functions focused and single-purpose
- Document complex functions and classes
- Add comments for non-obvious code sections

## Testing

- Add tests for new features
- Update tests when modifying existing features
- Ensure all tests pass before submitting PR
- Include both unit and integration tests where applicable

## Questions?

If you have any questions about contributing, please open an issue with the label "question". 