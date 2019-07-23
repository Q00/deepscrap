import json
import os

 #Edit right side
def replaceRight(original, old, new, count_right):
    repeat=0
    text = original
    
    count_find = original.count(old)
    if count_right > count_find : # 바꿀 횟수가 문자열에 포함된 old보다 많다면
        repeat = count_find # 문자열에 포함된 old의 모든 개수(count_find)만큼 교체한다
    else :
        repeat = count_right # 아니라면 입력받은 개수(count)만큼 교체한다

    for _ in range(repeat):
        find_index = text.rfind(old) # 오른쪽부터 index를 찾기위해 rfind 사용
        text = text[:find_index] + new + text[find_index+1:]
    
    return text


def one_user_one_json():

    name = input()

    #Get the list of file name 
    file_list = os.listdir('/Users/junha_lee/Desktop/PredictAttacks/Crawling/Tweets/UserTweet/'+name)

    real_list = []

    for i in range(1, len(file_list)):
    	if name in file_list[i] : real_list.insert(i,file_list[i])

    filenames = real_list

    #Just Merge
    with open('/Users/junha_lee/Desktop/PredictAttacks/Crawling/Tweets/UserTweet_json/'+name+'.json','w') as outfile:
    	for fname in filenames:
    		with open(fname) as infile:
    			outfile.write(infile.read()+',')

    #Transforming format
    file_ = open('/Users/junha_lee/Desktop/PredictAttacks/Crawling/Tweets/UserTweet_json/'+name+'.json','r')

    replace1 = file_.readline().replace('{','[{',1)
    replace2 = replaceRight(replace1,',',']',1)

    #Save as complete json format
    with open('/Users/junha_lee/Desktop/PredictAttacks/Crawling/Tweets/UserTweet_json/'+name+'.json','w') as outfile:
    	outfile.write(replace2)


if __name__ == '__main__':
	one_user_one_json()
