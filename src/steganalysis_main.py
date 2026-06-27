import os
from lsb_steganalysis import LSBSteganalysis


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

CLEAN_IMAGE = os.path.join(
    PROJECT_ROOT,
    "examples",
    "input.png"
)

STEGO_IMAGE = os.path.join(
    PROJECT_ROOT,
    "examples",
    "stego.png"
)

BIT_PLANE_IMAGE = os.path.join(
    PROJECT_ROOT,
    "examples",
    "bit_plane.png"
)



def print_menu():

    print("\n" + "=" * 45)
    print("      LSB IMAGE STEGANALYSIS")
    print("=" * 45)
    print("1. Extract LSB Bit-Plane")
    print("2. Histogram Analysis")
    print("3. Complete Analysis")
    print("4. Exit")
    print("=" * 45)



while True:

    print_menu()

    choice = input("Enter your choice (1-4): ").strip()


    if choice == "4":

        print("\nThank you for using the program.")

        break


    if not os.path.exists(STEGO_IMAGE):

        print("\n[ERROR]")
        print("stego.png not found.")
        print("Please run lsb.py first and encode a message.\n")

        input("Press Enter to continue...")
        continue


    if choice == "1":

        print("\nExtracting LSB Bit-Plane...\n")

        LSBSteganalysis.extract_bit_plane(
            STEGO_IMAGE,
            BIT_PLANE_IMAGE
        )

        input("\nPress Enter to continue...")

    
    elif choice == "2":

        print("\nPerforming Histogram Analysis...\n")

        LSBSteganalysis.compare_histograms(
            CLEAN_IMAGE,
            STEGO_IMAGE
        )

        input("\nPress Enter to continue...")

    
    elif choice == "3":

        print("\nRunning Complete Analysis...\n")

        LSBSteganalysis.run_complete_analysis(
            CLEAN_IMAGE,
            STEGO_IMAGE,
            BIT_PLANE_IMAGE
        )

        input("\nPress Enter to continue...")

    

    else:

        print("\nInvalid choice. Please enter a number between 1 and 4.")

        input("\nPress Enter to continue...")