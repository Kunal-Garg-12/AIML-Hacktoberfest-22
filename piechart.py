import matplotlib.pyplot as pt

sizes = [50,23,17,15,5]

labels=['apple','blueberry','strawberry','banoffe','chocolate']
colors=['yellow','orange','cyan','red','pink']
pt.pie(sizes,colors=colors,startangle=90,labels=labels)
pt.title('pie chart')
pt.legend(title='legend',loc = 'lower left')
pt.axis('equal')

pt.show()
