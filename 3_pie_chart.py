from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [60341,55234,47294,36293,35449]
labels = ["Javascript", "html/css", "sql","python", "java"]
explode = [0,0,0,0.1,0]

plt.pie(slices, labels=labels, explode=explode, shadow=True,startangle=90,autopct='%1.1f%%',
        wedgeprops={"edgecolor":"black"})

plt.title("My awesome Pie Chart")
plt.tight_layout()
plt.show()