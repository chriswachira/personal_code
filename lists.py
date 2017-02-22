

class DataList():
    def __init__(self, size):
        self.size = size
    
    def get_list(self):
        count = 0
        data_list = []
        while count < self.size:
            data = input("Enter data: ")
            data_list.append(data)
            count += 1
        print("================")
        return data_list


class QueryList():
    def __init__(self, size):
        self.size = size
    
    def get_list(self):
        count = 0
        query_list = []
        while count < self.size:
            query = input("Enter query:")
            query_list.append(query)
            count += 1
        print("================")
        return query_list
