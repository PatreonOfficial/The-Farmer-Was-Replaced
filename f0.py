clear()
for i in range(get_world_size()):
	for j in range(get_world_size()):
		till()
		move(East)
	move(North)
change_hat(Hats.Dinosaur_Hat)