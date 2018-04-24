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

Generated Estimate | Highest Value Index | One-Hot Answer | Auther Guessed | Actual Author | Correctness

  ====================================================================================================

[0.8017687  0.11640045 0.08183074] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.7701956  0.22289847 0.00690592] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.82292163 0.15475947 0.02231891] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.9065591  0.07859214 0.01484876] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.8558597  0.14003581 0.00410457] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.76496553 0.1947985  0.04023603] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.33935055 0.59620404 0.06444542] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.79261494 0.16554205 0.04184292] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.93216395 0.05835282 0.00948322] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.6086697  0.34349495 0.04783532] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.8010034  0.12484721 0.07414939] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.5991275  0.3811525  0.01972008] 0 [0. 1. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A2F1ZOWOPNJB Incorrect
[0.45752707 0.28674856 0.25572434] 0 [0. 1. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A2F1ZOWOPNJB Incorrect
[0.46463147 0.2914314  0.2439371 ] 0 [0. 0. 1.] Guessed: A1A1BM6N28X9J0 Actual: A1A4L7VRD74WXT Incorrect
[0.39890063 0.32838637 0.27271307] 0 [0. 0. 1.] Guessed: A1A1BM6N28X9J0 Actual: A1A4L7VRD74WXT Incorrect
[0.42029506 0.22597006 0.35373482] 0 [0. 0. 1.] Guessed: A1A1BM6N28X9J0 Actual: A1A4L7VRD74WXT Incorrect

Correct: 10 Incorrect: 6 Out of: 16

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
RESULTS FOR 35 AUTHORS
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Number of Authors: 35
Sampling: Normal
Batch Size: 5
Epochs: 5
Training Set: The first 4 reviews from each author
Testing Set: The remaining reviews (reviews[4:]) for each author

Correct: 18 Incorrect: 221 Out of: 239

Too big to show full results here...

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
RESULTS FOR 3 AUTHORS (OVERSAMPLING)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Number of Authors: 35
Sampling: 3x normal size for training
Batch Size: 5
Epochs: 5
Training Set: The first 4 reviews from each author
Testing Set: The remaining reviews (reviews[4:]) for each author

Generated Estimate | Highest Value Index | One-Hot Answer | Auther Guessed | Actual Author | Correctness

  ====================================================================================================

[0.73186874 0.06626571 0.20186557] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.32729214 0.6646403  0.00806758] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.76128274 0.15152915 0.08718819] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.451889   0.15908805 0.38902295] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.5032034  0.48808962 0.00870707] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.3730736  0.31482884 0.3120975 ] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.02338962 0.6051824  0.37142795] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.7001809  0.2566174  0.04320176] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.6946329  0.1078987  0.19746836] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.06808257 0.33536014 0.5965573 ] 2 [1. 0. 0.] Guessed: A1A4L7VRD74WXT Actual: A1A1BM6N28X9J0 Incorrect
[0.72061753 0.05766146 0.22172095] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.3971244  0.5955054  0.00737016] 1 [0. 1. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A2F1ZOWOPNJB Correct
[0.16137287 0.18743743 0.65118974] 2 [0. 1. 0.] Guessed: A1A4L7VRD74WXT Actual: A1A2F1ZOWOPNJB Incorrect
[0.20135145 0.22824834 0.57040024] 2 [0. 0. 1.] Guessed: A1A4L7VRD74WXT Actual: A1A4L7VRD74WXT Correct
[0.23673432 0.33813968 0.42512602] 2 [0. 0. 1.] Guessed: A1A4L7VRD74WXT Actual: A1A4L7VRD74WXT Correct
[0.0739742  0.04747758 0.87854815] 2 [0. 0. 1.] Guessed: A1A4L7VRD74WXT Actual: A1A4L7VRD74WXT Correct

Correct: 12 Incorrect: 4 Out of: 16

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
RESULTS FOR 35 AUTHORS (OVERSAMPLING)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Number of Authors: 35
Sampling: 3x normal size for training
Batch Size: 5
Epochs: 5
Training Set: The first 4 reviews from each author
Testing Set: The remaining reviews (reviews[4:]) for each author

Correct: 20 Incorrect: 219 Out of: 239

Too big to show full results here...