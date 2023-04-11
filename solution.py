import pandas as pd
import numpy as np
from scipy.stats import pareto, cauchy, norm, ttest_ind, ks_2samp, mannwhitneyu, permutation_test, cramervonmises_2samp

chat_id = 322172960 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return ks_2samp(x, y, alternative="greater").pvalue < 0.01 # Ваш ответ, True или False
    #return cramervonmises_2samp(x, y).pvalue < 0.01 # Ваш ответ, True или False
