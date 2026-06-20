
# LSB Image Steganography



This project implements a robust image steganography system that enables secure embedding of textual information within digital images using Least Significant Bit (LSB) manipulation. The solution preserves the visual integrity of the carrier image while allowing exact reconstruction of the hidden payload.



Unlike conventional text storage methods, the hidden message is encoded directly into the pixel matrix of a lossless PNG image, making the embedded information imperceptible to the human eye. A dedicated extraction mechanism reconstructs the original payload with 100% accuracy through bit-level decoding.



## Key Features



* Lossless PNG-based steganography

* Pixel-level LSB encoding and decoding

* Exact payload recovery using a binary length header

* UTF-8 text support

* Capacity validation to prevent overflow

* Portable Python implementation using Pillow

* User-friendly command-line interface



## Technical Overview



The system leverages the Least Significant Bit of RGB pixel channels to store message data. A 32-bit header containing the payload length is embedded before the actual message, enabling deterministic extraction without requiring external metadata.



### Encoding Pipeline



1. Convert the secret message into UTF-8 bytes.

2. Generate a 32-bit payload length header.

3. Transform the payload into a binary bit stream.

4. Embed bits into the least significant bits of RGB channels.

5. Save the modified image as a lossless PNG.



### Decoding Pipeline



1. Read the LSBs from RGB channels.

2. Extract the 32-bit payload length header.

3. Recover the payload bits.

4. Reconstruct the original UTF-8 message.

5. Display the decoded text.



## Applications



* Secure information concealment

* Digital watermarking research

* Information security education

* Steganography demonstrations

* Image processing experiments

* Cybersecurity learning projects



Installation

pip install -r requirements.txt



Run

python project.py



Menu

1. Encode Message
2. Decode Message
3. Exit


