# importing the libraries 
from bs4 import BeautifulSoup 
import requests 
  
# creating function 
def scrape_info(url): 
      
    # getting the request from url 
    r = requests.get(url) 
      
    # converting the text 
    s = str(BeautifulSoup(r.text, "html.parser"))

    # f = open('demo.txt', 'w')

    print(s)

    # f.write(str(s))

    # f.close()
      
    # finding meta info for title 
    title = s.find("span", class_="watch-title").text.replace("\n", "") 
      
    # finding meta info for views 
    views = s.find("div", class_="watch-view-count").text 
      
    # finding meta info for likes 
    likes = s.find("span", class_="like-button-renderer").span.button.text 
      
    # saving this data in dictionary 
    data = {'title':title, 'views':views, 'likes':likes} 
      
    # returning the dictionary 
    return data 
  
# main function 
if __name__ == "__main__": 
      
    # URL of the video 
    url ="https://www.youtube.com/watch?time_continue=17&v=2wEA8nuThj8"
      
    # calling the function 
    data = scrape_info(url) 
      
    # printing the dictionary 
    print(data) 