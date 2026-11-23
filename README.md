# Office Jokes

[![make.fun · u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/nmlyz/office-jokes/rank.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/nmlyz/office-jokes/reward.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
<sub>See the entry on [make.fun](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)</sub>

A small program that writes one office joke line to a text file. The line
is assembled from two clauses: an out-of-office message that promises a
Monday return, and an inbox that spends the week applying for the job.

## Usage

Run the program with Python 3:

```sh
python3 main.py
```

## Output

The program writes `entry.txt` containing a single line. By default the
file is created in `/output`. Set the `MAKEFUN_OUTPUT_DIR` environment
variable to choose a different output directory.

Before writing, the program checks that the line is between 1 and 200
characters, fits on a single line, has no leading or trailing whitespace,
contains no double spaces, and ends with a period. After writing, it reads
the file back and confirms the bytes match exactly.
