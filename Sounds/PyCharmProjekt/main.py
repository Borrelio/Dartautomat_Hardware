import os
import shutil

PathAlt = "../Caller 3 ALT"
PathNeu = "../Caller 3 NEU"
Endung = "wav"

for i in range(0,181):
    try:
        # File Kopieren in Ordner NEU
        shutil.copy(PathAlt+"/"+str(i)+"."+Endung, PathNeu+"/"+str(i)+"."+Endung)
        print("File kopiert: "+ str(i))

        OldFileName = os.path.join(PathNeu+"/", str(i)+"."+Endung)
        print("{0:04d}_CallerNumber_".format(i))
        Neu = "{0:04d}_CallerNumber_".format(i)
        NewFIleName = os.path.join(PathNeu+"/", Neu+str(i)+"."+Endung)


        os.rename(OldFileName, NewFIleName )
    except:
        pass
