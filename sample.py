import numpy as np
from population import Population

class Sample:
    def __init__(self, population: Population, size: int) -> None:
        """
        Sampleオブジェクトを初期化する。
        
        Args:
            population (Population): 母集団オブジェクト
            size (int): サンプルサイズ
        """
        self.sample = np.random.choice(population.get_population(), size)
        self.mean = np.mean(self.sample)
        self.variance = np.var(self.sample)
        self.size = size
    
    def get_mean(self) -> float:
        """
        サンプルの平均値を取得する。
        
        Returns:
            float: サンプルの平均値
        """
        return self.mean

    def get_variance(self) -> float:
        """
        サンプルの分散を取得する。
        
        Returns:
            float: サンプルの分散
        """
        return self.variance
    
    def get_unbiased_variance(self) -> float:
        """
        不偏分散を取得する。
        
        Returns:
            float: 不偏分散
        """
        return self.variance * self.size / (self.size - 1)

    def get_size(self) -> int:
        """
        サンプルのサイズを取得する。
        
        Returns:
            int: サンプルのサイズ
        """
        return self.size

    def get_sample(self) -> np.ndarray:
        """
        サンプルを取得する。
        
        Returns:
            numpy.ndarray: サンプル
        """
        return self.sample