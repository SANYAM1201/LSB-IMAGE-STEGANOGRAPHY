from PIL import Image
import struct
import os


class LSBSteganography:

    @staticmethod
    def encode(input_image, output_image, secret_message):

        img = Image.open(input_image).convert("RGB")
        pixels = list(img.getdata())

        message_bytes = secret_message.encode("utf-8")

        # 4-byte length header
        length_header = struct.pack(">I", len(message_bytes))

        payload = length_header + message_bytes

        bit_stream = "".join(
            format(byte, "08b")
            for byte in payload
        )

        capacity = len(pixels) * 3

        if len(bit_stream) > capacity:
            raise ValueError(
                "Message too large for selected image."
            )

        bit_index = 0
        new_pixels = []

        for pixel in pixels:

            r, g, b = pixel
            channels = [r, g, b]

            for i in range(3):

                if bit_index < len(bit_stream):

                    channels[i] = (
                        channels[i] & 0xFE
                    ) | int(bit_stream[bit_index])

                    bit_index += 1

            new_pixels.append(tuple(channels))

        img.putdata(new_pixels)
        img.save(output_image, "PNG")

        print("\nMessage embedded successfully!")
        print("Output image:", output_image)

    @staticmethod
    def decode(stego_image):

        img = Image.open(stego_image).convert("RGB")
        pixels = list(img.getdata())

        bits = []

        for pixel in pixels:

            r, g, b = pixel

            bits.append(str(r & 1))
            bits.append(str(g & 1))
            bits.append(str(b & 1))

        bit_string = "".join(bits)

        header_bits = bit_string[:32]

        payload_length = struct.unpack(
            ">I",
            bytes(
                int(header_bits[i:i + 8], 2)
                for i in range(0, 32, 8)
            )
        )[0]

        payload_start = 32
        payload_end = payload_start + payload_length * 8

        payload_bits = bit_string[
            payload_start:payload_end
        ]

        message_bytes = bytes(
            int(payload_bits[i:i + 8], 2)
            for i in range(
                0,
                len(payload_bits),
                8
            )
        )

        return message_bytes.decode("utf-8")


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

PROJECT_ROOT = os.path.dirname(BASE_DIR)

INPUT_IMAGE = os.path.join(
    PROJECT_ROOT,
    "examples",
    "input.png"
)

STEGO_IMAGE = os.path.join(
    PROJECT_ROOT,
    "examples",
    "stego.png"
)


while True:

    print("\n===== LSB IMAGE STEGANOGRAPHY =====")
    print("1. Encode Message")
    print("2. Decode Message")
    print("3. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":

        secret = input(
            "\nEnter secret message: "
        )

        LSBSteganography.encode(
            INPUT_IMAGE,
            STEGO_IMAGE,
            secret
        )

    elif choice == "2":

        message = (
            LSBSteganography.decode(
                STEGO_IMAGE
            )
        )

        print(
            "\nRecovered Message:",
            message
        )

    elif choice == "3":

        print("Exiting...")
        break

    else:

        print("Invalid choice.")