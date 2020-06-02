import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

data = pd.read_csv(r'review_link.csv', engine = 'python')
data['movie_title'] = [title.replace('<U+00A0>', '') for title in data['movie_title']]

data = data[~data['movie_title'].duplicated()][:50]
data.set_index(pd.Index(list(range(50))), inplace = True)

with open('./movie review/movie_review1.txt', 'w', encoding='utf-8') as f:
    for i in range(10):
        f.write('<Movie title is ' + data['movie_title'][i] + '>' + '\n')
        total_url = data['review_link'][i]
        for j in range(4):
            if j == 0:
                r = requests.get(total_url)
            else:
                r = requests.post(url, {'User-Agent': 'Mozila/5.0'})
            broth = BeautifulSoup(r.text, "lxml")
            for item in broth.select(".review-container"):
                review_content = item.select_one(".text").text
                review_date = item.select_one(".review-date").text
                # print(review_date)
                f.write(review_date + '\n')
                try:
                    review_score = item.select_one('div.ipl-ratings-bar span > span:nth-child(2)').text
                except:
                    pass
                try:
                    f.write('평점은 {}점'.format(review_score))
                    f.write('\n')
                except:
                    pass
                f.write(review_content + '\n')
            my_url = broth.select_one('div.load-more-data').attrs['data-key']
            url = total_url + '&ref_=' + 'undefined&paginationKey=' + my_url
            url = url.replace('reviews?sort', 'reviews/_ajax?sort')

        f.write('\n')

print("movie review1 is finished.")

with open('./movie review/movie_review2.txt', 'w', encoding='utf-8') as f:
    for i in range(10, 20):
        f.write('<Movie title is ' + data['movie_title'][i] + '>' + '\n')
        total_url = data['review_link'][i]
        for j in range(4):
            if j == 0:
                r = requests.get(total_url)
            else:
                r = requests.post(url, {'User-Agent': 'Mozila/5.0'})
            broth = BeautifulSoup(r.text, "lxml")
            for item in broth.select(".review-container"):
                review_content = item.select_one(".text").text
                review_date = item.select_one(".review-date").text
                # print(review_date)
                f.write(review_date + '\n')
                try:
                    review_score = item.select_one('div.ipl-ratings-bar span > span:nth-child(2)').text
                except:
                    pass
                try:
                    f.write('평점은 {}점'.format(review_score))
                    f.write('\n')
                except:
                    pass
                f.write(review_content + '\n')
            my_url = broth.select_one('div.load-more-data').attrs['data-key']
            url = total_url + '&ref_=' + 'undefined&paginationKey=' + my_url
            url = url.replace('reviews?sort', 'reviews/_ajax?sort')

        f.write('\n')

print("movie review2 is finished.")

with open('./movie review/movie_review3.txt', 'w', encoding='utf-8') as f:
    for i in range(20, 30):
        f.write('<Movie title is ' + data['movie_title'][i] + '>' + '\n')
        total_url = data['review_link'][i]
        for j in range(4):
            if j == 0:

                r = requests.get(total_url)
            else:
                r = requests.post(url, {'User-Agent': 'Mozila/5.0'})
            broth = BeautifulSoup(r.text, "lxml")
            for item in broth.select(".review-container"):
                review_content = item.select_one(".text").text
                review_date = item.select_one(".review-date").text
                # print(review_date)
                f.write(review_date + '\n')
                try:
                    review_score = item.select_one('div.ipl-ratings-bar span > span:nth-child(2)').text
                except:
                    pass
                try:
                    f.write('평점은 {}점'.format(review_score))
                    f.write('\n')
                except:
                    pass
                f.write(review_content + '\n')
            my_url = broth.select_one('div.load-more-data').attrs['data-key']
            url = total_url + '&ref_=' + 'undefined&paginationKey=' + my_url
            url = url.replace('reviews?sort', 'reviews/_ajax?sort')

        f.write('\n')

print("movie review3 is finished.")

with open('./movie review/movie_review4.txt', 'w', encoding='utf-8') as f:
    for i in range(30, 40):
        f.write('<Movie title is ' + data['movie_title'][i] + '>' + '\n')
        total_url = data['review_link'][i]
        for j in range(4):
            if j == 0:
                r = requests.get(total_url)
            else:
                r = requests.post(url, {'User-Agent': 'Mozila/5.0'})
            broth = BeautifulSoup(r.text, "lxml")
            for item in broth.select(".review-container"):
                review_content = item.select_one(".text").text
                review_date = item.select_one(".review-date").text
                # print(review_date)
                f.write(review_date + '\n')
                try:
                    review_score = item.select_one('div.ipl-ratings-bar span > span:nth-child(2)').text
                except:
                    pass
                try:
                    f.write('평점은 {}점'.format(review_score))
                    f.write('\n')
                except:
                    pass
                f.write(review_content + '\n')
            my_url = broth.select_one('div.load-more-data').attrs['data-key']
            url = total_url + '&ref_=' + 'undefined&paginationKey=' + my_url
            url = url.replace('reviews?sort', 'reviews/_ajax?sort')

        f.write('\n')

