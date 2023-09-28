import os, argparse
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def encryptFiles(folder="."):
	thisFile = os.path.basename(__file__)

	for root, dirs, files in os.walk(folder):

		for filename in files:
			if filename.endswith(".py") and filename != thisFile:
				theFile = os.path.join(root, filename)
				print(f"[#] Processing {theFile}...")

				with open(theFile, "r", encoding="utf=8") as file:
					encrypted = cipher.encrypt(file.read().encode("utf-8"))

				with open(theFile, "w", encoding="utf=8") as file:
					file.write("from cryptography.fernet import Fernet\n")
					file.write(f"\n")
					file.write(f"key = {key}\n")
					file.write(f"cipher = Fernet(key)\n")
					file.write(f"encrypted = {encrypted}\n")
					file.write(f"\n")
					file.write(f"exec(cipher.decrypt(encrypted).decode(\"utf-8\"))\n")
					file.write(f"\n")

	print("[#] Finished!")

def main():
	parser = argparse.ArgumentParser(description="   ____  __    ____           ____       \n  / __ \\/ /_  / __/_  _______/ __ \\__  __\n / / / / __ \\/ /_/ / / / ___/ /_/ / / / /\n/ /_/ / /_/ / __/ /_/ (__  ) ____/ /_/ / \n\\____/_.___/_/  \\__,_/____/_/    \\__, /  \n                                /____/   \n\n[Obfuspy] Python script to encrypt other scripts\n[https://github.com/samuelchristlie/ObfusPy]\n\n", formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument("-i", help="Folder to be encrypted.\nIf none given, current folder will be used", default=".")

	args = parser.parse_args()

	encryptFiles(args.i)
	
if __name__ == "__main__":
	main()


			





# cipher.encrypt()
# exec(cipher.decrypt())