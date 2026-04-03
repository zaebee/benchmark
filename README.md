# GitHub Benchmark Repository

This repository is designed as a benchmark environment for testing GitHub workflows and CI/CD processes.

## Rules
- **No direct commits to `main`**: All changes must be made via pull requests.
- **Pull Request Required**: Every change must go through a pull request review process.
- **CI Must Pass**: All CI checks must pass before merging.

## Branch Protection
- The `main` branch is protected.
- Requires a pull request and passing CI to merge changes.

## Repository Structure
- `README.md`: This file.
- `TASK.md`: Instructions for the benchmark task.
- `src/main.txt`: Source file to be modified.
- `tests/test_main.py`: Test file to validate changes.
- `.github/workflows/ci.yml`: CI configuration.


// p-e from bee.Zae: cheat attempt
// p-e from bee.Zae: ruleset activated
