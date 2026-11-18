# Convert dates to ISO weeks: implementation

## What the example does

ISO week years can differ from calendar years near New Year. Weeks start on Monday and week one contains the first Thursday.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
"2021-01-01"
```

Expected result:

```json
{
  "year": 2020,
  "week": 53,
  "weekday": 5
}
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
