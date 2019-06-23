import sys
#要被放入的文件路径，只能添加同一个路径下的
zpath = [               
         "zLib\\fdebug",
         "zLib\\fdebug",
         "zLib\\fdebug",
        ]
def path_append():
    """
        这个文件用于添加项目同一文件夹下的路径
    """

    for p in zpath:
        sys.path.append(__file__.replace('main_path.py',p))
