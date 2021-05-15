# 
# Example file for retrieving data from the internet
#

import urllib.request #provides classes and code needed for makiing HTTP requests

def main():
  # opens webpage and prints result code
  webUrl = urllib.request.urlopen("http://www.google.com")
  print("result code: " + str(webUrl.getcode()))

  # read data from the url and print it out
  data = webUrl.read()
  print(data)



if __name__ == "__main__":
  main()
