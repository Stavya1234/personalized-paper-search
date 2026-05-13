def compute_personalization_score(
    paper_text,
    user_preferences
):

    """
    Computes a personalization relevance score
    based on overlap between paper text and
    user preference topics.

    Returns a normalized score between 0 and 1.
    """

    if not user_preferences:
        return 0.0

    paper_text = paper_text.lower()

    matches = 0

    for topic in user_preferences:

        topic = topic.lower().strip()

        if topic in paper_text:
            matches += 1

    return matches / len(user_preferences)