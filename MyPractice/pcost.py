import csv
def calculate_cost_shares(filepath):
    total_cost=0.0

    with open(filepath,'r') as f:
        csv_reader=csv.reader(f)
        
        header=next(csv_reader)
        
        for row in csv_reader:      
            no_of_shares=int(row[1])
            
            price=float(row[2])
            
            total_cost=total_cost+no_of_shares*price
        return total_cost
        

print(calculate_cost_shares("/workspaces/python-mastery/Data/portfolio.csv"))
    
