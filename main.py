print("Choose a program to run:")
print("1. Website Vulnerability Scanner")
print("2. Image Steganography")
print("3. Dictionary Attack")

choice = input("Enter your choice (1-3): ")

if choice == "1":
    exec(open("webvulnscanner/WebVulnScanner.py").read())
elif choice == "2":
    exec(open("steganography/steganography.py").read())
elif choice == "3":
    exec(open("seltool/dict.py").read())
else:
    print("Invalid choice!")
