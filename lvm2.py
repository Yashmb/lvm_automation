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
    try:
        sys = (input("select : "))
    except ValueError:
        print("Select an option")
    head()

def main():
    print("""
    1. Physical Volume
    2. Volume Group
    3. Logical Volume
    4. Increase/Decrease Volume
    0. back
    \n
    """)

while True:
    index()
 
    if sys == "1":
        while True:
            main()
            
            global inp

            try:
                inp = int(input("select : "))
            except ValueError:
                os.system("clear")
                head()
                print("Select an option")
                continue
            os.system("clear")

            if inp == 1:
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

                    try:
                        pv = int(input("select : "))
                    except ValueError:
                        os.system("clear")
                        head()
                        print("Select an option")
                        continue

                    if pv == 1:
                        print("\n"*2)
                        print(os.system("fdisk -l"))
                        print("\n"*2)
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif pv == 2:
                        print("\n"*2)
                        print(os.system("df -h -T"))
                        print("\n"*2)
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif pv == 3:
                        print("\n"*2)
                        print(os.system("pvdisplay"))
                        print("\n"*2)
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
                            print("\n"*2)
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

                    try:
                        vg = int(input("select : "))
                    except ValueError:
                        os.system("clear")
                        head()
                        print("Select an option")
                        continue

                    if vg == 1:
                        print("\n"*2)
                        print(os.system("pvdisplay"))
                        print("\n"*2)
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif vg == 2:
                        print("\n"*2)
                        print(os.system("df -h -T"))
                        print("\n"*2)
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif vg == 3:
                        print("\n"*2)
                        print(os.system("vgdisplay"))
                        print("\n"*2) 
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
                            print("\n"*2)
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

                    try:
                        lv = int(input("select : "))
                    except ValueError:
                        os.system("clear")
                        head()
                        print("Select an option")
                        continue

                    if lv == 1:
                        print("\n"*2)
                        print(os.system("vgdisplay"))
                        print("\n"*2)
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif lv == 2:
                        print("\n"*2)
                        print(os.system("df -h -T"))
                        print("\n"*2)
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif lv == 3:
                        print("\n"*2)
                        print(os.system("lvdisplay"))
                        print("\n"*2)
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
                            print("\n"*2)
                            cmd1 = ("mkfs.ext4 /dev/{0}/{1}".format(vgname, lvname))
                            os.system(cmd1)
                            print("\n"*2)
                            cmd2 = ("mount /dev/{0}/{1} {2}".format(vgname, lvname, mount))
                            os.system(cmd2)
                            print("\n"*2)
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
                    5. Reduce Volume
                    0. back
                    \n
                    """)

                    try:
                        ev = int(input("select : "))
                    except ValueError:
                        os.system("clear")
                        head()
                        print("Select an option")
                        continue

                    if ev == 1:
                        print("\n"*2)
                        print(os.system("df -h"))
                        print("\n"*2)
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif ev == 2:
                        print("\n"*2)
                        print(os.system("vgdisplay"))
                        print("\n"*2)
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif ev == 3:
                        print("\n"*2)
                        print(os.system("lvdisplay"))
                        print("\n"*2)
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif ev == 4:
                        print("\n"*2)
                        size = input("Size (GB) : ")
                        print("\n"*2)
                        os.system("df -h -T")
                        print("\n"*2)
                        drive = input("Enter drive/volume name : ")
                        print("\n"*2)
                        if drive == "" or size == "":
                            print("Invalid")
                            cl = input("Press any key to continue")
                            if cl == "":
                                os.system("clear")
                                continue
                        else:
                            cmd = ("lvextend --size +{0}G {1}".format(size, drive))
                            os.system(cmd)
                            print("\n"*2)
                            cmd1 = ("resize2fs {0}".format(drive))
                            os.system(cmd1)
                            print("\n"*2)
                            cl = input("Press any key to continue")
                            if cl == "":
                                os.system("clear")
                                continue
                    elif ev == 5:
                        print("\n"*2)
                        size = input("Size (GB) : ")
                        print("\n"*2)
                        os.system("df -h -T")
                        print("\n"*2)
                        drive = input("Enter drive/volume name : ")
                        print("\n"*2)
                        if lvname == "" or size == "":
                            print("Invalid")
                            cl = input("Press any key to continue")
                            if cl == "":
                                os.system("clear")
                                continue
                        else:
                            cmd = ("lvreduce --size -{0}G {1}".format(size, drive))
                            os.system(cmd)
                            print("\n"*2)
                            cmd1 = ("resize2fs {0}".format(drive))
                            os.system(cmd1)
                            print("\n"*2)
                            cl = input("Press any key to continue")
                            if cl == "":
                                os.system("clear")
                                continue 
                    elif lv == 0:
                        break


            elif inp == 0:
                break

        os.system("clear")
        head()



    elif sys == "2":

        # global ip
        # ip = input("remote IP : ")
        # os.system("clear")
        # head()

        while True:
            
            global ip

            print(("""Press "b" to go back""").center(width))
            print("\n"*2)
            ip = input("remote IP : ")
            
            if ip == "b":
                os.system("clear")
                head()
                break
            else:
                os.system("clear")
                head()

    
            main()

            global inp1

            try:
                inp1 = int(input("select : "))
            except ValueError:
                os.system("clear")
                head()
                print("Select an option")
                continue
            os.system("clear")

            if inp1 == 1:
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

                    try:
                        pv = int(input("select : "))
                    except ValueError:
                        os.system("clear")
                        head()
                        print("Select an option")
                        continue

                    if pv == 1:
                        print("\n"*2)
                        cmd = ("ssh root@{0} fdisk -l".format(ip))
                        os.system(cmd)
                        print("\n"*2)
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif pv == 2:
                        print("\n"*2)
                        cmd = ("ssh root@{0} df -h -T".format(ip))
                        os.system(cmd)
                        print("\n"*2)
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif pv == 3:
                        print("\n"*2)
                        cmd = ("ssh root@{0} pvdisplay".format(ip))
                        os.system(cmd)
                        print("\n"*2)
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif pv == 4:
                        print("\n"*2)
                        cmd = ("ssh root@{0} fdisk -l".format(ip))
                        os.system(cmd)
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
                            cmd1 = ("ssh root@{0} pvcreate {1}".format(ip, drive))
                            os.system(cmd1)
                            print("\n"*2)
                            cl = input("Press any key to continue")
                            if cl == "":
                                os.system("clear")
                                continue
                    elif pv == 0:
                        break

                os.system("clear")
                head()

            elif inp1 == 2:
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

                    try:
                        vg = int(input("select : "))
                    except ValueError:
                        os.system("clear")
                        head()
                        print("Select an option")
                        continue

                    if vg == 1:
                        print("\n"*2)
                        cmd = ("ssh root@{0} pvdisplay".format(ip))
                        os.system(cmd)
                        print("\n"*2)
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif vg == 2:
                        print("\n"*2)
                        cmd = ("ssh root@{0} df -h -T".format(ip))
                        os.system(cmd)
                        print("\n"*2)
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif vg == 3:
                        print("\n"*2)
                        cmd = ("ssh root@{0} vgdisplay".format(ip))
                        os.system(cmd)
                        print("\n"*2)
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue                   
                    elif vg == 4:
                        print("\n"*2)
                        cmd = ("ssh root@{0} pvdisplay".format(ip))
                        os.system(cmd)
                        print("\n"*2)
                        drive = input("Enter physical volumes : ")
                        print("\n"*2)
                        cmd1 = ("ssh root@{0} vgdisplay".format(ip))
                        os.system(cmd1)
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
                            cmd2 = ("ssh root@{0} vgcreate {1} {2} ".format(ip, drive, vgname))
                            os.system(cmd2)
                            print("\n"*2)
                            cl = input("Press any key to continue")
                            if cl == "":
                                os.system("clear")
                                continue
                    elif vg == 0:
                        break
                    
                os.system("clear")
                head()

            elif inp1 == 3:
                while True:
                    head()

                    print("""
                    1. Volume Group List
                    2. File System
                    3. Logical Volume List
                    4. Logical Volume Create
                    0. back
                    \n
                    """)

                    try:
                        lv = int(input("select : "))
                    except ValueError:
                        os.system("clear")
                        head()
                        print("Select an option")
                        continue

                    if lv == 1:
                        print("\n"*2)
                        cmd = ("ssh root@{0} vgdisplay".format(ip))
                        os.system(cmd)
                        print("\n"*2)
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif lv == 2:
                        print("\n"*2)
                        cmd = ("ssh root@{0} df -h -T".format(ip))
                        os.system(cmd)
                        print("\n"*2)
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif lv == 3:
                        print("\n"*2)
                        cmd = ("ssh root@{0} lvdisplay".format(ip))
                        os.system(cmd)
                        print("\n"*2)
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif lv == 4:
                        print("\n"*2)
                        size = input("LV size : ")
                        print("\n"*2)
                        cmd = ("ssh root@{0} lvdisplay".format(ip))
                        os.system(cmd)
                        print("\n"*2)
                        lvname = input("Enter LV name : ")
                        print("\n"*2)
                        cmd1 = ("ssh root@{0} vgdisplay".format(ip))
                        os.system(cmd1)
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
                            cmd2 = ("ssh root@{0} lvcreate --size {1}G --name {2} {3}".format(ip, size, lvname, vgname))
                            os.system(cmd2)
                            print("\n"*2)
                            cmd3 = ("ssh root@{0} mkfs.ext4 /dev/{1}/{2}".format(ip, vgname, lvname))
                            os.system(cmd3)
                            print("\n"*2)
                            cmd4 = ("ssh root@{0} mount /dev/{1}/{2} {3}".format(ip, vgname, lvname, mount))
                            os.system(cmd4)
                            print("\n"*2)
                            cl = input("Press any key to continue")
                            if cl == "":
                                os.system("clear")
                                continue 
                    elif lv == 0:
                        break
            
                os.system("clear")
                head()
        
            elif inp1 == 4:
                while True:
                    head()

                    print("""
                    1. File System
                    2. Volume Group List
                    3. Logical Volume List
                    4. Extend Volume
                    5. Reduce Volume
                    \n
                    """)

                    try:
                        ev = int(input("select : "))
                    except ValueError:
                        os.system("clear")
                        head()
                        print("Select an option")
                        continue

                    if ev == 1:
                        print("\n"*2)
                        cmd = ("ssh root@{0} df -h -T".format(ip))
                        os.system(cmd)
                        print("\n"*2)
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif ev == 2:
                        print("\n"*2)
                        cmd = ("ssh root@{0} vgdisplay".format(ip))
                        os.system(cmd)
                        print("\n"*2)
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif ev == 3:
                        print("\n"*2)
                        cmd = ("ssh root@{0} lvdisplay".format(ip))
                        os.system(cmd)
                        print("\n"*2)
                        cl = input("Press any key to continue")
                        if cl == "":
                            os.system("clear")
                            continue
                    elif ev == 4:
                        print("\n"*2)
                        size = input("Size (GB) : ")
                        print("\n"*2)
                        cmd = ("ssh root@{0} df -h -T".format(ip))
                        os.system(cmd)
                        print("\n"*2)
                        drive = input("Enter drive/volume name : ")
                        print("\n"*2)
                        if drive == "" or size == "":
                            print("Invalid")
                            cl = input("Press any key to continue")
                            if cl == "":
                                os.system("clear")
                                continue
                        else:
                            cmd1 = ("ssh root@{0} lvextend --size +{1}G {2}".format(ip, size, drive))
                            os.system(cmd1)
                            print("\n"*2)
                            cmd2 = ("ssh root@{0} resize2fs {1}".format(ip, drive))
                            os.system(cmd2)
                            print("\n"*2)
                            cl = input("Press any key to continue")
                            if cl == "":
                                os.system("clear")
                                continue
                    elif ev == 5:
                        print("\n"*2)
                        size = input("Size (GB) : ")
                        print("\n"*2)
                        cmd = ("ssh root@{0} df -h -T".format(ip))
                        os.system(cmd)
                        print("\n"*2)
                        drive = input("Enter drive/volume name : ")
                        if lvname == "" or size == "":
                            print("Invalid")
                            cl = input("Press any key to continue")
                            if cl == "":
                                os.system("clear")
                                continue
                        else:
                            cmd1 = ("ssh root@{0} lvreduce --size -{1}G {2}".format(ip, size, drive))
                            os.system(cmd1)
                            print("\n"*2)
                            cmd2 = ("ssh root@{0} resize2fs {1}".format(ip, drive))
                            os.system(cmd2)
                            print("\n"*2)
                            cl = input("Press any key to continue")
                            if cl == "":
                                os.system("clear")
                                continue


            elif inp1 == 0:
                break

        os.system("clear")
        head()

    elif sys == "q":
        print(("exiting.....").center(width))
        os.system("sleep 2")
        os.system("clear")
        exit()
