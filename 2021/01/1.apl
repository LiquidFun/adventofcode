solve ← {+/0>-/⍉↑⍵(1↓⍵)}
solvePartTwo ← {solve 2↓⌽{+/⍉↑⍵(1↓⍵)(2↓⍵)}⌽⍵}

input ← 199 200 208 210 200 207 240 269 260 263

solve input

solvePartTwo input
