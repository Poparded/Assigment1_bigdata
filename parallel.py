import time
import pandas as pd
from collections import Counter

def parallelcomp(doc):
    data = []  # List to hold the data for DataFrame
    total_time = 0
    counter= Counter()
    word_count_array = []

    start_time = time.perf_counter()

    with open(doc, "r") as file:
        lines = file.readlines()
        for line in lines:
            words = line.split()
            counter.update(words)
        num_words = sum(len(line.split()) for line in lines)
        num_lines = len(lines)






    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time

    summary_data = [{'Document': doc,"Type": "Parallel", 'Number of Words': num_words, 'Number of Lines': num_lines,
                     'Execution Time (Seconds)': execution_time, 'Total Time': total_time}]
    df_summary = pd.DataFrame(summary_data)
    summary_filename = f"{doc.replace('.txt', '')}_parallel_summary.csv"
    df_summary.to_csv(summary_filename, index=False)

    # Sorted word counts
    word_counts_data = [{'Word': word, 'Count': count} for word, count in counter.items()]
    df_word_counts = pd.DataFrame(word_counts_data).sort_values(by='Count', ascending=True)
    word_counts_filename = f"{doc.replace('.txt', '')}_parallel_word_counts.csv"
    df_word_counts.to_csv(word_counts_filename, index=False)

