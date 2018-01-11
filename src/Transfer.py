#!/usr/bin/env python

import os

import sys
import time
import Type
import Creator

"""  将dimens.xml文件解析，根据用户设置的 density  cale_density  xdpi 比例创建转换后的xml（默认比例：1 1 160）  """


class Transfer:
    def __init__(self, density, scale_density, xdpi, file_path):
        if density:
            self.density = density
        else:
            self.density = 1

        if scale_density:
            self.scale_density = scale_density
        else:
            self.scale_density = 1

        if xdpi:
            self.xdpi = xdpi
        else:
            self.xdpi = 160

        if file_path:
            self.file_path = file_path
        else:
            self.file_path = None

    def parse_xml(self, path, creator):
        """"  解析xml文件，每一个节点生成一个字典，并存储到列表中  """
        node_list = []
        if path:
            data = creator.parse_file(path)
            element = data.getElementsByTagName(Type.dimen)
            for node in element:
                node_list.append({str(node.getAttribute(Type.name)): str(node.firstChild.data)})
            return node_list

    def generator(self, function_output):
        if self.density and self.scale_density and self.xdpi and self.file_path:
            function_output('>> Start to parse parameters...')
            original_file_path, file_name = os.path.split(self.file_path)
            creator = Creator.Creator(self.density, self.scale_density, self.xdpi)
            function_output('>> Loading the xml file : %s ' % original_file_path)

            # 解析xml文件
            node_list = self.parse_xml(self.file_path, creator)
            function_output('>> File read successfully..')

            # 生成xml格式数据
            function_output('>> Start to generate the target xml data...')
            creator.creat_xml(node_list, function_output)
            # 开始写xml文档
            # 创建本次操作的单独目录
            function_output('>> Start to generate the target xml file...')
            internal_write_path = original_file_path + self.local_time()
            if not os.path.exists(internal_write_path):
                os.mkdir(internal_write_path)
            internal_write_file_name = internal_write_path + '\dimens.xml'
            # 打开文件并
            function_output('>> Start to write data to target xml file...')
            with open(internal_write_file_name, 'w') as fp:
                # 写入数据
                creator.writexml(fp)
                function_output('>> Write successfully...')
                function_output('>> Target File Path: %s ' % internal_write_file_name)

            # 删除本次创建的文件（需要在用户下载完成后删除源文件）
            # shutil.rmtree(wirte_file_name)
            del node_list
        else:
            function_output('>> Please enter the correct information.')

    def output_info(self, info):
        print(info)

    def local_time(self):
        return time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))


if __name__ == '__main__':
    if len(sys.argv) >= 5:
        print('>>start to parse parameters...')
        density = float(sys.argv[1])
        scale_density = float(sys.argv[2])
        xdpi = float(sys.argv[3])
        file_path, file_name = os.path.split(sys.argv[4])
        transfer = Transfer(density, scale_density, xdpi, sys.argv[4])
        creator = Creator.Creator(density, scale_density, xdpi)
        print('>>loading the xml file...')
        # 解析xml文件
        node_list = transfer.parse_xml(sys.argv[4], creator)
        print('>>file parsing successfully..')
        print('>>start to convert the data...')
        print('>>start to generate the target xml...')
        # 生成xml格式数据
        creator.creat_xml(node_list, transfer.output_info)
        # 开始写xml文档
        # 创建本次操作的单独目录
        write_path = file_path + transfer.local_time()
        if not os.path.exists(write_path):
            os.mkdir(write_path)
        wirte_file_name = write_path + transfer.write_file_path()
        # 打开文件并
        # print('>>writting data to the target xml file...')
        print('>>start to write data to xml file...')
        fp = open(wirte_file_name, 'w')
        # 写入数据
        creator.writexml(fp)
        # 关闭文件操作
        fp.close()
        print('>>write successfully...')
        print('>>Path: % s ' % wirte_file_name)
        # 删除本次创建的文件（需要在用户下载完成后删除源文件）
        # shutil.rmtree(wirte_file_name)
        del node_list
    else:
        print('>>please enter the correct information.')
