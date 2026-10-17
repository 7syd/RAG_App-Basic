def retrieve_documents(
    vectorstore,
    query: str,
    k: int = 3,
    queries: list[str] | None = None,
):
    """
    Retrieve relevant chunks and preserve their distance scores.

    Lower Chroma distance scores generally indicate closer matches.
    Distances are not probabilities.
    """

    search_queries = [query]

    if queries:
        search_queries.extend(queries)

    results = []
    seen_chunks = set()

    for search_query in search_queries:
        matches = vectorstore.similarity_search_with_score(
            search_query,
            k=k,
        )

        for document, distance in matches:
            chunk_text = document.page_content.strip()

            if chunk_text and chunk_text not in seen_chunks:
                seen_chunks.add(chunk_text)

                results.append({
                    "document": document,
                    "distance": float(distance),
                    "matched_query": search_query,
                })

    # Put the closest matches first.
    results.sort(key=lambda item: item["distance"])

    return results