h = {((5, 5), 'East', 1): ((4, 5), 'West', 1), ((3, 5), 'West', 1): ((4, 5), 'West', 1), ((4, 5), 'East', 1): ((3, 5), 'West', 1), ((2, 5), 'West', 1): ((3, 5), 'West', 1), ((3, 5), 'East', 1): ((2, 5), 'West', 1), ((1, 5), 'West', 1): ((2, 5), 'West', 1), ((1, 4), 'South', 1): ((1, 5), 'West', 1), ((2, 5), 'East', 1): ((1, 5), 'West', 1), ((5, 4), 'South', 1): ((5, 5), 'East', 1), ((4, 5), 'West', 1): ((5, 5), 'East', 1), ((5, 5), 'North', 1): ((5, 4), 'South', 1), ((5, 3), 'South', 1): ((5, 4), 'South', 1), ((5, 4), 'North', 1): ((5, 3), 'South', 1), ((4, 3), 'West', 1): ((5, 3), 'South', 1), ((4, 2), 'South', 1): ((4, 3), 'West', 1), ((5, 3), 'East', 1): ((4, 3), 'West', 1), ((4, 3), 'North', 1): ((4, 2), 'South', 1), ((3, 2), 'West', 1): ((4, 2), 'South', 1), ((4, 2), 'East', 1): ((3, 2), 'West', 1), ((2, 2), 'West', 1): ((3, 2), 'West', 1), ((2, 3), 'North', 1): ((2, 2), 'West', 1), ((2, 1), 'South', 1): ((2, 2), 'West', 1), ((3, 2), 'East', 1): ((2, 2), 'West', 1), ((2, 2), 'North', 1): ((2, 1), 'South', 1), ((1, 1), 'West', 1): ((2, 1), 'South', 1)}

# ((x1,y1), direct1, g1),((x2,y2), direct2, g2)

curr = ((1, 1), 'West', 1)
lst = [curr]

i = 8
while i:
	i -= 1
	print(curr)
	lst.append(h[curr]) 
	curr = h[curr]


print(lst)




