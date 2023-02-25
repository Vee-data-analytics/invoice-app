from pickletools import read_uint1
import pandas as pd  
from pyecharts import options as opts 
from pyecharts.charts import Bar, Calendar, Tab
from positions.models import Position
from django_plotly_dash import DjangoDash
from positions.models import Position
from estipositions.models import Position as estipositions
from django.template import loader
from django.http import HttpResponse


REMOTE_HOST = "https://pyecharts.github.io/assets/js" 


def index(request):
    template = loader.get_template('dash_plots/pycharts.html')
    l3d = invoice_pyechart(request)
    vled = invoice_calendar(request)
    context = dict(
        myechart=l3d.render_embed(),
        calchart=vled.render_embed(),
        host=REMOTE_HOST,
        #script_list=l3d.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))


def invoice_pyechart(request):
    
    qs = Position.objects.all()
    
    invoice_data = [
            {
                'Invoice':x.invoice.invoice_number,
                'Client':x.invoice.clients.name,
                'Issued date':x.created,
                'Close':x.invoice.closed,
                'Amount':x.amount,
                'Title':x.title,
                'Payed':x.invoice.payed,
    
            } for x in qs
        ]
    
    df = pd.DataFrame(invoice_data)
    
    df['Month'] = df['Issued date'].dt.month
    df.head(3)

    grouped_by_months = df.groupby(by=['Month']).sum()[['Amount']]
    grouped_by_months.head(3)
    
    bar_chart_by_month = (
        Bar()
        .add_xaxis(grouped_by_months.index.tolist())
        .add_yaxis('Amount', grouped_by_months['Amount'].round(0).tolist())
        .set_global_opts(
            title_opts=opts.TitleOpts(title='Invoice & Profit by month', subtitle='in R')
        )
    
    )
    return bar_chart_by_month

def invoice_calendar(request):
    qs = Position.objects.all()
    
    invoice_data = [
            {
                'Invoice':x.invoice.invoice_number,
                'Client':x.invoice.clients.name,
                'Issued date':x.created,
                'Close':x.invoice.closed,
                'Amount':x.amount,
                'Title':x.title,
                'Payed':x.invoice.payed,
    
            } for x in qs
        ]
    
    df = pd.DataFrame(invoice_data)
    
    df['Month'] = df['Issued date'].dt.month
    df.head(3)
    
    grouped_by_months = df.groupby(by=['Month']).sum()[[ 'Amount']]
    grouped_by_months.head(3)

    invoice_by_date = df.groupby(by='Issued date').sum()[['Amount']].round(0)
    invoice_by_date = invoice_by_date.reset_index()
    invoice_by_date.head(3)
    
    data = invoice_by_date[[ 'Issued date', 'Amount', ]].values.tolist()
    
    max_amount = df['Amount'].max()
    min_amount = df['Amount'].min()
    
    invoice_calender= (
        Calendar()
        .add('', data, calendar_opts=opts.CalendarOpts(range_='2022'))
        .set_global_opts(
            title_opts = opts.TitleOpts(title='Invoice Calendar', subtitle='Rands'),
            visualmap_opts=opts.VisualMapOpts(
                max_=max_amount,
                min_=min_amount,
                orient='horizontal',
                is_piecewise=False,
                pos_top='230px',
                pos_left='100px',)
        )
    )
    
    

    tab = Tab(page_title='Invoice and Profit Overiew')
 
    return invoice_calender