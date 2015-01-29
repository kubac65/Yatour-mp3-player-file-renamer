import os
import sys

if len(sys.argv) != 2:
	print 'Provide path to the folder'
else:
	dir_path = sys.argv[1]
	dirs = os.listdir(dir_path)
	dirs.sort()
	dir_counter = 1

	for dir_name in dirs:
		os.rename(os.path.join(dir_path, dir_name), os.path.join(dir_path, str(dir_counter)))
		dir_counter += 1

	dirs = os.listdir(dir_path)
	dirs.sort()
	dir_counter = 1
	
	for dir_name in dirs:
		path = os.path.join(dir_path, dir_name)
		if os.path.isdir(path):
			new_dir_name = 'CD%02d' % dir_counter
			new_path = os.path.join(dir_path, new_dir_name)
			os.rename(path, new_path)
			print 'Renamed dir:', dir_name, 'to:', new_dir_name
			dir_counter += 1

			files = os.listdir(new_path)
			files.sort()

			files_counter = 1

			for file_name in files:
				file_path = os.path.join(new_path, file_name)
				if os.path.isfile(file_path):
					if file_name[-4:] == '.mp3':
						os.rename(file_path, os.path.join(new_path, '%03d.mp3' % files_counter))
						files_counter += 1
					else:
						os.remove(file_path)	