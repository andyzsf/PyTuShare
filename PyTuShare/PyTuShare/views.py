from django.http import HttpResponse
import tushare

def hello(request):
    print tushare.__version__
    test_tushare(request)
    return HttpResponse("Hello world")
 

def test_tushare(request):
    datas=tushare.get_hist_data('002088',start='2015-07-03',end='2015-07-03')
    print datas