
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
class MyPagination(PageNumberPagination):
    page_size = 25
    page_query_param = 'mypage'
    page_size_query_param = 'num'
    max_page_size = 30
    last_page_strings = ('endpage')

class MyPagination2(LimitOffsetPagination):
    default_limit = 15
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 25

class MyPagination3(CursorPagination):
    # pass #created
    ordering = 'esal'
    page_size = 5
