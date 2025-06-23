from grading_word.accuracy_grading import calculate_total_scores
from grading_word.formatting_grading import calculate_total_scores_formatting

# def add_accuracy_scores(path, existing_scores=None):
#     """Add accuracy scores to existing scores"""
#     accuracy_scores = calculate_total_scores(path)
#     formatting_scores = calculate_total_scores_formatting(path)
#
#     if existing_scores is None:
#         return accuracy_scores
#
#     # Merge scores
#     total_scores = {}
#     all_files = (
#         set(accuracy_scores.keys())
#         | set(formatting_scores.keys())
#         | set(existing_scores.keys())
#     )
#
#     for filename in all_files:
#         accuracy = accuracy_scores.get(filename, 0)
#         formatting = formatting_scores.get(filename, 0)
#         existing = existing_scores.get(filename, 0)
#         total_scores[filename] = accuracy + formatting + existing
#         print(
#             f"📊 {filename} — Combined Score: {total_scores[filename]} (Accuracy: {accuracy}, Other: {existing})"
#         )
#
#     return total_scores


def add_accuracy_scores(path, existing_scores=None):
    """Add accuracy and formatting scores to existing scores"""
    accuracy_scores = calculate_total_scores(path)
    formatting_scores = calculate_total_scores_formatting(path)

    total_scores = {}
    all_files = (
        set(accuracy_scores) | set(formatting_scores) | set(existing_scores or {})
    )

    for filename in all_files:
        accuracy = accuracy_scores.get(filename, 0)
        formatting = formatting_scores.get(filename, 0)
        existing = (existing_scores or {}).get(filename, 0)
        total_scores[filename] = accuracy + formatting + existing
        print(
            f"📊 {filename} — Combined Score: {total_scores[filename]} "
            f"(Accuracy: {accuracy}, Formatting: {formatting}, Existing: {existing})"
        )

    return total_scores
