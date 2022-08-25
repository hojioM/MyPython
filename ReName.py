import os

target = ["【cychd.top】", "【次元虫洞chdchd.cc】", "【次元虫洞cychdacg.cc】", "【chdchd.cc】", "【cychdacg.cc】","【次元虫洞cychd.com】"]
file_path = "E:\OneDrive\OneDrive - hojom\福利姬"


def FileReName(path):
    FilePath = os.listdir(path)
    for i in FilePath:
        old_file_path = path + "\\" + i
        if os.path.isdir(old_file_path):
            FileReName(old_file_path)
        for j in target:
            if i.find(j) != -1:
                string = i.replace(j, "")
                new_file_path = path + "\\" + string
                os.rename(old_file_path, new_file_path)
                break
    return


# files = os.listdir(file_path)
# for i in files:
#     print(file_path+"\\"+i)
#     FileReName(file_path+"\\"+i)
FileReName("E:\OneDrive\OneDrive - hojom\Coser\桜桃喵")
