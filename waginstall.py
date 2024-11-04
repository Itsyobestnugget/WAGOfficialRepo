import os


def depinstall():
  print("Are you sure you want to install the dependencies?\n\n this will install:\nColorama\ngoogle-generativeai" )
  i = input("y/n: ")
  if i == "y":
    os.system("pip install google-generativeai")
    os.system("pip install colorama")
  if i == "n":
    print("prompt terminated")
def depupdate():
  print("Are you sure you want to update the dependencies?:\n\nColorama\ngoogle-generativeai" )
  i = input("y/n: ")
  if i == "y":
    os.system("pip install --upgrade google-generativeai")
    os.system("pip install --upgrade colorama")
  if i == "n":
    print("prompt terminated")
def uninstall():
  print("are you sure you want to uninstall?")
  i = input("y/n: ")
  if i == "y":
    os.system("pip uninstall colorama")
    os.system("pip uninstall google-generativeai")
    os.remove("WAGpreview.py")
    os.remove("WAGfull.py")
    os.remove("WAGit.py")
    os.remove("WAGdev.py")
    os.remove("WAGpremium.py")
    os.remove("waginstall.py")
print("Imported waginstall")