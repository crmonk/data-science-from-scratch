from scratch.introduction import users, friendship_pairs, interests

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
			for user_id, interest_name
			where interest_name = target_interest]

data_scientists_who_like()