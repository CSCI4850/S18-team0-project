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

[0.6593313  0.23679575 0.10387288] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.95129144 0.03295878 0.01574974] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.90335745 0.04353776 0.05310475] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.72952765 0.12847267 0.14199966] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.91043425 0.04722584 0.0423399 ] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.9326967  0.02972467 0.03757861] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.61186165 0.21743524 0.1707031 ] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.9288966  0.03659373 0.0345096 ] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.8815845  0.09037118 0.02804426] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.63951343 0.1707804  0.18970616] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.5790147  0.27759963 0.14338571] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.55676943 0.22658236 0.21664827] 0 [0. 1. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A2F1ZOWOPNJB Incorrect
[0.56875646 0.22814912 0.2030945 ] 0 [0. 1. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A2F1ZOWOPNJB Incorrect
[0.78797984 0.07613571 0.13588442] 0 [0. 0. 1.] Guessed: A1A1BM6N28X9J0 Actual: A1A4L7VRD74WXT Incorrect
[0.37912807 0.2444112  0.3764607 ] 0 [0. 0. 1.] Guessed: A1A1BM6N28X9J0 Actual: A1A4L7VRD74WXT Incorrect
[0.47348523 0.3089621  0.21755269] 0 [0. 0. 1.] Guessed: A1A1BM6N28X9J0 Actual: A1A4L7VRD74WXT Incorrect

Correct: 11 Incorrect: 5 Out of: 16

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

Correct: 15 Incorrect: 224 Out of: 239

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

[0.40979826 0.49859774 0.09160393] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.74281913 0.21619229 0.04098851] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.4760952 0.1083782 0.4155266] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.31033632 0.2342388  0.45542485] 2 [1. 0. 0.] Guessed: A1A4L7VRD74WXT Actual: A1A1BM6N28X9J0 Incorrect
[0.4397284  0.13159296 0.42867866] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.8437753  0.10876475 0.04745989] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.26880214 0.38816088 0.34303698] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.8099825  0.12660913 0.06340842] 0 [1. 0. 0.] Guessed: A1A1BM6N28X9J0 Actual: A1A1BM6N28X9J0 Correct
[0.3792133  0.4735567  0.14723004] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.18874434 0.29052755 0.52072805] 2 [1. 0. 0.] Guessed: A1A4L7VRD74WXT Actual: A1A1BM6N28X9J0 Incorrect
[0.22438775 0.5413595  0.23425277] 1 [1. 0. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A1BM6N28X9J0 Incorrect
[0.09481306 0.2581139  0.64707303] 2 [0. 1. 0.] Guessed: A1A4L7VRD74WXT Actual: A1A2F1ZOWOPNJB Incorrect
[0.16956758 0.42223054 0.40820184] 1 [0. 1. 0.] Guessed: A1A2F1ZOWOPNJB Actual: A1A2F1ZOWOPNJB Correct
[0.43821737 0.12238311 0.43939948] 2 [0. 0. 1.] Guessed: A1A4L7VRD74WXT Actual: A1A4L7VRD74WXT Correct
[0.01676595 0.06492093 0.9183131 ] 2 [0. 0. 1.] Guessed: A1A4L7VRD74WXT Actual: A1A4L7VRD74WXT Correct
[0.2589098  0.42245254 0.31863773] 1 [0. 0. 1.] Guessed: A1A2F1ZOWOPNJB Actual: A1A4L7VRD74WXT Incorrect

Correct: 8 Incorrect: 8 Out of: 16

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
RESULTS FOR 35 AUTHORS (OVERSAMPLING)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Number of Authors: 35
Sampling: 3x
Batch Size: 5
Epochs: 5
Training Set: The first 4 reviews from each author
Testing Set: The remaining reviews (reviews[4:]) for each author

Testing Phase Results:

Correct: 17 Incorrect: 222 Out of: 239