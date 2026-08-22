# Python Teaching Script

This directory contains the bilingual Python teaching script for HTL students.

The script is maintained in separate English and German Markdown files so each language can be read and exported independently.

## Structure

```text
script/
├── en/
│   └── chapter_template.md
├── de/
│   └── chapter_template.md
└── README.md
```

Future chapters should use matching chapter numbers and filenames in both language directories, for example:

```text
script/en/01_introduction.md
script/de/01_einfuehrung.md
```

The chapter templates define the common structure for explanations, examples, exercises, and quizzes. Practical programming examples should normally live in `examples/` and be linked from the corresponding chapter.

## Workflow

1. Create the chapter in English and German from the templates.
2. Keep the learning objectives and technical scope equivalent in both languages.
3. Add or reuse practical examples under `examples/`.
4. Link each practical example from the chapter.
5. Add exercises and a short self-check quiz at the end of the chapter.
6. Keep Python code, identifiers, filenames, and technical syntax identical in both language versions whenever practical.
