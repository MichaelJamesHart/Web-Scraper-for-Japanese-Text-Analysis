# Web-Scraper-for-Japanese-Text-Analysis
(IN PROGRESS) A web scraper for analyzing large bodies of Japanese text to provide insight into proficiency level, language use patterns, and key phrase extraction.

The first and primary use of the program will be to scrape my entire body of work from the website DMM uKnow, which is an online English-teaching platform where Japanese people studying English can submit questions about the meaning and utility of English-language words or phrases. The English teachers, called "anchors" on this site, can post replies to the Japanese people's questions. All of the English teacher's explanations are required to be written in Japanese, while the example English sentences are of course provided in English. I was employed by DMM as a language translation "anchor" from 2018 to 2020, and provided 861 answers to Japanese people's questions.

Project Outline:
1) Scrape the Japanese text content from all 861 of my answers.
2) Analyze the content to get a list of the most commonly used words and phrases, excluding stop words.
4) Import or create a function that can run a strict Japanese-language spell-check and grammar-check on the text.
5) Create visualizations of my most common used words/phrases and most common grammar mistakes with Tableau.
6) Look for any correlations between the number of "useful" votes an answer gets with the word count, specific words/phrases, or the presence/absence of spelling mistakes.

Extra Features:
1) Scrape the Japanese text from every non-Japanese "anchor" on the DMM uKnow website, associating each body of text with the nationality of the individual.
2) Analyze the content of the text, and group the results by nationality. Export the results to a CSV file.
3) Import the CSV data into Tableau and create visualizations to see if there are any correlations between nationality and specific Japanese word/phrase usage patterns or grammar mistakes.
4) Apply more rigorous regression statistics to the correlations.
