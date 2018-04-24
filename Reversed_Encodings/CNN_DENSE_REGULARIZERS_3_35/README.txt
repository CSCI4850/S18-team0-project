Optimizer for all nets: Adam
-----------------------------

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
RESULTS FOR 3 AUTHORS
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Number of Authors: 3
Sampling: Normal
Batch Size: 5
Epochs: 5
Training Set: The first 4 reviews from each author
Testing Set: The remaining reviews (reviews[4:]) for each author

Testing Phase Results:

Generated Estimate | Highest Value Index | One-Hot Answer | Author Guessed | Actual Author | Correctness

  ====================================================================================================

[0.3594241  0.5587887  0.08178717] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.44883958 0.5364545  0.01470589] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.5515288  0.35430515 0.09416603] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.44887912 0.40085822 0.1502627 ] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.501065   0.42327875 0.07565626] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.51971805 0.43274927 0.04753272] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.37403232 0.48467687 0.14129083] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.49593133 0.46938747 0.03468123] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.32062528 0.66545284 0.01392183] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.3711068  0.47584236 0.15305085] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.33255368 0.5637     0.10374635] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.34827402 0.4908062  0.16091983] 1 [0. 1. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A2F1ZOWOPNJB Correct
[0.35133764 0.4854622  0.16320014] 1 [0. 1. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A2F1ZOWOPNJB Correct
[0.49080974 0.3323758  0.17681447] 0 [0. 0. 1.] Guessed: A1A1BM6N28X9J0 Actual: A1A4L7VRD74WXT Incorrect
[0.31357807 0.3670506  0.31937137] 1 [0. 0. 1.] Guessed: A1A2F1ZOWOPNJB Actual: A1A4L7VRD74WXT Incorrect
[0.3461547  0.4352732  0.21857199] 1 [0. 0. 1.] Guessed: A1A2F1ZOWOPNJB Actual: A1A4L7VRD74WXT Incorrect

Correct: 7 Incorrect: 9 Out of: 16

Optimizer for all nets: Adam
-----------------------------

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
RESULTS FOR 35 AUTHORS
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Number of Authors: 35
Sampling: Normal
Batch Size: 5
Epochs: 5
Training Set: The first 4 reviews from each author
Testing Set: The remaining reviews (reviews[4:]) for each author

Testing Phase Results:

Correct: 4 Incorrect: 235 Out of: 239

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
RESULTS FOR 3 AUTHORS (OVERSAMPLING)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Number of Authors: 3
Sampling: 3x
Batch Size: 5
Epochs: 5
Training Set: The first 4 reviews from each author
Testing Set: The remaining reviews (reviews[4:]) for each author

Testing Phase Results:


Generated Estimate | Highest Value Index | One-Hot Answer | Author Guessed | Actual Author | Correctness

  ====================================================================================================

[0.34193635 0.3513005  0.30676317] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.53218365 0.26858577 0.19923055] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.37451938 0.26682633 0.35865423] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.3458076  0.3038007  0.35039172] 2 [1. 0. 0.] Guessed: A1A4L7VRD74WXT Actual: A1A1BM6N28X9J0 Incorrect
[0.3621885  0.29829767 0.33951378] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.39055935 0.37396535 0.23547529] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.3642389  0.3269804  0.30878067] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.52413476 0.26070425 0.21516097] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.47236356 0.37368834 0.15394814] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.3289944  0.32437813 0.34662753] 2 [1. 0. 0.] Guessed: A1A4L7VRD74WXT Actual: A1A1BM6N28X9J0 Incorrect
[0.35122705 0.34488565 0.30388725] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.3310734  0.3248912  0.34403536] 2 [0. 1. 0.] Guessed: A1A4L7VRD74WXT Actual: A1A2F1ZOWOPNJB Incorrect
[0.35374975 0.3143689  0.33188134] 0 [0. 1. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A2F1ZOWOPNJB Incorrect
[0.35178167 0.31546804 0.3327503 ] 0 [0. 0. 1.] Guessed: A1A1BM6N28X9J0 Actual: A1A4L7VRD74WXT Incorrect
[0.3273694  0.31983477 0.3527958 ] 2 [0. 0. 1.] Guessed: A1A4L7VRD74WXT Actual: A1A4L7VRD74WXT Correct
[0.32703122 0.3256867  0.34728202] 2 [0. 0. 1.] Guessed: A1A4L7VRD74WXT Actual: A1A4L7VRD74WXT Correct

Correct: 10 Incorrect: 6 Out of: 16

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
RESULTS FOR 35 AUTHORS (OVERSAMPLING)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Number of Authors: 3
Sampling: 3x
Batch Size: 5
Epochs: 5
Training Set: The first 4 reviews from each author
Testing Set: The remaining reviews (reviews[4:]) for each author

Testing Phase Results:

Correct: 4 Incorrect: 235 Out of: 239