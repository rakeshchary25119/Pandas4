import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N <= len(employee) and N > 0:
        
        return employee
    else:
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})