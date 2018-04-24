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

[0.4651388  0.39292192 0.14193928] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.45747706 0.49210784 0.05041507] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.4619484  0.42666253 0.11138901] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.5038165  0.4361215  0.06006209] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.47462294 0.47912863 0.04624842] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.44543695 0.46842834 0.08613477] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.38507143 0.5314261  0.08350246] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.44266668 0.4641792  0.09315413] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.4942633  0.41951704 0.08621962] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.40468875 0.4803642  0.11494707] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.45187864 0.4118411  0.13628028] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.4261302  0.5312845  0.04258528] 1 [0. 1. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A2F1ZOWOPNJB Correct
[0.3845083  0.40009055 0.21540114] 1 [0. 1. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A2F1ZOWOPNJB Correct
[0.36265388 0.3742365  0.26310968] 1 [0. 0. 1.] Guessed: A1A2F1ZOWOPNJB Actual: A1A4L7VRD74WXT Incorrect
[0.355077   0.3760655  0.26885745] 1 [0. 0. 1.] Guessed: A1A2F1ZOWOPNJB Actual: A1A4L7VRD74WXT Incorrect
[0.3642233  0.36714417 0.26863262] 1 [0. 0. 1.] Guessed: A1A2F1ZOWOPNJB Actual: A1A4L7VRD74WXT Incorrect

Correct: 7 Incorrect: 9 Out of: 16

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

Correct: 12 Incorrect: 227 Out of: 239

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
RESULTS FOR 3 AUTHORS (OVERSAMPLING)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Number of Authors: 3
Sampling: 3x normal size for training
Batch Size: 5
Epochs: 5
Training Set: The first 4 reviews from each author
Testing Set: The remaining reviews (reviews[4:]) for each author

Testing Phase Results:

[0.34726775 0.3227823  0.32994995] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.37330195 0.3185686  0.30812946] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.34645855 0.32945475 0.32408673] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.38025454 0.30946198 0.31028354] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.3864661  0.32487068 0.28866324] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.35691175 0.3331463  0.30994195] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.33250794 0.33204743 0.3354447 ] 2 [1. 0. 0.] Guessed: A1A4L7VRD74WXT Actual: A1A1BM6N28X9J0 Incorrect
[0.35522437 0.32544112 0.31933445] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.3586827  0.31518704 0.32613033] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.33328083 0.33030954 0.3364097 ] 2 [1. 0. 0.] Guessed: A1A4L7VRD74WXT Actual: A1A1BM6N28X9J0 Incorrect
[0.3485191  0.31658077 0.33490005] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.3999107  0.33380434 0.26628497] 0 [0. 1. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A2F1ZOWOPNJB Incorrect
[0.33149192 0.33224586 0.3362622 ] 2 [0. 1. 0.] Guessed: A1A4L7VRD74WXT Actual: A1A2F1ZOWOPNJB Incorrect
[0.33215618 0.33205253 0.3357913 ] 2 [0. 0. 1.] Guessed: A1A4L7VRD74WXT Actual: A1A4L7VRD74WXT Correct
[0.33218518 0.3321513  0.3356636 ] 2 [0. 0. 1.] Guessed: A1A4L7VRD74WXT Actual: A1A4L7VRD74WXT Correct
[0.33227637 0.33188328 0.33584037] 2 [0. 0. 1.] Guessed: A1A4L7VRD74WXT Actual: A1A4L7VRD74WXT Correct

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

Testing Phase Results:

Correct: 18 Incorrect: 221 Out of: 239