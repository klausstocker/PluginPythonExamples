# Codex Handoff Context

## Project goal

Develop a bilingual Python teaching script for HTL students in Austria, roughly ages 15–19.

The teaching script is written in Markdown. The German and English versions are kept as separate files under `script/de/` and `script/en/`.

The practical exercises/examples are implemented in this repository under `examples/` and should follow the repository conventions in `agents.md`.

## Current topic: Variables

The first content module is `variables`:

- `script/en/variables.md`
- `script/de/variables.md`

The material is based mainly on an uploaded Python variables guide and the existing HTL Python presentation. The teaching scope for this first variables module was intentionally narrowed for beginners.

### Include at this stage

- what a variable is
- assignment with `=`
- reassignment
- meaningful variable names
- Python naming rules
- `snake_case`
- the basic types `int`, `float`, `str`, and `bool`
- `type()` for inspecting types
- simple multiple assignment
- simple value swapping
- constants as a naming convention using uppercase names
- small technical examples suitable for HTL students

### Postpone to later modules

Do not make the exercises depend on concepts that have not yet been taught. In particular, postpone these unless an exercise absolutely needs the existing repository test interface:

- conditions / `if`
- loops
- lists and dictionaries
- functions as a teaching topic
- variable scope / `global`
- type hints
- advanced unpacking
- classes / OOP

## Intended example progression

Create several small examples of increasing difficulty. Good candidates are:

1. very simple variable assignment and reassignment
2. electrical power calculation using `P = U * I`
3. temperature conversion
4. a slightly more involved technical calculation using several measured quantities

Prefer HTL-relevant contexts such as electrical engineering, automation, robotics, measurement, or data processing over generic shopping/person examples.

## Example structure

Follow `agents.md` and the existing `template/` folder.

Each example should normally contain:

- `README.md` — task, learning goal, files, and test instructions
- `answer.py` — reference implementation
- `test_answer.py` — tests, preferably using built-in `unittest`

Keep examples self-contained, readable, and easy for teachers and students to copy and adapt.

## Didactic style

- Target learners are technical-school students, not professional Python developers.
- Prefer explicit, readable code over clever or compact code.
- Use descriptive English identifiers in code where practical so both German and English teaching material can refer to the same source files.
- Avoid introducing extra syntax just to make an exercise more elegant.
- Example data in tests should differ from demonstration values where practical.
- Keep external dependencies to a minimum.

## Repository workflow

This branch is intended for implementing the practical examples for the variables module. The teaching-script content itself is currently maintained primarily in the web chat and lives on `main` under `script/`.

When examples are ready, they can later be linked from both language versions of the variables chapter.
