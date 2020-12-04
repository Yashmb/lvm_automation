import os
import time
import sys

width = os.get_terminal_size().columns

welcome = (" LVM Automation ").center(width)

def head():
    os.system("clear")
    print("\n"*2)
    print((" ---------------- ").center(width))
    print(welcome)
    print((" ---------------- ").center(width))
    print("\n"*2)

head()

def index():
    print("""
    1. local system
    2. remote system
    q. quit
    \n
    """)
    global sys
    sys = (input("select : "))
    os.system("clear")
    head()

def main():
    print("""
    1. Physical Volume
    2. Volume Group
    3. Logical Volume
    4. Increase Volume
    5. Decrease Volume
    0. back
    \n
    """)

while True:
    index()
    
    if sys == ("1" and "2" and "3"):
        print("Select an option")
    elif sys == "1":
        while True:
            main()

            inp = int(input("select : "))
            os.system("clear")

            if inp == "":
                print("Select an option")
            elif inp == 1:
                while True:
                    head()
                
                    print("""
                    1. Drives Attached
                    2. File System
                    3. Physical Volume List
                    4. Physical Volume Create                
                    0. back
                    \n
                    """)
                    pv = int(input("select : "))

                    if pv == "":
                        print("Select an option")
                    elif pv == 1:
                        print("\n"*2)
                        print(os.system("fdisk -l"))
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif pv == 2:
                        print("\n"*2)
                        print(os.system("df -h -T"))
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif pv == 3:
                        print("\n"*2)
                        print(os.system("pvdisplay"))
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif pv == 4:
                        print("\n"*2)
                        os.system("fdisk -l")
                        print("\n"*2)
                        drive = input("Enter drive name : ")
                        print("\n"*2)
                        if drive == "":
                            print("Invalid")
                            cl = input("Press any key to continue")
                            if cl == "":
                                os.system("clear")
                                continue
                        else:
                            cmd = ("pvcreate {0}".format(drive))
                            os.system(cmd)
                            cl = input("Press any key to continue")
                            if cl == "":
                                os.system("clear")
                                continue
                    elif pv == 0:
                        break

                os.system("clear")
                head()

            elif inp == 2:
                while True:
                    head()
                
                    print("""
                    1. Physical Volumes List
                    2. File System
                    3. Volume Group List
                    4. Volume Group Create
                    0. back
                    \n
                    """)

                    vg = int(input("select : "))

                    if vg == "":
                        print("Select an option")
                    elif vg == 1:
                        print("\n"*2)
                        print(os.system("pvdisplay"))
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif vg == 2:
                        print("\n"*2)
                        print(os.system("df -h -T"))
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif vg == 3:
                        print("\n"*2)
                        print(os.system("vgdisplay")) 
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue                   
                    elif vg == 4:
                        print("\n"*2)
                        os.system("pvdisplay")
                        print("\n"*2)
                        drive = input("Enter physical volumes : ")
                        print("\n"*2)
                        os.system("vgdisplay")
                        print("\n"*2)
                        vgname = input("Enter VG name : ")
                        print("\n"*2)
                        if drive == "" or vgname == "":
                            print("Invalid")
                            cl = input("Press any key to continue")
                            if cl == "":
                                os.system("clear")
                                continue
                        else:
                            cmd = ("vgcreate {0} {1} ".format(drive, vgname))
                            os.system(cmd)
                            cl = input("Press any key to continue")
                            if cl == "":
                                os.system("clear")
                                continue
                    elif vg == 0:
                        break
                    
                os.system("clear")
                head()

            elif inp == 3:
                while True:
                    head()

                    print("""
                    1. Volume Group List
                    2. File System
                    3. Logical Volume List
                    4. Logical Volume Create
                    5. Mount/Unmount Logical Volume
                    0. back
                    \n
                    """)
                    lv = int(input("select : "))

                    if lv == "":
                        print("Select an option")
                    elif lv == 1:
                        print("\n"*2)
                        print(os.system("vgdisplay"))
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif lv == 2:
                        print("\n"*2)
                        print(os.system("df -h -T"))
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif lv == 3:
                        print("\n"*2)
                        print(os.system("lvdisplay"))
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif lv == 4:
                        print("\n"*2)
                        size = input("LV size : ")
                        lvname = input("Enter LV name : ")
                        print("\n"*2)
                        os.system("vgdisplay")
                        print("\n"*2)
                        vgname = input("Enter VG name: ")
                        mount = input("Enter mount point")
                        print("\n"*2)
                        if lvname == "" or size == "":
                            print("Invalid")
                            cl = input("Press any key to continue")
                            if cl == "":
                                os.system("clear")
                                continue
                        else:
                            cmd = ("lvcreate --size {0}G --name {1} {2}".format(size, lvname, vgname))
                            os.system(cmd)
                            cmd1 = ("mks.ext4 /dev/{0}/{1}".format(vgname, lvname))
                            os.system(cmd1)
                            cmd2 = ("mount {0}".format(mount))
                            cl = input("Press any key to continue")
                            if cl == "":
                                os.system("clear")
                                continue 
                    elif lv == 0:
                        break
            
                os.system("clear")
                head()
        
            elif inp == 4:
                while True:
                    head()

                    print("""
                    1. File System
                    2. Volume Group List
                    3. Logical Volume List
                    4. Extend Volume
                    \n
                    """)

                    ev = input("select : ")

                    if ev == "":
                        print("Select an option")
                    if ev == 1:
                        print("\n"*2)
                        print(os.system("df -h"))
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif ev == 2:
                        print("\n"*2)
                        print(os.system("vgdisplay"))
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif ev == 3:
                        print("\n"*2)
                        print(os.system("lvdisplay"))
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif ev == 4:
                        print("\n"*2)
                        size = input("Size (GB) : ")
                        drive = input("Enter drive/volume name : ")
                        cmd = ("lvextend --size +{0}G {1}.format(size, drive)")

            elif inp == 0:
                continue

        os.system("clear")
        head()


    elif sys == "2":
        ip = input("remote IP : ")
    
        while True:
            def main():
                print("""
                1. physical volume
                2. volume group
                3. logical volume
                0. back
                """)
            main()

            inp = int(input("select : "))

            if inp == 1:
                while True:
                    print("""
                    1. drives attached
                    2. file system
                    3. physical volume create
                    4. physical volume display
                    0. back
                    """)
                    pv = int(input("select : "))

                    if pv == 1:
                        print(os.system("fdisk -l"))
                    elif pv == 2:
                        print(os.system("df -h -T"))
                    elif pv == 3:
                        drive = input("Enter drive name : ")
                        if drive == "":
                            print("Invalid")
                        else:
                            cmd = ("pvcreate {0}".format(drive))
                            os.system(cmd)
                    elif pv == 4:
                        print(os.system("pvdisplay"))
                    elif pv == 0:
                        main()

            elif inp == 2:
                while True:
                    print("""
                    1. Physical Volumes List
                    2. file system
                    3. volume group create
                    4. volume group display
                    0. back
                    """)
                    vg = int(input("select : "))

                    if vg == 1:
                        print(os.system("pvdisplay"))
                    elif vg == 2:
                        print(os.system("df -h -T"))
                    elif vg == 3:
                        drive = input("Enter physical volumes : ")
                        vgname = input("Enter VG name : ")
                        if drive == "" or vgname == "":
                            print("Invalid")
                        else:
                            cmd = ("vgcreate {0} {1} ".format(drive, vgname))
                            os.system(cmd)
                    elif pv == 4:
                        print(os.system("vgdisplay"))
                    elif pv == 0:
                        main()

            elif inp == 3:
                while True:
                    print("""
                    1. Volume Group List
                    2. file system
                    3. logical volume create
                    4. logical volume display
                    0. back
                    """)
                    lv = int(input("select : "))

                    if lv == 1:
                        print(os.system("vgdisplay"))
                    elif lv == 2:
                        print(os.system("df -h -T"))
                    elif lv == 3:
                        size = input("LV size : ")
                        lvname = input("Enter LV name : ")
                        vgname = input("Enter VG name: ")
                        if lvname == "" or size == "":
                            print("Invalid")
                        else:
                            cmd = ("lvcreate --size {0}G --name {1} {2}".format(size, lvname, vgname))
                            os.system(cmd)
                    elif pv == 4:
                        print(os.system("pvdisplay"))
                    elif pv == 0:
                        main()

            elif inp == 0:
                index()

            print("Press Enter to Continue")
            cl = input()
            if cl == "":
                os.system("clear")
                head()

    elif sys == "q":
        print(("exiting.....").center(width))
        os.system("sleep 3")
        os.system("clear")
        exit()
