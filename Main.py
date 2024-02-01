from serial import serialcomp
from parallel import parallelcomp
from multiprocessing import Process
import pandas as pd
import matplotlib.pyplot as plt

# Define the function to process a document
def parallelcompmulti():
    if __name__ == '__main__':
        docs = ["wordfiledoc.txt", "lorem_ipsum_100.txt"]
        processes = []
        count = 0

        for doc in docs:
            p = Process(target=parallelcomp, args=(doc,))
            processes.append(p)
            p.start()
            count += 1
            print(count)

        # Wait for all processes to finish
        for p in processes:
            p.join()

        # Files to store summaries and word counts
array_wordfiledoc_summary = ["wordfiledoc__Serial_counts_summary.csv", "wordfiledoc_parallel_summary.csv"]
array_wordfiledoc_word_counts = ["wordfiledoc_Serial_counts.csv", "wordfiledoc_parallel_word_counts.csv"]

        # Define the function to process wordfiledoc
def wordfiledoc(summary_files, word_count_files):
        count = 0
        for summary_file in summary_files:
                df_summary = pd.read_csv(summary_file)
                document = df_summary['Document'][0]
                num_words = df_summary['Number of Words'][0]
                total_time = df_summary['Total Time'][0]
                type = df_summary['Type'][0]

                print(f"Document: {document}\nType: {type} \nNumber of Words: {num_words}\nTotal Time: {total_time} seconds")
                count += 1
                print(count)

        for word_count_file in word_count_files:
                df_word_counts = pd.read_csv(word_count_file)
                plt.figure(figsize=(10, 6))
                plt.bar(df_word_counts['Word'], df_word_counts['Count'], color="skyblue")
                plt.ylabel('Counts')
                plt.title(f'Word Counts in {word_count_file}')
                plt.xticks(rotation=45, ha="right")
                plt.tight_layout()
                plt.show()
lorem_ipsum_summary = ["lorem_ipsum_100_parallel_summary.csv", "lorem_ipsum_100__Serial_counts_summary.csv"]
lorem_ipsum_word_counts = ["lorem_ipsum_100_Serial_counts.csv", "lorem_ipsum_100_parallel_word_counts.csv"]

        # Define the function to process lorem_ipsum
def lorem_ipsum(summary_files, word_count_files):
            count = 0

            for summary_file in summary_files:
                df_summary = pd.read_csv(summary_file)
                document = df_summary['Document'][0]
                num_words = df_summary['Number of Words'][0]
                total_time = df_summary['Total Time'][0]
                type = df_summary['Type'][0]

                print(f"Document: {document} \nType: {type} \nNumber of Words: {num_words}\nTotal Time: {total_time} seconds")
                count += 1
                print(count)

            for word_count_file in word_count_files:
                df_word_counts = pd.read_csv(word_count_file)
                plt.figure(figsize=(10, 6))
                plt.bar(df_word_counts['Word'], df_word_counts['Count'], color="skyblue")
                plt.ylabel('Counts')
                plt.title(f'Word Counts in {word_count_file}')
                plt.xticks(rotation=45, ha="right")
                plt.tight_layout()
                plt.show()

#parallelcompmulti()
#serialcomp()
wordfiledoc(array_wordfiledoc_summary, array_wordfiledoc_word_counts)

lorem_ipsum(lorem_ipsum_summary, lorem_ipsum_word_counts)
