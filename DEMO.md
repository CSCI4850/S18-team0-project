### Running a Quick Demo

So, you've got a everything installed and you want to see if it all works. Or maybe you just want a quick and dirty demonstration to see how one of these networks run.

The demo folder contains everything you need for a quick run.
Demo network.ipynb: A simple convolutional network implementation that uses all the same packages and resources as the full networks in the project.
demo\_input.dat: Some pre-prepared data to use as input for the network.

To test the demo network, first open demo/Demo network.ipynb.
Everything should be ready to run. You can either step through the run gradually with the Play button (in the current version of Jupyter as of this writing), or if you want to just run it all at once, use Run All under the Run menu.

The cells are as follows:
1. Loads all of the necessary packages.
2. Reads in the input data. Notice for the purposes of this demo we are only using 8 data points, although each data point is a vector 300 in size.
3. Constructs the convolutional network. Notice that the network contains more than 50 million parameters. This would seem like a fairly large network for using with only 8 data points, but this network is based on the full networks used in this project meant for much larger data sets.
4. Runs the network. For the sake of expediency, it is set to only run for 50 epochs. A basic demo shouldn't take more than a few minutes, after all. Feel free to experiment with larger numbers if you wish.
5. Prints out graphs showing the change in loss and accuracy over time. For the sake of this demo, in theory, loss should show as dropping quickly early on, then holding fairly steady with little change from then on. Accuracy should show the opposite. However, there is some element of chance in this, so your results may look very different.
6. Prints out the final loss and accuracy. Don't worry if these come out looking bad. If you've gotten this far at all, everything is working.
