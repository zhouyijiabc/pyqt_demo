'''
Author: xzhouinfo
Date: 2022-01-26 01:27:46
LastEditors: xzhouinfo
LastEditTime: 2022-01-26 01:16:16
Description: 表格操作
'''
import pandas as pd
import os
from pathlib import Path


class TableHandle:
    def __init__(self, file_path, save_name, marge_col=None):
        self.save_name = save_name
        self.file_path = file_path
        if os.path.isfile(file_path):
            self.df = pd.read_excel(file_path)
            self.columns = self.df.columns
            print(self.columns)
        else:
            self.df = None

    def marge_table(self, is_sort=False, sort_key=None):
        """
        合并表格
        :param is_sort: 是否排序，默认不排序
        :param sort_key: 排序列
        :return: None
        """
        if os.path.isdir(self.file_path):
            excel_files = Path(self.file_path)
            excel_files = excel_files.glob('*.xlsx')
            print(excel_files)
            all_df = []
            for file in excel_files:
                df = pd.read_excel(file)
                all_df.append(df)
            df = pd.concat(all_df)
            if is_sort and sort_key is not None:
                df = df.sort_values(by=sort_key, ascending=False)
            print(df)
            df.to_excel(self.save_name, index=False)
        else:
            print('文件路径错误')

    def top_to_sheet(self, top_num=10):
        """:top_num: 提取top10 出来
        """
        pass

if __name__ == '__main__':
    file_path = r'J:\PythonProject\python_demo\测试库demo'
    save_name = 'marge1.xlsx'
    a = TableHandle(file_path=file_path, save_name=save_name)
    a.marge_table(is_sort=True, sort_key='birthdate')
    # a