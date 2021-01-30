import os, time

PATH = "/home/toufik/Downloads"
NR_SECONDS_DAY = 86400

def main():
    lijst = os.listdir(PATH)

    nowEpoch = time.time()
    yesterDayEpoch = nowEpoch - NR_SECONDS_DAY

    for el in lijst:
        creationTime = os.path.getctime( PATH + "/" + el)
        if( yesterDayEpoch > creationTime ):
            os.unlink( PATH + "/" + el )

main()
