import matplotlib.pyplot as plt

def generate_bar_chart():
  labels = ['a', 'b', 'c']
  values = [100,200,80]
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig('bar.png')
  plt.close()

  def generate_pie_chart():
    labels = ['a', 'b', 'c']
  values = [100,200,80]
    fig, ax = plt.subplots()
    ax.pie(values, labeles=labels)
    ax.axis('equal')
    plt.savefig('pie.png')
    plt.close()
    

if __name__ == '__main__':
  #generate_bar_chart()
  generate_pie_chart()