import requests
import telegram
from bs4 import BeautifulSoup
from telegram.ext import Updater
import imdb


def PopularMovie(strL, id, bot, year):
    for str in strL:
        print year
        if 1918<year<2017:
            print "y"
            url_imdb = "http://www.imdb.com/search/title?at=0&genres="+str+"&sort=moviemeter,asc&year="+repr(year)
        else:
            url_imdb = "http://www.imdb.com/genre/" + str
        print url_imdb
        r_imdb = requests.get(url_imdb)
        print r_imdb
        soup_imdb = BeautifulSoup(r_imdb.text, 'html.parser')
        list_imdb = soup_imdb.find_all('td', {"class":"title"})
        # print list_imdb[0].contents[3].get_text()
        for movie in list_imdb:
            print movie.contents[3].get_text()


def TopMovie(strL, id, bot):
    ia = imdb.IMDb()
    for str in strL:
        url= "http://goodmovieslist.com/best-movies/best-" + str+"-movies.html"
        print url
        r = requests.get(url)
        print r
        soup = BeautifulSoup(r.text, 'html.parser')
        result=""
        list  = soup.find_all('span', {"class":"list_movie_localized_name Undefined"})
        for movie in list:
            #s_result = ia.search_movie(movie.get_text())
            #print type(s_result[0])
            #ia.update(s_reult[0])
            #print "x"
            #print s_result['rating']
            result+=movie.get_text()
            result+="\n"
        bot.sendMessage(chat_id=id, text=result)            
        
    
    
def preProcess(str):
    arr = str.split()
    print arr
    genre=[]
    year=0
    i=0
    isPopular=False
    for s in arr:
        s=s.lower()
        print s
        if s=="popular":
            isPopular=True
        if s in movie_tag:
            genre.append(s)
        if s in emoji:
            genre.append(emoji[s])
        try: 
            year = int(s)
            isPopular=True
        except ValueError:
            pass
    print isPopular
    l = []
    print "x"
    l.append(isPopular)
    l.append(genre)
    l.append(year)
    print "x"
    return l

def checkMovie(str, id, bot):
    str = preProcess(str)
    print str[0]
    if str[0] is True:
        PopularMovie(str[1], id, bot, str[2])
    else:
        TopMovie(str[1], id, bot)
    

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')


def echo(bot, u):
    checkMovie(u.message.text, u.message.chat_id,bot)
    #bot.sendMessage(update.message.chat_id, text=update.message.text)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


#bot = telegram.Bot(token='213919768:AAE1se41DEoVemNTViEAW5SS_qfijxyOnrk')
#print(bot.getMe())

emoji={u"\u2764":"romance", u"\U0001f61e":"inspirational"}

ia = imdb.IMDb()
movie_tag=["adventure", "comedy", "fantasy", "action", "scifi", "noir", "crime", "thriller", "suspense","horror", "romance", "muiacal", "film-noir", "war", "drama", "biography", "history", "mystery"]
#count = 6
# Create the EventHandler and pass it your bot's token.
updater = Updater("213919768:AAE1se41DEoVemNTViEAW5SS_qfijxyOnrk")

#updater.setWebhook("topmovielist.herokuapp.com")
    # Get the dispatcher to register handlers
dp = updater.dispatcher

    # on different commands - answer in Telegram
dp.addTelegramCommandHandler("start", start)
dp.addTelegramCommandHandler("help", help)

    # on noncommand i.e message - echo the message on Telegram
dp.addTelegramMessageHandler(echo)

    # log all errors
dp.addErrorHandler(error)

    # Start the Bot
updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
updater.idle()
        
     
