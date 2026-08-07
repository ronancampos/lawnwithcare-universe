---
title: Repository Standards
universe: Lawn With Care Universe
document: Repository Standards
version: 1.0.0
status: CANON
author: Ronan Campos
creative_direction: OpenAI ChatGPT
last_update: 2026-08-06
---

# 🌱 Lawn With Care Universe

# Repository Standards

> "A repository is not a collection of files.
It is the collective memory of the franchise."

---

# Purpose

This document defines the official standards governing the organization, maintenance and evolution of the Lawn With Care Universe repository.

The repository is the permanent knowledge base of the franchise.

Every contributor—human or AI—must follow these standards.

---

# Repository Philosophy

The repository exists to make knowledge permanent.

Conversations are temporary.

Ideas are temporary.

Documentation is permanent.

The repository is always the single source of truth.

---

# Core Principles

The repository should always be:

Simple.

Predictable.

Consistent.

Searchable.

Scalable.

Readable.

Versioned.

Self-documenting.

---

# Repository Structure

The project is divided into clearly defined domains.

```
00-Franchise
01-Characters
02-World
03-Storytelling
04-Art
05-AI
06-Studio
07-Marketing
08-Comics
09-Assets
10-References
11-Templates
12-Lore
13-Episodes
```

Folders represent knowledge domains.

They never represent software.

---

# Folder Rules

Every folder has one clear responsibility.

Avoid overlapping content.

Documentation belongs where it is maintained.

Not where it is temporarily used.

---

# README Rule

Every major folder should contain a README.md.

The README explains:

Purpose.

Contents.

Reading order.

Related folders.

Contributors should understand a folder before opening its documents.

---

# Naming Convention

Use:

English.

Title Case for document titles.

Hyphen-separated file names.

Examples

```
Story-Bible.md

Discovery-System.md

Brooks-Identity.md

Episode-Structure.md
```

Avoid:

Spaces.

Special characters.

Dates in filenames.

Generic names such as:

```
Final

New

Copy

Updated

Version2
```

---

# Numbered Folders

Number prefixes define reading order.

Example

```
00-Franchise

01-Characters

02-World
```

Numbers are permanent.

Avoid renumbering unless absolutely necessary.

---

# Document Metadata

Every canonical document begins with:

```
Title

Universe

Document

Version

Status

Author

Creative Direction

Last Update
```

Metadata should remain consistent across the repository.

---

# Canon Documents

Canonical documents include:

```
status: CANON
```

Only approved documents receive this designation.

Drafts must never be labeled as canon.

---

# Draft Documents

Working drafts should clearly state:

```
status: DRAFT
```

Drafts remain outside official canon until approved.

---

# Cross References

Whenever appropriate, documents should reference related documentation.

Example

```
Related Documents

Story Bible

Episode Structure

Discovery System

World Bible
```

Documentation should form a connected knowledge network.

---

# Single Source of Truth

Each concept has one primary document.

Examples

Brooks

→ Brooks-Identity.md

Discovery Frame™

→ Discovery-System.md

Field Kit

→ Field-Equipment.md

Never duplicate canonical definitions.

Reference them instead.

---

# Images

Store reference artwork separately from production artwork.

Suggested structure

```
Reference/

Production/

Published/

Archive/
```

Avoid mixing working files with final assets.

---

# Documentation Style

Write in clear English.

Prefer short paragraphs.

Use descriptive headings.

Avoid unnecessary repetition.

Every section should have a clear purpose.

---

# Markdown Standards

Use:

ATX headings (#)

Code blocks

Tables when appropriate

Horizontal separators

Consistent indentation

Avoid HTML unless required.

---

# Links

Prefer relative links inside the repository.

Example

```
../02-World/Discovery-System.md
```

Broken links should be corrected immediately.

---

# Repository Growth

When introducing new documentation ask:

Does this belong in an existing document?

Would updating current documentation be better?

Can duplication be avoided?

Prefer expanding existing documentation.

---

# New Documents

Before creating a document verify:

Is this topic already documented?

Does it have long-term value?

Will future contributors use it?

If not,

consider updating an existing file instead.

---

# Archive Policy

Deprecated material moves to:

```
Archive/
```

Nothing important is deleted.

Project history has value.

---

# Templates

Whenever repeated structures emerge,

create templates.

Examples

Episode Brief

Character Sheet

Location Sheet

Badge Sheet

Prompt Template

Review Report

Templates reduce inconsistency.

---

# AI Contributions

AI-generated content should:

Respect repository structure.

Avoid creating duplicate concepts.

Reference existing documentation.

Identify assumptions.

Never silently modify canon.

---

# Human Contributions

Humans remain responsible for:

Creative approval.

Canon decisions.

Major revisions.

Repository organization.

The repository supports collaboration.

It does not replace judgment.

---

# Repository Maintenance

Regular maintenance includes:

Removing duplicates.

Fixing links.

Updating metadata.

Reviewing folder structure.

Improving documentation.

Archiving obsolete files.

Maintenance is part of production.

---

# Searchability

Every important concept should be discoverable through:

Document title.

Section headings.

Metadata.

Keywords.

Related documents.

Good organization is a productivity tool.

---

# Long-Term Scalability

The repository should remain understandable after:

100 episodes.

500 illustrations.

Thousands of assets.

Multiple contributors.

Several years of development.

Structure should never depend on memory.

Only on documentation.

---

# Repository Health Checklist

Regularly verify:

✓ Folder structure consistent

✓ README files updated

✓ Metadata complete

✓ Canon documents identified

✓ Links working

✓ Duplicate concepts removed

✓ Templates current

✓ Archive organized

✓ Versions synchronized

---

# Repository Promise

Every contributor should be able to:

Understand the project quickly.

Locate any document easily.

Trust the documentation.

Build upon previous work.

Without needing the original conversations.

---

# Official Repository Principle

The repository is not where the project is stored.

The repository is where the project lives.

---

# Related Documents

Studio README

Production Pipeline

AI Pipeline

Review Workflow

Asset Management

Versioning

Release Process

Quality Assurance

PROJECT_STATUS

README

---

Status

CANON v1.0