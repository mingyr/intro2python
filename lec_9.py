import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6, 5), dpi=100)
ax = fig.add_subplot(1, 1, 1)
ax.set_xlim(0,360), ax.set_ylim(-1,1)

# FC : Figure coordinates (pixels)
# NFC : Normalized figure coordinates (0 → 1)
# DC : Data coordinates (data units)
# NDC : Normalized data coordinates (0 → 1)

DC_to_FC = ax.transData.transform
FC_to_DC = ax.transData.inverted().transform
NDC_to_FC = ax.transAxes.transform
FC_to_NDC = ax.transAxes.inverted().transform
NFC_to_FC = fig.transFigure.transform
FC_to_NFC = fig.transFigure.inverted().transform

# Top right corner in normalized figure coordinates
print(NFC_to_FC([1,1])) # (600,500)
# Top right corner in normalized data coordinates
print(NDC_to_FC([1,1])) # (540,440)



fig = plt.figure(figsize=(6, 2), dpi=100)
ax = fig.add_subplot(1, 1, 1)
ax.text(0., 0., "A")
ax.text(0., 0., "B", transform=fig.transFigure)
plt.show()




import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.transforms as transforms

fig, ax = plt.subplots()
x = np.random.randn(1000)

ax.hist(x, 30)
ax.set_title(r'$\sigma=1 \/ \dots \/ \sigma=2$', fontsize=16)

# the x coords of this transformation are data, and the y coord are axes
trans = transforms.blended_transform_factory(
    ax.transData, ax.transAxes)
# highlight the 1..2 stddev region with a span.
# We want x to be in data coordinates and y to span from 0..1 in axes coords.
rect = mpatches.Rectangle((1, 0), width=1, height=1, transform=trans,
                          color='yellow', alpha=0.5)
ax.add_patch(rect)

plt.show()





import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(5, 4))

# plot some data in data coordinates
x, y = 10*np.random.rand(2, 1000)
ax.plot(x, y*10., 'go', alpha=0.2)  #

# add a circle in fixed-coordinates
circ = mpatches.Circle((2.5, 2), 1.0, transform=fig.dpi_scale_trans,
                       facecolor='blue', alpha=0.75)
ax.add_patch(circ)
plt.show()



import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots()

# make a simple sine wave
x = np.arange(0., 2., 0.01)
y = np.sin(2*np.pi*x)
line, = ax.plot(x, y, lw=3, color='blue')

# shift the object over 2 points, and down 2 points
dx, dy = 2/72., -2/72.
offset = transforms.ScaledTranslation(dx, dy, fig.dpi_scale_trans)
shadow_transform = ax.transData + offset

# now plot the same data with our offset transform;
# use the zorder to make sure we are below the line
ax.plot(x, y, lw=3, color='gray',
        transform=shadow_transform,
        zorder=0.5*line.get_zorder())

ax.set_title('creating a shadow effect with an offset transform')
plt.show()