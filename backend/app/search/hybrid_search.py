from backend.app.search.semantic_search import semantic_search
from backend.app.search.lexical_search import lexical_search
from backend.app.search.personalization import (
    compute_personalization_score
)

def normalize_scores(results):

    scores = [
        result["score"]
        for result in results
    ]

    min_score = min(scores)
    max_score = max(scores)

    # Avoid division by zero
    if max_score == min_score:

        for result in results:

            result["normalized_score"] = 1.0

        return results

    for result in results:

        normalized = (
            result["score"] - min_score
        ) / (
            max_score - min_score
        )

        result["normalized_score"] = normalized

    return results


def hybrid_search(
    query,
    top_k=5,
    semantic_weight=0.6,
    lexical_weight=0.3,
    personalization_weight=0.1,
    user_preferences=None
):

    semantic_results = semantic_search(
        query,
        top_k=50
    )

    lexical_results = lexical_search(
        query,
        top_k=50
    )

    semantic_results = normalize_scores(
        semantic_results
    )

    lexical_results = normalize_scores(
        lexical_results
    )

    combined_results = {}

    # Add semantic scores
    for result in semantic_results:

        title = result["title"]

        combined_results[title] = {
            "semantic_score":
                result["normalized_score"],
            "lexical_score": 0.0
        }

    # Add lexical scores
    for result in lexical_results:

        title = result["title"]

        if title not in combined_results:

            combined_results[title] = {
                "semantic_score": 0.0,
                "lexical_score":
                    result["normalized_score"]
            }

        else:

            combined_results[title][
                "lexical_score"
            ] = result["normalized_score"]

    final_results = []

    for title, scores in combined_results.items():
        personalization_score = (
            compute_personalization_score(
                title,
                user_preferences
            )
        )

        final_score = (
            semantic_weight
            * scores["semantic_score"]
            +
            lexical_weight
            * scores["lexical_score"]
            +
            personalization_weight
            * personalization_score
        )

        final_results.append({
            "title": title,
            "score": final_score,
            "semantic_score":
                scores["semantic_score"],
            "lexical_score":
                scores["lexical_score"],
            "personalization_score":
                personalization_score,
        })

    final_results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return final_results[:top_k]

if __name__ == "__main__":

    query = input("Search query: ")

    results = hybrid_search(query)

    print("\nTop Results:\n")

    for result in results:

        print(
            f"{result['score']:.4f} | "
            f"S:{result['semantic_score']:.4f} | "
            f"L:{result['lexical_score']:.4f} | "
            f"{result['title']}"
        )