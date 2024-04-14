import numpy as np
from population import Population
from sample import Sample

# 母集団のパラメータ
UNIFORM_LOW = -10
UNIFORM_HIGH = 10
POPULATION_SIZE = 100000

# 母集団を生成
POPULATION = Population(UNIFORM_LOW, UNIFORM_HIGH, POPULATION_SIZE)

# サンプルのパラメータ
SAMPLE_SIZE = 10
SAMPLE_NUM = 1000

def get_relative_error(experimental: float, theoretical: float) -> float:
    """
    2つの値の相対誤差を計算する。

    Args:
        experimental (float): 実験値
        theoretical (float): 理論値

    Returns:
        float: 相対誤差
    """
    return np.abs(experimental - theoretical) / theoretical

if __name__ == "__main__":    
    # 標本分散と不偏標本分散の平均値を計算
    sample_variance_average = 0
    unbiased_sample_variance_average = 0
    for _ in range(SAMPLE_NUM):
        s = Sample(POPULATION, SAMPLE_SIZE)
        sample_variance_average += s.get_variance()
        unbiased_sample_variance_average += s.get_unbiased_variance()
    sample_variance_average /= SAMPLE_NUM
    unbiased_sample_variance_average /= SAMPLE_NUM
    
    # 標本分散と不偏標本分散の相対誤差を計算
    sample_variance_error = get_relative_error(sample_variance_average, POPULATION.get_variance())
    unbiased_sample_variance_error = get_relative_error(unbiased_sample_variance_average, POPULATION.get_variance())
    
    # 結果を出力
    print(f"母分散：{POPULATION.get_variance():.2f}")
    print(f"標本分散の平均値：{sample_variance_average:.2f} (相対誤差：{sample_variance_error * 100:.2f}%)")
    print(f"不偏標本分散の平均値：{unbiased_sample_variance_average:.2f} (相対誤差：{unbiased_sample_variance_error * 100:.2f}%)")
