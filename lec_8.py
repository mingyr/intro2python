import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6,6))
ax = plt.subplot(aspect=1)
ax.plot(range(10))
plt.show()



fig, ax = plt.subplots(figsize=(5,2))
for label in ax.get_xaxis().get_ticklabels():
    label.set_fontweight("bold")

plt.show()

def figure(dpi):
    fig = plt.figure(figsize=(4.25,.2))
    ax = plt.subplot(1,1,1)
    text = "Text rendered at 10pt using %d dpi" % dpi
    ax.text(0.5, 0.5, text, ha="center", va="center",
        fontname="Source Serif Pro",
        fontsize=10, fontweight="light")
    plt.savefig("figure-dpi-%03d.png" % dpi, dpi=dpi)
    
figure(50), figure(100), figure(300), figure(600)

