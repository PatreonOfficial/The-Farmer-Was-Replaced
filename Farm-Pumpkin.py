clear()
isfull = False
while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
					till()
			plant(Entities.Pumpkin)
			move(East)
		move(North)
	
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_entity_type() == Entities.Pumpkin:
				isfull = True
			else:
				isfull = False
				plant(Entities.Pumpkin)
			move(East)
		move(North)
	if isfull:
		harvest()
	