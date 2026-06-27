from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


class LSBSteganalysis:

    @staticmethod
    def extract_bit_plane(input_image, output_image):
        """
        Extract the Least Significant Bit (0th Bit Plane)
        and save it as a grayscale image.
        """

        try:
            img = Image.open(input_image).convert("RGB")
        except FileNotFoundError:
            print("\n[ERROR] Image not found.")
            return

        width, height = img.size

        bit_plane = Image.new("L", (width, height))

        pixels = img.load()
        output = bit_plane.load()

        for y in range(height):
            for x in range(width):

                r, g, b = pixels[x, y]

                # Number of RGB channels whose LSB is 1
                value = ((r & 1) + (g & 1) + (b & 1)) * 85

                output[x, y] = value

        bit_plane.save(output_image)

        print("\n✓ Bit-plane extracted successfully.")
        print(f"Saved as: {output_image}")

        plt.figure(figsize=(6, 6))
        plt.imshow(bit_plane, cmap="gray")
        plt.title("Extracted LSB Bit Plane")
        plt.axis("off")
        plt.show()

    @staticmethod
    def compare_histograms(clean_image, stego_image):
        """
        Compare histogram of clean and stego images.
        """

        try:
            clean = Image.open(clean_image).convert("L")
            stego = Image.open(stego_image).convert("L")

        except FileNotFoundError:
            print("\n[ERROR] Image not found.")
            return

        clean_pixels = np.array(clean).flatten()
        stego_pixels = np.array(stego).flatten()

        hist_clean, _ = np.histogram(
            clean_pixels,
            bins=256,
            range=(0, 256)
        )

        hist_stego, _ = np.histogram(
            stego_pixels,
            bins=256,
            range=(0, 256)
        )

        x = np.arange(256)
        width = 0.4

        plt.figure(figsize=(14, 8))

        # -------------------------------
        # Clean Histogram
        # -------------------------------
        plt.subplot(2, 2, 1)

        plt.bar(
            x,
            hist_clean,
            color="blue"
        )

        plt.title("Clean Image Histogram")
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Pixel Count")
        plt.grid(True)

        # -------------------------------
        # Stego Histogram
        # -------------------------------
        plt.subplot(2, 2, 2)

        plt.bar(
            x,
            hist_stego,
            color="red"
        )

        plt.title("Stego Image Histogram")
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Pixel Count")
        plt.grid(True)

        # -------------------------------
        # Side-by-side Comparison
        # -------------------------------
        plt.subplot(2, 1, 2)

        plt.bar(
            x - width / 2,
            hist_clean,
            width,
            color="blue",
            label="Clean"
        )

        plt.bar(
            x + width / 2,
            hist_stego,
            width,
            color="red",
            label="Stego"
        )

        plt.title("Histogram Comparison")
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Pixel Count")
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.show()

        # -------------------------------
        # Histogram Difference
        # -------------------------------

        difference = hist_stego - hist_clean

        plt.figure(figsize=(12, 4))

        plt.bar(
            x,
            difference,
            color="green"
        )

        plt.title("Histogram Difference (Stego - Clean)")
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Difference")
        plt.grid(True)

        plt.show()

        print("\n✓ Histogram analysis completed.")

    @staticmethod
    def run_complete_analysis(
        clean_image,
        stego_image,
        bit_plane_output
    ):
        """
        Run complete steganalysis.
        """

        print("\nRunning Complete Analysis...\n")

        LSBSteganalysis.extract_bit_plane(
            stego_image,
            bit_plane_output
        )

        LSBSteganalysis.compare_histograms(
            clean_image,
            stego_image
        )

        print("\n✓ Complete Steganalysis Finished Successfully.")