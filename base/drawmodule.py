from drawille import Canvas

c = Canvas()

def draw_plot(data_to_draw):
	c = Canvas()
	for x in data_to_draw:
		index = data_to_draw.index(x)
		c.set(index, float(x['Position']))
	print(c.frame())
print(c.frame())

