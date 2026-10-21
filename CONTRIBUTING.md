# Proposed Git Workflow for the Kona Kapital Team

## Branching (GitHub Flow)
- `main` is always deployable. Never commit directly to it.
- Create a short-lived branch per task: `feature/<name>`, `fix/<name>`, `docs/<name>`.
- Open a Pull Request into `main`; at least one teammate reviews before merging.
- Delete the branch after it is merged.

## Commits
- One topic per commit. Use `git add -p` to stage only related changes.
- Subject line: imperative, under 72 characters (e.g. "Add budget summary card").
- Leave a blank line, then a body explaining what changed, why, and anything to watch out for.

## Rebasing
- Only rebase your own local, unpushed commits. Never rewrite history on `main` or on shared branches.
- If a merge conflict gets messy, `git merge --abort` and ask the teammate who made the other change.