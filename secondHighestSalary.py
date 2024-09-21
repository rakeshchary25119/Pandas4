import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    second_highest_salary = list(employee['salary'].unique())
    
    
    if len(second_highest_salary)<2:
        result = [None] 
    else:
        second_highest_salary.sort(reverse = True)
        result = [second_highest_salary[1]]
    return pd.DataFrame(result, columns = ['SecondHighestSalary'])