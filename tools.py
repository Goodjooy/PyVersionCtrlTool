# -*- coding: utf-8 -*-
# @Author: FrozenString
# @Date:   2020-11-01 09:11:16
# @Last Modified by:   FrozenString
# @Last Modified time: 2020-11-01 09:46:25
from input_output import IOCtrl
import os
import functools
# git交互方法类


def cmd_info(cmd, io):
    infos = os.popen(cmd)

    for info in infos.readlines():
        io.info_out_put(info)


class GitCtrl(object):
    def __init__(self, ioCtrl, path, gitpath="git", reinit=False):
        """
        初始化git仓库
        """
        self.gitpath = gitpath
        self.path = ""
        if os.path.isabs(path):
            self.path = path
        else:
            self.path = os.path.abspath(path)

        if isinstance(ioCtrl, IOCtrl):
            self.io = ioCtrl
        else:
            self.io = IOCtrl()

        # 检查目标目录下是否有.git文件夹
        if os.path.exists(os.path.join(path, ".git")) and not reinit:
            pass
        else:
            # 新建仓库
            cmd = f"\"{gitpath}\" init \"{path}\""
            cmd_info(cmd, self.io)

    def add_files(self, filenames):
        target_files = functools.reduce(
            lambda x, y: f"{x} \"{os.path.abspath(y)}\"", filenames, "")
        cmd = f"\"{self.gitpath}\" add {target_files}"
        cmd_info(cmd, self.io)

    def commit(self, info):
        cmd = f"\"{self.gitpath}\" commit -m {info}"
        cmd_info(cmd, self.io)
