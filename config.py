import pbs

l = pbs.Library(self, 'logs', __file__)

l.doc_out_dir = "~/WindowsShare/html/logs"

self.parts.append(l)


#import pbs.classes.Dynamic

#l = pbs.classes.Static.Static("util", self)

#l.make()

#self.include("tests")

