from grading_word.accuracy_grading import calculate_total_scores
from grading_word.formatting_grading import calculate_total_scores_formatting


def add_accuracy_scores(path, existing_scores=None):
    """Add accuracy and formatting scores to existing scores"""
    accuracy_scores = calculate_total_scores(path)
    formatting_scores = calculate_total_scores_formatting(path)

    total_scores = {}
    all_files = (
        set(accuracy_scores) | set(formatting_scores) | set(existing_scores or {})
    )

    for dirname in all_files:
        accuracy = accuracy_scores.get(dirname, 0)
        formatting = formatting_scores.get(dirname, 0)
        existing = (existing_scores or {}).get(dirname, 0)
        total_scores[dirname] = accuracy + formatting + existing
        print(
            f"📊 {dirname} — Combined Score: {total_scores[dirname]} "
            f"(Accuracy: {accuracy}, Formatting: {formatting}, Existing: {existing})"
        )

    return total_scores


# def add_accuracy_scores(path, existing_scores=None):
#     """Add accuracy and formatting scores for both DOCX and PPTX files"""
#     # DOCX scores
#     docx_accuracy_scores = calculate_total_scores(path)
#     docx_formatting_scores = calculate_total_scores_formatting(path)
#
#     # PPTX scores (you'll need to create these functions)
#     pptx_accuracy_scores = calculate_total_scores_pptx(path)
#     pptx_formatting_scores = calculate_total_scores_formatting_pptx(path)
#
#     total_scores = {}
#     all_files = (
#         set(docx_accuracy_scores) | set(docx_formatting_scores) |
#         set(pptx_accuracy_scores) | set(pptx_formatting_scores) |
#         set(existing_scores or {})
#     )
#
#     for dirname in all_files:
#         docx_accuracy = docx_accuracy_scores.get(dirname, 0)
#         docx_formatting = docx_formatting_scores.get(dirname, 0)
#         pptx_accuracy = pptx_accuracy_scores.get(dirname, 0)
#         pptx_formatting = pptx_formatting_scores.get(dirname, 0)
#         existing = (existing_scores or {}).get(dirname, 0)
#
#         total_scores[dirname] = (docx_accuracy + docx_formatting +
#                                pptx_accuracy + pptx_formatting + existing)
#
#         print(
#             f"📊 {dirname} — Combined Score: {total_scores[dirname]} "
#             f"(DOCX: {docx_accuracy + docx_formatting}, "
#             f"PPTX: {pptx_accuracy + pptx_formatting}, "
#             f"Existing: {existing})"
#         )
#
#     return total_scores
#

# import csv
#
# def add_accuracy_scores(path, existing_scores=None):
#     """Add accuracy and formatting scores for both DOCX and PPTX files"""
#     # DOCX scores
#     docx_accuracy_scores = calculate_total_scores(path)
#     docx_formatting_scores = calculate_total_scores_formatting(path)
#
#     # PPTX scores (you'll need to create these functions)
#     # pptx_accuracy_scores = calculate_total_scores_pptx(path)
#     # pptx_formatting_scores = calculate_total_scores_formatting_pptx(path)
#
#     # For now, using empty dicts for PPTX until you implement them
#     pptx_accuracy_scores = {}
#     pptx_formatting_scores = {}
#
#     total_scores = {}
#     detailed_scores = {}
#
#     all_files = (
#         set(docx_accuracy_scores) | set(docx_formatting_scores) |
#         set(pptx_accuracy_scores) | set(pptx_formatting_scores) |
#         set(existing_scores or {})
#     )
#
#     for dirname in all_files:
#         docx_accuracy = docx_accuracy_scores.get(dirname, 0)
#         docx_formatting = docx_formatting_scores.get(dirname, 0)
#         pptx_accuracy = pptx_accuracy_scores.get(dirname, 0)
#         pptx_formatting = pptx_formatting_scores.get(dirname, 0)
#         existing = (existing_scores or {}).get(dirname, 0)
#
#         docx_total = docx_accuracy + docx_formatting
#         pptx_total = pptx_accuracy + pptx_formatting
#         grand_total = docx_total + pptx_total + existing
#
#         total_scores[dirname] = grand_total
#         detailed_scores[dirname] = {
#             'docx_accuracy': docx_accuracy,
#             'docx_formatting': docx_formatting,
#             'docx_total': docx_total,
#             'pptx_accuracy': pptx_accuracy,
#             'pptx_formatting': pptx_formatting,
#             'pptx_total': pptx_total,
#             'existing': existing,
#             'grand_total': grand_total
#         }
#
#         print(
#             f"📊 {dirname} — Combined Score: {grand_total} "
#             f"(DOCX: {docx_total}, PPTX: {pptx_total}, Existing: {existing})"
#         )
#
#     return total_scores, detailed_scores

# def export_scores_to_csv(detailed_scores, filename="grading_results.csv"):
#     """Export detailed scores to CSV file"""
#     if not detailed_scores:
#         print("No scores to export")
#         return
#
#     with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#         fieldnames = ['folder_name', 'docx_accuracy', 'docx_formatting', 'docx_total',
#                      'pptx_accuracy', 'pptx_formatting', 'pptx_total', 'existing', 'grand_total']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#         writer.writeheader()
#         for folder_name, scores in detailed_scores.items():
#             row = {'folder_name': folder_name}
#             row.update(scores)
#             writer.writerow(row)
#
#     print(f"✅ Scores exported to {filename}")
# ```
#
# ## Update your main function to use the new export:
#
# ```python
# def main():
#     path = "your/path/here"
#     total_scores, detailed_scores = add_accuracy_scores(path)
#
#     # Export to CSV
#     export_scores_to_csv(detailed_scores, "student_grades.csv")
