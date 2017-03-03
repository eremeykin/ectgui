class PlotInfo:
    def __init__(self, table_models):
        self.data = {'X': None, "Y": None, "C": None}
        self.tables = set()

    def set(self, table, column, marker):
        self.tables.add(table)
        for tab in self.tables:
            tab.model().del_marker(marker)
            tab.horizontalHeader().viewport().update()
        table.model().set_marker(column, marker)
        table.horizontalHeader().viewport().update()
        self.data[marker] = (table, column)

    def delete_markers(self):
        for tab in self.tables:
            tab.model().del_all_markers()
            tab.horizontalHeader().viewport().update()
        self.data = {'X': None, "Y": None, "C": None}

    def get(self, marker):
        try:
            table, column = self.data[marker]
        except TypeError:
            return None
        return table.model().get_actual_data().ix[:, column]

