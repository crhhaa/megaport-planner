# CLAUDE.md

## Environment

- **Language**: Python 3.13.6
- **Package manager**: [uv](https://docs.astral.sh/uv/) — use `uv` for all dependency management, not `pip` directly.

## Common Commands

```bash
# Install dependencies
uv sync

# Run the project (update once an entry point is defined)
uv run python <entry_point>

# Add a dependency
uv add <package>

# Run tests (update once a test framework is configured)
uv run pytest
```


*All code you produce will undergo an automated AI review. It is mandatory to ensure the code is error-free, highly optimized, and follows best practices to achieve the intended outcome effectively.*