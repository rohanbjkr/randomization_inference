import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

def randomization_inference(df, y_col, t_col, beta, simulations=1000, seed=2022, p_original=None):
    """
    Performs randomization inference to calculate a p-value.

    Args:
        df (pandas.DataFrame): The dataframe containing the data.
        y_col (str): The name of the outcome variable column.
        t_col (str): The name of the treatment variable column.
        beta (float): The observed treatment effect (beta) from the original regression.
        simulations (int, optional): The number of simulations to perform. Defaults to 1000.
        seed (int, optional): The random seed for reproducibility. Defaults to 2022.
        p_original (float, optional): The p-value from the original regression. Defaults to None.

    Returns:
        tuple: A tuple containing the p-value from the randomization inference and a dataframe of t-values.
    """
    np.random.seed(seed)
    t_values = []

    for i in range(1, simulations + 1):
        shuffled_t = np.random.permutation(df[t_col])
        temp_df = df.copy() # Avoid modifying original DataFrame
        temp_df[t_col] = shuffled_t
        ols = smf.ols(formula=f'{y_col} ~ {t_col}', data=temp_df).fit()
        t_values.append(ols.params[t_col])
        if i % 100 == 0:
            print(f'{i} out of {simulations} simulations completed')

    t_results = pd.DataFrame({'iteration': range(1, simulations + 1), 't_value': t_values})
    p_value = round(np.mean(np.abs(t_results['t_value']) >= abs(beta)), 3)

    if p_original is not None:
        print(f'P-value from original regression: {p_original}')
    print(f'P-value from randomization inference: {p_value}')

    return p_value, t_results