from lists import DataList
from lists import QueryList
import datetime
    
def search(data_list, query_list):
#     now = datetime.datetime.now()
    for i in query_list:
        for j in data_list:
            if i == j:
                print(i , "---" , j)
                print("found")
                break
#                 return "true" + str(now)
        else:
            print("not found")
            break
#                 return "false" + str(now)
        
            
if __name__ == "__main__":
    nums = input("Enter, respectively, integer of size of data list and\nsize of query list separated by a space: ").split()
    
    dataList = DataList(int(nums[0]))
    queryList = QueryList(int(nums[1]))
    
#     print(dataList.get_list())
#     print(queryList.get_list())
    search(dataList.get_list(), queryList.get_list())
    