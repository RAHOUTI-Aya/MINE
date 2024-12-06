6. Data labeling : 
===========

6.1  CAG count:
----------

To be able to label each DNA sequence, it is necessary to link the DNA sequences to the number of repeated CAG nucleotide triplets.

6.2  Labeling:
----------

 Labeling the sequences based on the number of CAG repeats:

- CAGcount < = 35: Normal

- 36 < = CAGcount < = 39: Intermediate

- 40 < = CAGcount < = 55: Reduced_Penetrance

- Sinon: Full_Mutation

.. code-block:: python

    def calculate_cag_repeats(sequence):
    """Calculating the number of CAG repeats in a DNA sequence"""

    repeats = re.findall(r'(CAG)', sequence)
    repeat_count = len(repeats)
    return repeat_count

    def label_sequence(repeat_count):
    """Labeling the sequence based on the number of CAG repeats"""
      if repeat_count <= 35:
        return 'Normal'
      elif 36 <= repeat_count <= 39:
        return 'Intermediate'
      elif 40 <= repeat_count <= 55:
        return 'Reduced_Penetrance'
      else:
        return 'Full_Mutation'



