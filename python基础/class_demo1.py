class PageView:
    def __init__(self, all_data_list, input_page, view_page_num=10):
        """
        data_list: 总数据
        page: 当前要查看的页面
        per_page_num: 每页默认显示数据行数
        """
        self.data_list = all_data_list
        self.page = input_page
        self.per_page_num = view_page_num

    @property
    def start(self):
        return (self.page-1)*self.per_page_num

    @property
    def end(self):
        return self.page*self.per_page_num

    def show(self):
        result = self.data_list[self.start:self.end]
        for row in result:
            print(row)


data_list = ['alex-'+str(i) for i in range(1, 901)]
while True:

    page = int(input('page'))
    per_page_num = 10
    obj = PageView(data_list, page)
    obj.show()
