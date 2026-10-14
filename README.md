# AI Agent Evals Lab

A hands-on project for learning how to evaluate AI agents.

## Day 1: Refund Outcome Evaluation

### Goal
Check whether a support agent created exactly one successful
refund for the correct order and amount.

### Approach
Use synthetic agent runs and mock backend refund records.
A Python grader evaluates the outcome of each run.

### Run
python3 src/evaluate.py

### Baseline results
- Run A: PASS
- Run B: FAIL — no refund created
- Run C: FAIL — wrong order refunded
- Task success rate: 33.3%

### Limitations
These are manually created examples, not live model runs.
The grader checks refund outcomes only.
It does not yet evaluate policy compliance, tool arguments,
or final response quality.