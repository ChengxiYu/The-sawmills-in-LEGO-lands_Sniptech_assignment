# The-sawmills-in-LEGO-lands_Sniptech_assignment
This solution is written in python.
It passed test case, which is called "test.txt" in solution folder.
you could run "python main.py" in cmd and see the result.

i used bruto force to calculate the profits of all possible permutations of the trunk set. I think we have to use this if we need all possible output of the trunks order.
because if we need all possible order of a set of more than 7 trunks for example, with the length of [1,2,3,4,5,6,7], we have a maximum profit of 14, 120 possible order for 
this maximum order, for example (1, 7, 5, 3, 6, 4, 2) and (1, 3, 7, 2, 4, 5, 6). the main reason for this is trunks with length 3 can be insert into the trunk orders, because maximum profit for a single 3 is cut into (2,1)
for example, (2,1,1,4,3,1) is totally the same with (2,1,1,3,4,1) and (2,3,1,1,4,1). The complexity will be very huge if the trunk number is very beg.

But if we only need the best profit and one order for this profit, there is a easier way. I have a protocol for this but have not realized.
