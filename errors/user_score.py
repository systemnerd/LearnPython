class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement
    
    def __repr__(self):
        return f"<User: {self.name}>"

def get_user_score(user: User):
    try:
        return perform_calculation(user.engagement_metrics)
    except KeyError:
        print(f"Incorrect values provided to our calculation function.")

def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2

def send_engagement_notification(user):
    print(f"Notification sent to {user}")

my_user = User('sample', {'click': 60, 'hits' : 100})
print(get_user_score(my_user))
send_engagement_notification(my_user)
