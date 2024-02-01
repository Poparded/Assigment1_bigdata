import time
import pandas as pd
from collections import Counter

def serialcomp():
    data = []  # List to hold the data for DataFrame
    docs = ["wordfiledoc.txt","lorem_ipsum_100.txt"]

    total_time = 0

    for doc in docs:
        data = []  # List to hold the data for DataFrame
        total_time = 0
        counter= Counter()

        start_time = time.perf_counter()

        with open(doc, "r") as file:
            lines = file.readlines()
            for line in lines:
                words = line.split()
                counter.update(words)
                execution_time = end_time - start_time

            num_words = sum(len(line.split()) for line in lines)
            num_lines = len(lines)

        end_time = time.perf_counter()
        execution_time = end_time - start_time
        total_time += execution_time

        summary_data = [
            {'Document': doc, "Type": "serial", 'Number of Words': num_words, 'Number of Lines': num_lines,
             'Execution Time (Seconds)': execution_time, 'Total Time': total_time}]
        df_summary = pd.DataFrame(summary_data)
        summary_filename = f"{doc.replace('.txt', '')}__Serial_counts_summary.csv"
        df_summary.to_csv(summary_filename, index=False)

        # Sorted word counts
        word_counts_data = [{'Word': word, 'Count': count} for word, count in counter.items()]
        df_word_counts = pd.DataFrame(word_counts_data).sort_values(by='Count', ascending=True)
        word_counts_filename = f"{doc.replace('.txt', '')}_Serial_counts.csv"
        df_word_counts.to_csv(word_counts_filename, index=False)


# Call the function
serialcomp()
