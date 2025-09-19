#Spam (or junk email) costs U.S. organizations billions of dollars a year in spam-prevention software, equipment, network resources,
#bandwidth, and lost productivity. Research online some of the most common spam email messages and words. Create a list of 30 words and
#phrases commonly found in spam messages. Write an application in which the user enters an email message. Then your application will scan
#the message for each of the 30 keywords or phrases. For each occurrence of one of these within the message, add a point to the message's
#"spam score". Next, rate the likelihood that the message is spam, based on the number of points received. Display the user's spam score,
#the likelihood message that it is spam, and the words/phrases which caused it to be spam.

#List of common spam words/phrases (https://youtu.be/9sQcROW4LZQ?si=iW9Bix4H4T0rpO6h)
SPAM_KEYWORDS = ["free", "winner", "win", "cash", "act now", "buy now", "limited time", "order now", "free trial", "click here",
                 "get paid", "no fees", "giveaway", "make money now", "this is not spam", "prize", "money back guarantee", "sales",
                 "follow this link", "save up", "one time deal", "act fast","buy more", "deals", "risk-free", "pure profit",
                 "offer expires", "miracle", "debt free", "call now", "#1", "make a quick buck"
                 ]

#Code that sets the score for spam and calculates it
def calculate_spam_score(message, spam_keywords):
    message_lower = message.lower()
    matched_keywords = []
    score = 0
    for keyword in spam_keywords:
        if keyword in message_lower:
            score += 1
            matched_keywords.append(keyword)
    return score, matched_keywords

#Code that sections the values of the spam score into different tiers of results.
def rate_spam_likelihood(score):
    if score <= 2:
        return "This is most likely not spam mail."
    elif score <= 5:
        return "This might be spam mail."
    elif score <= 10:
        return "This is likely to be spam mail."
    else:
        return "This is highly likely to be spam mail."

 #Code asking for the user to input the email they have gotten
def main():
    print("=== Joel's Amazing Spam Detector 1997===\n")
    message = input("Please enter your email message to calculate if it is spam or not: \n\n")

#taking the words from the email and calculating the score gained
    score, matched = calculate_spam_score(message, SPAM_KEYWORDS)
    rating = rate_spam_likelihood(score)

#printing the results for the user based on the calculation
    print("\n=== Joel's Amazing Spam Analysis Result ===")
    print(f"Spam Score: {score}")
    print(f"Likelihood: {rating}")
    print(f"Matched Spam Words/Phrases: {', '.join(matched) if matched else 'None'}")


if __name__ == "__main__":
    main()