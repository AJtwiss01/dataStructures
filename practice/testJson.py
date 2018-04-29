import json

def main():
    inventoryFileName = "REID_1F_20171004.json"
    inventoryFile = open(inventoryFileName, 'r')
    
    inventoryData = json.loads(inventoryFile.read())
    contents = inventoryData['contents']
    
    for row in contents:
##        print(row['row'])
##        print(row['slots'])
        for slot in row['slots']:
            print('{}{}: {}'.format(row['row'],slot['slot_number'],slot['item_name']))
        
main()