### Game Library

Practice game library app

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app game_library
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please
[install pre-commit](https://pre-commit.com/#installation) and enable it for
this repository:

```bash
cd apps/game_library
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting
your code:

- ruff
- eslint
- prettier
- pyupgrade

### Change to Merge Here

Hello!

### License

mit
