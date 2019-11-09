from scratch.introduction import users, friendship_pairs, interests, salaries_and_tenures


friendships = {user["id"]: [] for user in users}

for i,j in friendship_pairs:
	friendships[i].append(j)
	friendships[j].append(i)

def number_of_friends(user):
	"""How many friends does this user have?"""
	user_id = user["id"]
	friend_ids = friendships[user_id]
	return len(friend_ids)

total_connections =	sum(number_of_friends(user)
						for user in users) #24

num_users = len(users) #10
mean_connections = total_connections/num_users #2.4

# Create a list (user_id, number of friends)
num_of_friends_by_id = [(user["id"],number_of_friends(user)) 
						for user in users]

num_of_friends_by_id.sort(
				key = lambda id_and_friends: id_and_friends[1],
				reverse=True)
#print(num_of_friends_by_id)

# Data Scientists you may know

def foaf_ids_terrible(user):
	"""friend of a friend"""
	foaf_ids = []
	for friend_id in friendships[user["id"]]:
		foaf_ids += friendships[friend_id]
	return foaf_ids

def foaf_ids_bad(user):
	return [foaf_id
			for friend_id in friendships[user["id"]]
			for foaf_id in friendships[friend_id]]
	
#print(foaf_ids_terrible(users[0]))
#print(foaf_ids_bad(users[0]))

from collections import Counter

def friends_of_friends(user):
		user_id = user["id"]
		return Counter(
			foaf_id
			for friend_id in friendships[user_id]
			for foaf_id in friendships[friend_id]
			if foaf_id != user_id
			and foaf_id not in friendships[user_id]
		)

#print(friends_of_friends(users[0]))

def data_scientists_who_like(target_interest):
	""" Find the ids of all users who like the target interest. """
	return[user_id 
			for user_id, interest in interests 
			if interest == target_interest
	]
#print(data_scientists_who_like('Hadoop')) ~#[0,9]

from collections import defaultdict

# Keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
		user_ids_by_interest[interest].append(user_id)

interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
	interests_by_user_id[user_id].append(interest)

"""
iterate over user's interests
lookup list of users interested in that from index
"""

def most_common_interests_with(user):
	return Counter(
		interested_user_id
		for interest in interests_by_user_id[user["id"]]			# for each of my interests
		for interested_user_id in user_ids_by_interest[interest]	# find other users also interested
		if interested_user_id != user["id"]							# except for me
	)

assert(most_common_interests_with(users[0]) == Counter({9: 3, 1: 2, 8: 1, 5: 1}))

#---------------------------------------------------------------------------------------------------------

""" Keys are years, values are lists of the salaries for each tenure """
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
	salary_by_tenure[tenure].append(salary)

""" Keys are years,each value is average salary for that tenure """
average_salary_by_tenure = {
	tenure: sum(salaries)/ len(salaries)
	for tenure, salaries in salary_by_tenure.items()
}

def tenure_bucket(tenure):
	if tenure < 2:
		return "less than 2"
	elif tenure < 5:
		return "between 2 and 5"
	else:
		return "over 5"

salaries_by_tenure_bucket = defaultdict(list)

for salary,tenure in salaries_and_tenures:
	bucket = tenure_bucket(tenure)
	salaries_by_tenure_bucket[bucket].append(salary)

""" Keys are tenure buckets,each value is average salary for that tenure bucket """
average_salary_by_tenure = {
	tenure_bucket: sum(salaries)/ len(salaries)
	for tenure_bucket, salaries in salaries_by_tenure_bucket.items()
}

print(salaries_by_tenure_bucket)

print(average_salary_by_tenure)