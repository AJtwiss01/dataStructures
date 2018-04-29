def main():
    reviewFile = open('restaurant_reviews.txt')
    
    reviewCountDic = {}
    
    for line in reviewFile:
        line = line.strip()
        name , rating , comment = line.split(';')
        ratingValueCount = reviewCountDic.get(rating, 0)
        reviewCountDic[rating] = ratingValueCount + 1
    print(reviewCountDic)
        
    
main()