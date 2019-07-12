# -*- coding:utf-8 -*-

class Pagination(object):
    # 封装分页相关数据
    def __init__(self, current_page, record_count, page_record_limit, page_count_limit,searchtitle=''):
        """
        :param page_count:          总页数
        :param record_count:         数据总个数
        :param page_range:             页的范围
        :param page_count_limit:    最多显示页面
        :param page_record_limit:    每页显示的行数
        :param page_record_list:    页面数据列表
        :param current_page:        当前页
        :param page_mid:            页面显示页码中间位置页码
        """
        # 当前页码
        try:
            current_page = int(current_page)
            if current_page <= 1:
                current_page = 1
        except Exception as e:
            current_page = 1
        self.current_page = current_page
        # 数据总个数
        self.record_count = record_count
        # 每页显示的行数
        self.page_record_limit = page_record_limit
        # 总页数(数据总个数record_count / 每页显示的行数page_record_limit)
        # [数据总个数]对[每页显示的行数]取余,如果余数为0,总页数等于商,否则等于商+1
        page_count, tmp = divmod(record_count, page_record_limit)
        if tmp:
            self.page_count=page_count+1
        else:
            self.page_count = page_count
        # 页面页数显示限制(要奇数,便于对称显示)
        self.page_count_limit = page_count_limit
        self.searchtitle = searchtitle

    # 每页第一条数据
    @property
    def start(self):
        return (self.current_page - 1) * self.page_record_limit

    # 每页最后一条数据
    @property
    def end(self):
        return self.current_page * self.page_record_limit

    def page_range(self):

        # 如果,总页码[小于]最多显示页面：
        if self.page_count <= self.page_count_limit:
            page_start = 1
            page_end = self.page_count + 1
        # 如果,总页码[大于]最多显示页面：
        else:
            # 页面显示页码中间位置页码
            self.page_mid = int(self.page_count_limit-1)// 2
            if self.current_page <= self.page_mid:
                page_start = 1
                page_end = self.page_count_limit + 1
            else:
                if (self.current_page + self.page_mid) > self.page_count:
                    page_start = self.page_count - self.page_count_limit + 1
                    page_end = self.page_count + 1
                else:
                    page_start = self.current_page - self.page_mid
                    page_end = self.current_page + self.page_mid + 1
        return range(page_start, page_end)

    # 页面显示页码的控制
    def page_html(self):
        # 准备页面渲染的数据
        page_record_list = []
        # 首页
        if self.searchtitle:
            first_page = '<li><a href="?page=%s&searchtitle='% (1,)+self.searchtitle+'">首页</a></li>'
        else:
            first_page = '<li><a href="?page=%s">首页</a></li>' % (1,)
        page_record_list.append(first_page)

        # 处理上一页
        if self.current_page <= 1:
            prev_page = '<li class="disabled"><a href="#">上一页</a></li>'
        elif self.searchtitle:
            prev_page = '<li><a href="?page=%s&searchtitle='% (self.current_page - 1,)+self.searchtitle+'">上一页</a></li>'
        else:
            prev_page = '<li><a href="?page=%s">上一页</a></li>' % (self.current_page - 1,)
        page_record_list.append(prev_page)

        # 页码显示部分
        for i in self.page_range():
            if i == self.current_page:
                temp = '<li class="active"><a href="?page=%s">%s</a></li>' % (i, i)
            elif self.searchtitle:
                temp = '<li><a href="?page=%s&searchtitle='% (i,)+self.searchtitle+'">%s</a></li>' % (i,)
            else:
                temp = '<li><a href="?page=%s">%s</a></li>' % (i, i,)
            page_record_list.append(temp)

        # 处理下一页
        if self.current_page >= self.page_count:
            next_page = '<li class="disabled"><a href="#">下一页</a></li>'
        elif self.searchtitle:
            next_page = '<li><a href="?page=%s&searchtitle='% (self.current_page + 1,)+self.searchtitle+'">下一页</a></li>'
        else:
            next_page = '<li><a href="?page=%s">下一页</a></li>' % (self.current_page + 1,)
        page_record_list.append(next_page)

        # 尾页
        if self.searchtitle:
            last_page = '<li><a href="?page=%s&searchtitle=' % (self.page_count,)+self.searchtitle+'">尾页</a></li>'
        else:
            last_page = '<li><a href="?page=%s">尾页</a></li>' % (self.page_count,)
        page_record_list.append(last_page)

        return ''.join(page_record_list)