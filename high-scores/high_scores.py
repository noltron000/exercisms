def latest(scores):
	return scores[-1]


def personal_best(scores):
	return max(scores)


def personal_top_three(scores):
	top_scores = [0]*min(len(scores),3)
	for score in scores:
		for top_score in top_scores:
			if score > top_score:
				idx = top_scores.index(top_score)
				top_scores.insert(idx, score)
				top_scores.pop()
				break
	print(top_scores)
	return top_scores
