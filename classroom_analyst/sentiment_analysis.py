from google.cloud import language

def analyze(reviews):
	"""
	param:reviews : list of reviews for a particular faculty
	"""
	annotations_list = []
	language_client = language.Client()
	
	for review in reviews:
		document = language_client.document_from_html(review.content)
		annotations = document.annotate_text(include_sentiment=True,
				include_syntax=False,
				include_entities=False)
		annotations_list.append(annotations)

	positive,negative,neutral = 0,0,0
	total = len(annotations_list)

	for annotation in annotations_list:
		score = annotation.sentiment.score
		magnitude = annotation.sentiment.magnitude
		
		if score >= 0.2:
			positive += 1
		elif score <= -0.2:
			negative += 1
		else:
			neutral += 1

	return (total,positive, negative, neutral)