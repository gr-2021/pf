import panel as pn
from pandas import DataFrame
from bokeh.models import ColumnDataSource, LabelSet, Label, Arrow, VeeHead
from bokeh.plotting import figure

class WebApp():
    def __init__(self):
        self.cols = ['Source', 'PSQL', 'Task I', 'Task II', 'API', 'Task III', 'S3', 'DB', 'Viz I', 'Viz II', 'Viz III']
        self.obj_cols = ['Dados de Produção', 'Produção no Postgres', 'Coleta Postgres', 'Requisição na API','Modelo de M.L', 'Parquet para o S3', 'Bucket S3 com PySpark', 'Dados Classificados', 'Streamlit', 'PowerBi', 'Tableau']
        self.c = ['purple', 'red','gray', 'gray', 'blue', 'gray', 'red', 'purple', 'green', 'green', 'green']
        self.x = [1, 2, 3, 4, 4, 5, 6, 7,  7,   8, 7]
        self.y = [2.5, 2, 2.5, 2, 1, 2, 2, 2,  1.5, 2,   2.5]
        self.r = [.1, .1, .05, .05, .1, .05, .1, .1, .1, .1, .1]

    def window(self):
        source = ColumnDataSource(data=dict(x=self.x, y=self.y, c=self.c, r=self.r, cols=self.cols))
        p = figure(title="Pipeline de Deploy", width=550, height=400)
        p.scatter(source=source, x='x', y='y', color='c', radius='r', size=2)

        table = pn.widgets.Tabulator(pagination='remote', page_size=11).servable(target='last_project')
        info_pipe = {'bolinhas': self.cols,'objetivo': self.obj_cols}
        table.value = DataFrame(info_pipe).set_index('bolinhas')

        x_starts = [1, 3, 3, 4, 4, 5, 6, 7, 7, 8]
        y_starts = [2.5,2.5,2.5,2,2,2,2,2.5,1.5,2]
        x_ends = [2,2,4,4,5,6,7,7,7,7]
        y_ends = [2,2,2,1,2,2,2,2,2,2]

        for xs, ys, xe, ye in zip(x_starts, y_starts, x_ends, y_ends): 
            p.add_layout(Arrow(end=VeeHead(size=5),
                x_start=xs, y_start=ys, x_end=xe, y_end=ye
            ))

        labels = LabelSet(x='x', y='y', text='cols', x_offset=4, y_offset=4, source=source)

        p.add_layout(labels)

        try:
            pn.pane.Bokeh(p).servable(target='last_project')
        except ValueError:
            print('Oi?')

        return None