import matplotlib.pyplot as plt


def generete_pie_chart():
    labels = ['A', 'B', 'C', 'D']
    values = [15, 30, 45, 10]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig("pie.png")
    plt.close()