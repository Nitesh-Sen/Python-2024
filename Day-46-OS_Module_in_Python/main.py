# import os, shutil
# mdir = "data"
# if(not os.path.exists(mdir)):
#     os.mkdir(mdir)
# else:
#     print(f"\"{mdir}\" directory is already exist and going to remove")
#     shutil.rmtree(mdir, ignore_errors=True)

# dir = "Day"
# for i in range(0, 100):
#     dir = (f"data/Day{i+1}")
#     if(not os.path.exists(dir)):
#         os.mkdir(dir)
#     else:
#         print(f"\"{dir}\" is already exist. So going to remove that.")
#         # os.rmdir(dir) # This will be remove all empty directory only.
#         shutil.rmtree(dir, ignore_errors=True) # This will be remove all directories recursively.
#################### END ############################



######## 2nd Progrom. which will first create and next time reove that all accordingly.
# import os, shutil
# mdir = "data"
# dir = "Day"
# for i in range(0,1):
#     if(not os.path.exists(mdir)):
#         os.mkdir(mdir)
#     else:
#         print(f"\"{mdir}\" directory is already exist and going to remove")
#         shutil.rmtree(mdir, ignore_errors=True)
#         break
#     for i in range(0, 100):
#         dir = (f"data/Day{i+1}")
#         if(not os.path.exists(dir)):
#             os.mkdir(dir)
#         else:
#             print(f"\"{dir}\" is already exist. So going to remove that.")
#             # os.rmdir(dir) # This will be remove all empty directory only.
#             shutil.rmtree(dir, ignore_errors=True) # This will be remove all directories recursively.
#################### END ############################


####################### 3rd Program. How to rename the directories. ############################
# import os
# if(not os.path.exists(f"data")):
#     os.mkdir("data")
# else: 
#     print("Already exist data dir")
# for i in range(0, 100):
#     subdir = (f"data/Day{i+1}")
#     # if (not os.path.exists(subdir)):
#     #     os.mkdir(subdir)
#     # else:
#     #     print(f"Already exist {subdir}")

#     newnamesubdir = (f"data/Tutorial{i+1}")
#     os.rename(subdir, newnamesubdir)
################ END ###########################


########### 4th Program to list directory and files ##################

import os
folders = os.listdir("data")
print(folders)

for fold in folders:
    print(fold)
    print(os.listdir(f"data/{fold}"))