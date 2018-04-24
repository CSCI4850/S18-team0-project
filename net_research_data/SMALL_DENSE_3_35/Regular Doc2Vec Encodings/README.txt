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

[0.6967577  0.25450888 0.04873339] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.60740894 0.38322026 0.00937081] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.7727145  0.20644398 0.02084148] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.6575206  0.3240183  0.01846117] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.5216524  0.46661386 0.01173378] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.5536504  0.42456606 0.02178355] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.46869394 0.5175874  0.01371858] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.5687774  0.40640828 0.02481436] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.70534563 0.2721045  0.02254987] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.6201411  0.3526678  0.02719113] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.7052017  0.25319877 0.04159959] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.5047253  0.4846768  0.01059791] 0 [0. 1. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A2F1ZOWOPNJB Incorrect
[0.47360492 0.42949712 0.09689787] 0 [0. 1. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A2F1ZOWOPNJB Incorrect
[0.48034033 0.39435846 0.12530127] 0 [0. 0. 1.] Guessed: A1A1BM6N28X9J0 Actual: A1A4L7VRD74WXT Incorrect
[0.47928023 0.41659984 0.10411996] 0 [0. 0. 1.] Guessed: A1A1BM6N28X9J0 Actual: A1A4L7VRD74WXT Incorrect
[0.47630352 0.37089297 0.1528035 ] 0 [0. 0. 1.] Guessed: A1A1BM6N28X9J0 Actual: A1A4L7VRD74WXT Incorrect

Correct: 10 Incorrect: 6 Out of: 16

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
RESULTS FOR 35 AUTHORS
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Number of Authors: 3
Sampling: Normal
Batch Size: 5
Epochs: 5
Training Set: The first 4 reviews from each author
Testing Set: The remaining reviews (reviews[4:]) for each author

Testing Phase Results:

Correct: 32 Incorrect: 207 Out of: 239

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
RESULTS FOR 3 AUTHORS (OVERSAMPLING)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Number of Authors: 3
Sampling: 3x normal size for training data
Batch Size: 5
Epochs: 5
Training Set: The first 4 reviews from each author
Testing Set: The remaining reviews (reviews[4:]) for each author

Testing Phase Results:

[0.28536522 0.24005759 0.47457716] 2 [1. 0. 0.] Guessed: A1A4L7VRD74WXT Actual: A1A1BM6N28X9J0 Incorrect
[0.17967086 0.7286671  0.09166209] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.5052133  0.2813187  0.21346806] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.09961164 0.40099135 0.49939698] 2 [1. 0. 0.] Guessed: A1A4L7VRD74WXT Actual: A1A1BM6N28X9J0 Incorrect
[0.08535875 0.8136564  0.1009848 ] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.10929857 0.5112216  0.37947994] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.04275159 0.65835017 0.29889825] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.17574885 0.5998487  0.22440249] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.22184932 0.21028878 0.5678619 ] 2 [1. 0. 0.] Guessed: A1A4L7VRD74WXT Actual: A1A1BM6N28X9J0 Incorrect
[0.13987496 0.33018082 0.5299442 ] 2 [1. 0. 0.] Guessed: A1A4L7VRD74WXT Actual: A1A1BM6N28X9J0 Incorrect
[0.40048444 0.2782765  0.321239  ] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.07640618 0.8497769  0.07381681] 1 [0. 1. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A2F1ZOWOPNJB Correct
[0.08667233 0.47383645 0.4394912 ] 1 [0. 1. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A2F1ZOWOPNJB Correct
[0.12320344 0.36211923 0.51467735] 2 [0. 0. 1.] Guessed: A1A4L7VRD74WXT Actual: A1A4L7VRD74WXT Correct
[0.16737778 0.38820162 0.44442052] 2 [0. 0. 1.] Guessed: A1A4L7VRD74WXT Actual: A1A4L7VRD74WXT Correct
[0.06205153 0.1712867  0.7666618 ] 2 [0. 0. 1.] Guessed: A1A4L7VRD74WXT Actual: A1A4L7VRD74WXT Correct

Correct: 7 Incorrect: 9 Out of: 16

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
RESULTS FOR 35 AUTHORS (OVERSAMPLING)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Number of Authors: 3
Sampling: 3x normal size for training data
Batch Size: 5
Epochs: 5
Training Set: The first 4 reviews from each author
Testing Set: The remaining reviews (reviews[4:]) for each author

Testing Phase Results:

Correct: 22 Incorrect: 217 Out of: 239