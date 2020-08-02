from requests import get
from bs4 import BeautifulSoup
from email.message import EmailMessage
from smtplib import SMTPAuthenticationError, SMTP_SSL

# sites to read news from
site1 = 'https://theverge.com/tech'
site2 = 'https://techcrunch.com'
site3 = 'https://developer-tech.com'
site4 = 'https://news.ycombinator.com'

# List to store titles and links
mailData = []


def getNews(site):
    data = get(site).text

    soup = BeautifulSoup(data, 'html.parser')

    try:
        print('News from:', site)

        links = soup.findAll('a', {'data-analytics-link': 'article'})
        for link in links:
            # saving data to the list
            mailData.append(link.text)
            mailData.append(link.get('href'))
            mailData.append('')

        links = soup.findAll('a', {'class': 'post-block__title__link'})
        for link in links:
            # saving data to the list
            mailData.append(link.text)
            mailData.append(link.get('href'))
            mailData.append('')

        links = soup.findAll('a', {'rel': 'bookmark'})
        for link in links:
            # saving data to the list
            mailData.append(link.text)
            mailData.append(link.get('href'))
            mailData.append('')

        links = soup.findAll('a', {'class': 'storylink'})
        for link in links:
            # saving data to the list
            mailData.append(link.text)
            mailData.append(link.get('href'))
            mailData.append('')

    except Exception as e:
        print(e)
        exit()


def sendMail(stringMessge):
    server = SMTP_SSL('smtp.gmail.com', 465)


    # add data
    fromMail = '' 
    toMail = ''
    password = ''

    try:
        server.login(fromMail, password)

    except SMTPAuthenticationError:
        print('\nCan\'t login')
        exit()

    msg = EmailMessage()

    msg['Subject'] = 'Daily news from your Bot!'
    message = stringMessge

    msg['From'] = fromMail
    msg['To'] = toMail

    msg.set_content(message)
    server.send_message(msg)
    server.quit()
    print('Done!')
    exit()


def converttostr(input_seq, seperator):
    # Join all the strings in list
    final_str = seperator.join(input_seq)

    print(final_str)

    # send string to function to send mail
    # sendMail(final_str)


getNews(site1)

getNews(site2)

getNews(site3)

getNews(site4)

converttostr(mailData, '\n')
