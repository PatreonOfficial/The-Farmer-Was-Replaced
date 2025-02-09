directions = [North, East, South, West]
index = 0
def create_maze():
	clear()
	plant(Entities.Bush)
	n_substance = get_world_size() * 1
	use_item(Items.Weird_Substance, n_substance)

	treasure_hunt()
def treasure_hunt():
	global index
	while True:
		if move(directions[index]):
			index = (index + 1) % 4
		elif move(directions[index]) == False:
			index = (index - 1) % 4
		if get_entity_type() == Entities.Treasure:
			harvest()
			create_maze()
create_maze()