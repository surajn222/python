# https://stackoverflow.com/questions/11977279/builder-pattern-equivalent-in-python

class Row_Builder(object):
  def __init__(self):
    self.row = ['' for i in range(10)]

  def with_fy(self, fiscal_year):
    self.row[fiscal_year] = fiscal_year
    return self

  def with_id(self, batch_id):
    self.row[batch_id] = batch_id
    return self

  def build(self):
    return self.row

  def __str__(self):
    print(f"{self.row}")

Row = Row_Builder().with_fy(1).build()
print(Row)

