# dat550-project-g5
DAT550 final project of Group 5

Main project on jupyter notebooks, all found under notebook folder.

Three sets of notebooks. General pre-processing of non facebook status files in 'Project DAT 550.ipynb'. All CSV's fed to it in data folder.

LSH investigation to assess BuzzFeed's original work in 'LSH_investigation.ipynb'. It used the CSV file 'oneline_status_matrix.csv', which had to be shortened significantly due to githubs 100 MB upload limit. Current size is 13 MB, but original file was 500MB. The method to recreate is inside the notebook, but commented out. The shortened version is left as an example.

All other notebooks related to differing ML models training and analysis. Note 'img_tools.py' is a python script file also used by these notebooks.

Statuses folder is the set of all statuses that went into creating 'oneline_status_matrix.csv' and other CSV files used in some of the ML models. Taken directly from BuzzFeed's repository.

Original BuzzFeed article that requisitioned the research: https://www.buzzfeednews.com/article/craigsilverman/inside-the-partisan-fight-for-your-news-feed

Original github repository of this research that provided all data for this project: https://github.com/BuzzFeedNews/2017-08-partisan-sites-and-facebook-pages
