clear()
print("So eine Zeitverschwendung")
while True:
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		if can_harvest():
			if measure() >= 7:
				harvest()
		plant(Entities.Sunflower)
		move(East)
	move(North)