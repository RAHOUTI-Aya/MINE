7.  Features extraction model benchmarking:
===========

   CNN Conv2D relies on convolutional layers to capture local spatial patterns in DNA sequences, while DNAbert leverages a transformer-based architecture, pre-trained specifically on genomic data, to detect complex patterns and long-range dependencies.
DNA sequences for the CNN Conv2D model were one-hot encoded and reshaped for compatibility with the Conv2D layers, while DNAbert utilized k-mer tokenization to generate embeddings. Benchmarking results showed that DNAbert consistently outperformed CNN Conv2D across key metrics.
