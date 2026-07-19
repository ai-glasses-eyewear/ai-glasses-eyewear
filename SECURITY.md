# Security Policy

This is an open data and documentation repository (the AI Glasses Open
Database). It contains datasets, schema, scripts, and docs. It does not ship a
running service, but we still take the integrity of the data and the safety of
contributors seriously.

## Reporting a vulnerability

Please report suspected vulnerabilities **privately**. Do **not** open a public
issue, pull request, or discussion for a security problem.

Email: **sales@ai-eyewear.ch**

Include, where possible:

- a description of the issue and its impact;
- the file, path, or workflow affected;
- steps to reproduce;
- any suggested fix.

We aim to acknowledge reports within a few working days. We are a small team and
cannot commit to a fixed response deadline, but we will keep you informed as we
investigate.

## Scope

In scope:

- integrity or correctness problems that could mislead data consumers;
- issues in the repository's scripts or GitHub Actions workflows;
- accidental exposure of secrets in the repository history.

Out of scope:

- the commercial website and its infrastructure (report those to the same
  address, but note they are separate from this repository);
- vulnerabilities in third-party tools that merely consume this dataset.

## Credential and secret handling

Never place secrets in this repository or its metadata. Specifically:

- do **not** put tokens, passwords, API keys, or other credentials in issues,
  pull requests, commit messages, commit contents, documentation, or GitHub
  Actions logs;
- if a secret is exposed, treat it as compromised: rotate it immediately and
  report it privately using the email above.

We recommend maintainers and contributors:

- enable **GitHub secret scanning** (and push protection) on forks and the main
  repository;
- enable **two-factor authentication (2FA)** on their GitHub accounts.

## Supported versions

Only the **latest release** of the dataset is supported. Security and integrity
fixes are applied to the current release; older snapshots are kept for
provenance but are not maintained.
