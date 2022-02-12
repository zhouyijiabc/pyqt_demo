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
            print('file path is worry')

    def top_to_sheet(self, top_num=10):
        pass


if __name__ == '__main__':
    pass