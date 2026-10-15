# Observed LeTTo export conventions

These conventions come from the repository's `.lto` files and the user's
successive corrections. They are project conventions, not a complete LeTTo XSD.
The newest user-edited question takes precedence over this reference.

## Container and question linkage

Use a UTF-8 XML declaration followed by `<letto mode="101" databaseinfo="sql">`.
Each question is `<question type="MoodleClozeCalc">` with `questionType` 22.
Keep the reference's other grading and presentation fields. Imported questions
may have real database IDs. Reset copied IDs and text ID attributes only for a
new question; never reuse another question's real IDs.

The HTML task belongs in `text[@art="Questiontext"]/inhalt` as CDATA. Include
`[Q0]`. Its `subquestion` uses name `Q0`, mode 6, and `plugininfo` equal to
`Plugin1:`. Preserve the reference's answer structure. Empty XML elements such
as `<maxima/>` and `<maxima></maxima>` are equivalent.

## Plugin payload

The actual XML tag is plural: `plugins`. Its CDATA text has this exact envelope:

```text
[PI Plugin1 Python "{JSON object}"]
```

The opening and closing quotes belong to the LeTTo envelope. Serialize the
inner object with `json.dumps(..., ensure_ascii=False, separators=(",", ":"))`;
do not JSON-encode the entire envelope or escape it a second time. Python
newlines and quotes must be encoded by the JSON serializer. Use an XML writer
that preserves CDATA, and check parsing after writing.

The corrected examples use these configuration fields:

| Field | Meaning or convention |
| --- | --- |
| `datasetVariables` | Objects with `name`, preview `value`, and `unit: ""` |
| `validation` | Self-contained Python reference and `unittest.Checker` |
| `indication` | Student starter: comment or function stub, not the solution |
| `files` | `{}` for these self-contained exercises |
| `evalConfig` | `runAtTest: true`, `lintAtTest: true` |
| `linterConfig` | Default: `--disable=all --enable=F,E,W` |
| `linterWeight` | `0.5` in the latest corrected templates |
| `cpuTime` | `5` in the latest corrected templates |
| `formatterConfig` | Empty string |

Preserve explicit per-question settings. Dataset-backed examples use
`sendToParser` and `preCalc` set to `true`. The target provides `answer.py`,
`dataset`, and `helpers.RedirectedStdout`. Grade by capturing `import answer`
and the reference implementation separately. Do not require `runpy`,
`__file__`, mocked console input, repository paths, or local helper files in
the exported validator.

Student-facing text describes the given quantities directly using placeholders,
for example `Ein Behälter enthält {fuellstand} Liter`. Do not name dataset
variables as an input interface or mention the hidden `dataset` module,
`DatasetVariable`, or `.value`. Technical configuration belongs in teacher
documentation. Required function parameter names may appear in the task.

## Datasets

Every configured variable has a corresponding question-level `dataset` with
the same name. Copy the observed definition structure, including `type`,
`distribution`, `minimum`, `maximum`, `decimals`, `itemcount`, `zahlenbereich`,
`ziffern`, `einheit`, and semicolon-separated `items`.

- Dataset `einheit` is empty, matching JSON `unit: ""` and local Python.
- Preview values and local defaults match the first item of each variable.
- Items at the same index form one complete dataset. Counts must agree across
  variables, normally 40. Each row must satisfy task prerequisites.
- The observed integer range syntax is `I3-7`. For decimal values, preserve
  known working range syntax, such as the user's `F2:2-7` for robot positions.
  Do not guess new range syntax or overwrite related precision fields without
  an established reference.
- The robot export has `decimals` 0 despite floating-point items. Do not infer
  that this field alone determines the numeric type.
- Preserve the reference's dataset status unless the task requires changing it;
  the latest edited robot/power exports have empty status elements.

Units such as `mm`, `°C`, or `W` may still appear in task text and output. Empty
dataset units do not mean removing those labels from the exercise.

## Checks before handing over

Parse XML, unwrap and decode plugin JSON, compile both embedded Python strings,
and verify variable names, empty units, item counts, first-row defaults, and
dataset bounds. Verify output using the native-style validator for all dataset
rows and compare affected single/combined entries. Inspect required loop forms
and helper calls in the source; output equality alone cannot enforce them.
