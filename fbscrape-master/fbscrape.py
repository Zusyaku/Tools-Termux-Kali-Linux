from db.database import Database
from models.scrape_model import ScrapeModel
from facebook_scraper import get_posts
import json

def main():
    # Load list of target from targets.json file
    targets = loadTargets()
    scrapeData = []
    for target in targets['targets']:
        page = 1
        items = []

        while (True):
            isComplete = False
            # Fetching post per page, it will return 1 data per page
            for post in get_posts(target['username'], page=page):
                if len(items) < target['count']:
                    items.append(ScrapeModel(
                        post['post_id'],
                        post['post_text'],
                        target['username'],
                        post['username'],
                        post['time'],
                        post['likes'],
                        post['comments'],
                        post['shares']
                    ))
                    print("Scrape Data: {} / Count: {}/{}".format(target['username'], len(items), target['count']))
                else:
                    isComplete = True
                    break
            page += 1
            if isComplete:
                break

        # Merge result to scrapeData
        scrapeData.extend(items)
    
    # Add data to  database
    DB = Database()
    for x in range(0, len(scrapeData)):
        data = scrapeData[x]
        print("Inserting scrape data {}... {}/{}".format(data.username, x+1, len(scrapeData)))
        ## Check data first before insert
        if (DB.postExists(data.postId) == False):
            DB.insert(data)
        else:
            print("Post ID {} already exists".format(data.postId))

# Load target from [targets.json] configuration file
def loadTargets():
    file = open('config/targets.json')
    data = json.load(file)
    return data

if __name__ == "__main__":
    main()