import LollipopGraph as lol

G = lol.LollipopGraph(3,18)

G.updateDist({"v0"  : 10, "x3" : 2, "v8"  : 1})
#G.drawGraph(show_pebbling=True,CycleColor="blue",PathColor="green")

G.info()

G.drawGraph(CycleColor = "red",PathColor="green")

