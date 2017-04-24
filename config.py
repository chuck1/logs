import pbs2

l = pbs2.Library(self, 'logs', __file__)

l.doc_out_dir = "/media/sf_P_DRIVE/html/logs"

self.parts.append(l)


#import pbs.classes.Dynamic

#l = pbs.classes.Static.Static("util", self)

#l.make()

#self.include("tests")

