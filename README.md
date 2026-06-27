# 🔒 LSB Image Steganography and Steganalysis

⚙️TECHNICAL OVERVIEW:

This project implements a complete **Least Significant Bit (LSB) Image Steganography** system together with a **Steganalysis** module for detecting hidden information within digital images. The steganography component securely embeds textual messages inside lossless PNG images by modifying only the least significant bits of RGB pixel values, ensuring that the carrier image remains visually indistinguishable from the original while allowing accurate recovery of the hidden payload.

Complementing the embedding process, the steganalysis module provides forensic techniques for identifying the presence of hidden data. It performs **LSB Bit-Plane Extraction** to visualize the least significant bit layer and reveal suspicious patterns introduced during embedding. In addition, it performs **Histogram Analysis**, **Histogram Comparison**, and **Histogram Difference Visualization** to examine statistical variations between clean and stego images, demonstrating how hidden information can be detected without directly decoding the embedded message.

---

## 🚀 Project Workflow


                 Secret Message
                        │
                        ▼
              LSB Steganography
                        │
                        ▼
                  Stego Image
                        │
        ┌───────────────┴───────────────┐
        ▼                               ▼
 Message Recovery              LSB Steganalysis
                                        │
                ┌───────────────────────┴──────────────────────┐
                ▼                                              ▼
      LSB Bit-Plane Extraction                     Histogram Analysis


---

## ✨ Key Features

### Steganography

* Secure LSB-based message embedding
* Pixel-level RGB LSB manipulation
* Automatic payload length encoding
* Accurate message extraction
* Capacity validation to prevent overflow
* Lossless PNG image support

### Steganalysis

* LSB Bit-Plane Extraction
* Histogram Analysis
* Histogram Comparison
* Histogram Difference Visualization
* Detection of statistical artifacts caused by LSB embedding

---

## 🔄 Encoding Pipeline

1. Convert the secret message into UTF-8 bytes.
2. Generate a 32-bit payload length header.
3. Convert the payload into a binary bit stream.
4. Embed the bits into the least significant bits of RGB channels.
5. Save the modified image as a lossless PNG.

---

## 🔄 Decoding Pipeline

1. Read the least significant bits from RGB channels.
2. Recover the 32-bit payload length.
3. Extract the payload bits.
4. Reconstruct the original UTF-8 message.
5. Display the recovered message.

---

## 🔍 Steganalysis Pipeline

### Bit-Plane Extraction

1. Read the stego image.
2. Extract the least significant bit of every RGB channel.
3. Construct the 0th bit-plane.
4. Save the extracted bit-plane image for visual inspection.

### Histogram Analysis

1. Compute grayscale histograms of both images.
2. Compare the intensity distributions.
3. Generate histogram comparison plots.
4. Visualize histogram differences to identify statistical anomalies.

---

## 💻 Technologies Used

* Python
* Pillow
* NumPy
* Matplotlib

---

## 📂 Project Structure

```text
LSB-IMAGE-STEGANOGRAPHY-AND-STEGANALYSIS/
│
├── examples/
│   ├── input.png
│   ├── stego.png
│   └── bit_plane.png
│
├── screenshots/
│   ├── menu.png
│   ├── encode.png
│   ├── decode.png
│   ├── bit_plane.png
│   ├── histogram.png
│   └── histogram_difference.png
│
├── src/
│   ├── lsb.py
│   ├── lsb_steganalysis.py
│   └── main.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 Installation

```bash
pip install -r requirements.txt
```

---

## ▶ Usage

### Steganography

```bash
python src/lsb.py
```

### Steganalysis

```bash
python src/steganalysis_main.py
```

---

## 🎯 Applications

* Secure Information Hiding
* Digital Image Forensics
* Cybersecurity Education
* Digital Watermarking Research
* Image Processing
* Information Security Demonstrations
* Academic Research

