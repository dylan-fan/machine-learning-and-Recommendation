# author :dylan_fan;
# write at 2012/07/06; 

def Generate_Users2Items(trainfile):
    f= open(trainfile)
    users2items = {}
    for line in f.readlines():
        session = line.split(" ")
        userid = session[0]
        users2items[userid] = []
        for item in session[1:-1]:
            item = item.split(":")[1]
            users2items[userid].append(item)
    
    return users2items
        


class HeatSpearing:
    def __init__(self,users2items):
        self.users2items = {}
        self.items2users = {}
        self.users2items = users2items
        self.generate_item2users()
        self.users = self.users2items.keys()
        self.items = self.items2users.keys()
        
    def generate_item2users(self):
        
        for user, itemlist in self.users2items.items():
            for item in itemlist:
                self.items2users.setdefault(item,[])
                self.items2users[item].append(user)
        
        
    def get_top_items(self, userid):
        if userid not in self.users:
            print "%s is not verified" %(userid)
            return None
        recom_items = {}
        users_scores = {}
        userid_items = {}
        top_recommendation = []
#        users_scores[userid] = 1
        item_list = self.users2items.get(userid)
#        recom_items.setdefault((item, 0) for item in item_list)
        for item in item_list:
            userid_items[item] = 1.0
       
        for item , score in userid_items.items():
            userlist = self.items2users.get(item)
            for user in userlist:
                users_scores.setdefault(user,0)
                users_scores[user]+=1.0
        
        for user in users_scores.keys():
            users_scores[user] = float(users_scores.get(user))/ len(self.users2items.get(user))
        
        for user, score in users_scores.items():
            item_list = self.users2items.get(user)

            for item in item_list:
                recom_items.setdefault(item,0)
                recom_items[item] += score
            
        for item in recom_items.keys():
            recom_items[item] = float(recom_items.get(item)) / len(self.items2users.get(item))
        
        for item, score in recom_items.items():
            top_recommendation.append((score,item) if item not in self.users2items.get(userid))
        top_recommendation.sort(cmp=None, key=None, reverse=True)
        
        return top_recommendation

class Probs:
    def __init__(self,users2items):
        self.users2items = {}
        self.items2users = {}
        self.users2items = users2items
        self.generate_item2users()
        self.users = self.users2items.keys()
        self.items = self.items2users.keys()
        
    def generate_item2users(self):
        
        for user, itemlist in self.users2items.items():
            for item in itemlist:
                self.items2users.setdefault(item,[])
                self.items2users[item].append(user)
        
        
    def get_top_items(self, userid):
        if userid not in self.users:
            print "%s is not verified" %(userid)
            return None
        recom_items = {}
        users_scores = {}
        userid_items = {}
        top_recommendation = []
#        users_scores[userid] = 1
        item_list = self.users2items.get(userid)
#        recom_items.setdefault((item, 0) for item in item_list)
        for item in item_list:
            userid_items[item] = 1.0
       
        for item , score in userid_items.items():
            userlist = self.items2users.get(item)
            for user in userlist:
                users_scores.setdefault(user,0)
                users_scores[user]+= 1.0 / len(self.items2users.get(item))   
        
        for user, score in users_scores.items():
            item_list = self.users2items.get(user)

            for item in item_list:
                recom_items.setdefault(item,0)
                recom_items[item] += score / len(self.users2items.get(user))          
        
        
        for item, score in recom_items.items():
            top_recommendation.append((score,item) if item not in self.users2items.get(userid))
        top_recommendation.sort(cmp=None, key=None, reverse=True)
        
        return top_recommendation
    
if __name__ == '__main__':
    users2items = Generate_Users2Items("test_data/train_datas.txt")
    Heats_inst = HeatSpearing(users2items)
    Probs_inst = Probs(users2items)
    userid = "13347163898596348336390004807"
    print Heats_inst.get_top_items(userid)[:5]
    print Probs_inst.get_top_items(userid)[:5]
    
    
            
            
            
        
            
            
            
            
        
        
        
        
        
        
        
