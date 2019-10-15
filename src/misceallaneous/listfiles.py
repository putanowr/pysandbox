import os

if __name__ == '__main__':
    directory = os.getcwd()
    print('Directory:',directory)
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".py"): 
                print(os.path.join(directory, filename))
