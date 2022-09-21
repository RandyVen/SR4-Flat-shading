#Randy Venegas
from gl import Render

modelName = input('Modelo?: ')

r = Render()
r.glInit(800,600)
r.load(modelName, [2,1,4], [160, 160, 160])
r.glFinish("out2.bmp")