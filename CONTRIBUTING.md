# Contributing to thisyou-dev

## Development Workflow

We use a direct-to-main workflow for Copilot-assisted changes to streamline development. Human contributors should follow the branch-based process below.

### For Copilot-Assisted Changes

When Copilot makes code changes:
1. Changes are committed directly to `main`
2. Tests are run via CI/CD before changes go live
3. Changes auto-deploy to production via Render once tests pass

This streamlined workflow allows for rapid iteration while maintaining code quality through automated testing.

### For Human Contributors

1. **Create a feature branch** from `main` with a descriptive name:
   ```
   git checkout -b feature/your-feature-name
   ```
   or
   ```
   git checkout -b fix/your-bug-fix
   ```

2. **Make your changes** on the branch

3. **Commit with clear messages**:
   ```
   git commit -m "feat: add new feature" 
   git commit -m "fix: resolve bug"
   git commit -m "docs: update README"
   ```

4. **Push your branch** and **create a Pull Request** for review

5. **Get approval** before merging to `main`

### Commit Message Format

Use conventional commits to keep history clear:

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `refactor:` for code refactoring
- `test:` for test additions or changes
- `chore:` for maintenance tasks

Example: `feat: append .bsky.social to handles without dot segments`

### Branch Naming Conventions

- Feature branches: `feature/description-of-feature`
- Bug fix branches: `fix/description-of-bug`
- Documentation branches: `docs/description`

### Code Review

For human contributors:
- All changes must go through a Pull Request
- At least one approval is required before merging
- Use PRs to discuss changes and maintain code quality

### Before You Merge

- Ensure all tests pass
- Keep commits clean and organized
- Write clear PR descriptions explaining what and why

## Questions?

If you're unsure about the workflow, ask before making changes. Clear communication helps us maintain a high-quality codebase.
