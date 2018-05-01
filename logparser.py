
#!/usr/bin/env python2

#parser, parse the data into a data structure.

class log_line(object):
	def __init__(self, logline):
		#self.src = logline.split()
		for value in logline.split():
			if 'src=' in value:
				self.src = value[4:]
				continue
			if 'dst=' in value:
				self.dst = value[4:]
				continue
			if 'srcport=' in value:
				self.srcport = value[8:]
				continue
			if 'dstport=' in value:
				self.dstport = value[8:]
				continue
			if value.isdigit():
				self.time = value #[:]	

	def __repr__(self):
		return repr(self.src + ' ' + self.dst +  ' ' + self.srcport + ' ' + self.dstport + ' ' + self.time)
				
logs = []

with open('data.txt','r') as file:
	for line in file:
		logs.append(log_line(line))

print repr(logs)