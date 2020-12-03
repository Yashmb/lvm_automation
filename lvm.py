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

index()

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

if sys == "1":
    while True:
        main()

        inp = int(input("select : "))
        os.system("clear")


        if inp == 1:
            while True:
                head()
                
                print("""
                1. drives attached
                2. file system
                3. physical volume display
                4. physical volume create                
                0. back
                \n
                """)
                pv = int(input("select : "))

                if pv == 1:
                    print("\n"*2)
                    print(os.system("fdisk -l"))
                    cl = input("Press any key to continue")
                    if cl == "":
                        os.system("clear")
                        continue
                elif pv == 2:
                    print(os.system("df -h -T"))
                    cl = input("Press any key to continue")
                    if cl == "":
                        os.system("clear")
                        continue
                elif pv == 3:
                    print(os.system("pvdisplay"))
                    cl = input("Press any key to continue")
                    if cl == "":
                        os.system("clear")
                        continue
                elif pv == 4:
                    drive = input("Enter drive name : ")
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
                2. file system
                3. volume group display
                4. volume group create
                0. back
                \n
                """)

                vg = int(input("select : "))

                if vg == 1:
                    print(os.system("pvdisplay"))
                    cl = input("Press any key to continue")
                    if cl == "":
                        os.system("clear")
                        continue
                elif vg == 2:
                    print(os.system("df -h -T"))
                    cl = input("Press any key to continue")
                    if cl == "":
                        os.system("clear")
                        continue
                elif vg == 3:
                    print(os.system("vgdisplay")) 
                    cl = input("Press any key to continue")
                    if cl == "":
                        os.system("clear")
                        continue                   
                elif vg == 4:
                    drive = input("Enter physical volumes : ")
                    vgname = input("Enter VG name : ")
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
                3. Logical Volume Display
                4. Logical Volume Create
                5. Mount/Unmount Logical Volume
                0. back
                \n
                """)
                lv = int(input("select : "))

                if lv == 1:
                    print(os.system("vgdisplay"))
                    cl = input("Press any key to continue")
                    if cl == "":
                        os.system("clear")
                        continue
                elif lv == 2:
                    print(os.system("df -h -T"))
                    cl = input("Press any key to continue")
                    if cl == "":
                        os.system("clear")
                        continue
                elif lv == 3:
                    print(os.system("pvdisplay"))
                    cl = input("Press any key to continue")
                    if cl == "":
                        os.system("clear")
                        continue
                elif lv == 4:
                    size = input("LV size : ")
                    lvname = input("Enter LV name : ")
                    vgname = input("Enter VG name: ")
                    mount = input("Enter mount point")
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

        elif inp == 0:
            break

    os.system("clear")
    head()
    index()



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
