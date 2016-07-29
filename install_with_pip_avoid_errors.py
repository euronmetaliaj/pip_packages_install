import subprocess


def install_from_requirements(filename):
    lines = open(filename)
    for i in lines:
        try:
            subprocess.call(['pip', 'install', i])
        except:
            print "ERROR HAPPENED WITH :", i




#install_from_requirements("req.txt")
