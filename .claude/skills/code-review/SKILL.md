---
name: code-review
description: Review recent code changes for quality and security issues
user-invocable: true
allowed-tools: ["Read", "Glob", "Grep", "Bash"]
---

# Code Review Skill

Review the most recent git changes:

1. Run `git diff HEAD~1` to see latest changes
2. Check for security issues (SQL injection, exposed secrets, auth bypass)
3. Verify consistency with project patterns
4. Check TypeScript types in frontend code
5. Report findings with severity: critical / warning / info