print("movie review4 is finished.")

with open('./movie review/movie_review5.txt', 'w', encoding='utf-8') as f:
    for i in range(40, 50):
        f.write('<Movie title is ' + data['movie_title'][i] + '>' + '\n')
        total_url = data['review_link'][i]
        for j in range(4):
            if j == 0:
                r = requests.get(total_url)
            else:
                r = requests.post(url, {'User-Agent': 'Mozila/5.0'})
            broth = BeautifulSoup(r.text, "lxml")
            for item in broth.select(".review-container"):
                review_content = item.select_one(".text").text
                review_date = item.select_one(".review-date").text
                # print(review_date)
                f.write(review_date + '\n')
                try:
                    review_score = item.select_one('div.ipl-ratings-bar span > span:nth-child(2)').text
                except:
                    pass
                try:
                    f.write('평점은 {}점'.format(review_score))
                    f.write('\n')
                    f.write(review_content + '\n')
                except:
                    pass

            my_url = broth.select_one('div.load-more-data').attrs['data-key']
            url = total_url + '&ref_=' + 'undefined&paginationKey=' + my_url
            url = url.replace('reviews?sort', 'reviews/_ajax?sort')

        f.write('\n')

print("movie review5 is finished.")


def get_title(file, title_list):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.replace('\n', '')
            if line.startswith('<Movie title is'):
                title = line
                title = title.replace('<Movie title is ', '')
                title = title.replace('>', '')
                title_list.append(title)


def get_score(file, score_list):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.replace('\n', '')
            if line.startswith('평점은 '):
                score = line
                score = score.replace('평점은 ', '')
                score = score.replace('점', '')
                score_list.append(score)


def get_review(file, review_list):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.replace('\n', '')
            if len(line) > 30 and not line.endswith('>'):
                review = line
                review_list.append(review)


def get_date(file, length):
    date_list = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                date = re.search(r'\d+\s\w{3,}\s\d{4}', line)
                date = date.group()
                if len(date) > 10 and line.endswith('\n'):
                    date_list.append(date)
            except:
                pass
    if len(date_list) > length:
        date_list = date_list[:length]
    return date_list


def get_final_review(file, original_dictionary, reviews_date_list):
    with open(file, 'w', encoding = 'utf-8') as f:
        j = 0
        for index, date in enumerate(reviews_date_list):
            if index % 100 == 0:
                review_start_date = date
                if index != 0:
                    f.write('\n')
                f.write('영화제목: {}'.format(original_dictionary['title'][j]) + '\n')
                j = j+1
            try:
                sub = int(str(pd.to_datetime(date) - pd.to_datetime(review_start_date))[:2])
                if sub <= 7:
                    f.write('평점: {}'.format(original_dictionary['score'][index]) + '\t')
                    f.write('리뷰: {}'.format(original_dictionary['review'][index]))
                    f.write('\n')
            except:
                pass

movie1 = {'title':[], 'score':[], 'review':[]}
get_title('./movie review/movie_review1.txt', movie1['title'])
get_score('./movie review/movie_review1.txt', movie1['score'])
get_review('./movie review/movie_review1.txt', movie1['review'])
date_list = get_date('./movie review/movie_review1.txt', length = 1000)
get_final_review('final_movie1.txt', movie1, date_list)

movie2= {'title':[], 'score':[], 'review':[]}
get_title('./movie review/movie_review2.txt', movie2['title'])
get_score('./movie review/movie_review2.txt', movie2['score'])
get_review('./movie review/movie_review2.txt', movie2['review'])
date_list = get_date('./movie review/movie_review2.txt', length = 1000)
get_final_review('final_movie2.txt', movie2, date_list)

movie3= {'title':[], 'score':[], 'review':[]}
get_title('./movie review/movie_review3.txt', movie3['title'])
get_score('./movie review/movie_review3.txt', movie3['score'])
get_review('./movie review/movie_review3.txt', movie3['review'])
date_list = get_date('./movie review/movie_review3.txt', length = 1000)
get_final_review('final_movie3.txt', movie3, date_list)

movie4= {'title':[], 'score':[], 'review':[]}
get_title('./movie review/movie_review4.txt', movie4['title'])
get_score('./movie review/movie_review4.txt', movie4['score'])
get_review('./movie review/movie_review4.txt', movie4['review'])
date_list = get_date('./movie review/movie_review4.txt', length = 1000)
get_final_review('final_movie4.txt', movie4, date_list)

movie5= {'title':[], 'score':[], 'review':[]}
get_title('./movie review/movie_review5.txt', movie5['title'])
get_score('./movie review/movie_review5.txt', movie5['score'])
get_review('./movie review/movie_review5.txt', movie5['review'])
date_list = get_date('./movie review/movie_review5.txt', length = 1000)
get_final_review('final_movie5.txt', movie5, date_list)

print("All finished.")