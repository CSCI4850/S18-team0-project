# Authorship Attribution with Document Encodings and Neural Networks

Need to write a decent paragraph of description about the project....

## Getting Started

This will help you get a copy of the project running on your own system.

### Prerequisites

This project was made using a Jupyter notebook. You must have Jupyter installed and running to run this project inside a Jupyter notebook as well. You can find help setting up Jupyter on [its install page](http://jupyter.org/install), as well as the prerequisites for it, most importantly Python. Note Jupyter can run on either versions 2.7 or 3.3+ of Python, but this project was written using Python 3.
Furthermore, it uses Keras running on the TensorFlow framework to construct and run neural networks.

A full list of Python packages used when developing this project can be found at [PACKAGES.md](PACKAGES.md). They should be installed in your Python environment using "pip install (package)".

### Installing

Once the prerequisites are installed, this project should not need any additional setup to run. Simply clone the project into a folder within an instance of Jupyter, and it should be ready to run.


## Preprocessing

* Sample Data is in the [data](data/) folder:  
 demo\_reviews.txt
* Each script in the scripts folder performs a variation of an encoding method tested.
* They can be run as:
  * ./customDoc2Vec.py inputfilename outputfilename
  * ./spacyDoc2Vec.py inputfilename outputfilename
  * ./gensimDoc2Vec.py inputfilename outputfilename modelname
* For example:
  * ./gensimDoc2Vec.py demo\_reviews.txt demo\_encoded.txt demoModel

* The resulting data file is utilized by the Final Network Jupyter Notebook.

## Running

1. Run Setup
2. Read in the Vectors and Generate One-Hot Encodings
   * Settings
   * Authors: 3
3. Separate Training/Testing Sets
4. Setup Optional Oversampling
5. Shuffle and Reshape
6. Choose Network
   * Networks
   * Network 1 (CNN with regularizers)
   * Network 2 (CNN)
   * Network 3 (Dense)
7. Start Training
   * Settings
   * Batch Size: 5
   * Epochs: 5
8. Reshape Testing Data
9. Start Testing
10. Show Graphs
11. Generate Predictions


## Built With

* [Jupyter](http://jupyter.org/documentation/) - The environment used
* [TensorFlow](https://www.tensorflow.org/) - Makes neural networks easy
* [Keras](https://keras.io/) - High level API for fast experimentation with networks built on TensorFlow

## Authors

* **Miles Baer** - *Initial work*
* **Robert Smith** - *Initial work*
* **Nathaniel Boyer** - *Administration and presentation*
* **William Cope** - *Some documentation and administrative assistance*
* **Charles Johnson** - *Research paper drafting*

See also the list of [contributors](https://github.com/CSCI4850/S18-team0-project/contributors) who participated in this project.

## License

This project is licensed under the MIT License.

## Acknowledgments

* [Convolutional Neural Networks for Authorship Attribution of Short Texts by Shrestha et al](http://www.aclweb.org/anthology/E17-2106) Much of the initial work was based on the work outlined there.
