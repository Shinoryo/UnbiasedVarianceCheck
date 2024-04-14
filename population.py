import numpy as np

class Population:    
    def __init__(self, low: float, high: float, size: int) -> None:
        """
        Populationオブジェクトを初期化する。
        
        Args:
            low (float): 一様分布の下限
            high (float): 一様分布の上限
            size (int): 母集団のサンプルサイズ
        """
        self.population = np.random.uniform(low, high, size)
        self.mean = np.mean(self.population)
        self.variance = np.var(self.population)
        self.size = size
    
    def get_mean(self) -> float:
        """
        母集団の平均値を取得する。
        
        Returns:
            float: 母集団の平均値
        """
        return self.mean

    def get_variance(self) -> float:
        """
        母集団の分散を取得する。
        
        Returns:
            float: 母集団の分散
        """
        return self.variance
    
    def get_size(self) -> int:
        """
        母集団のサンプルサイズを取得する。
        
        Returns:
            int: 母集団のサンプルサイズ
        """
        return self.size

    def get_population(self) -> np.ndarray:
        """
        母集団のサンプルを取得する。
        
        Returns:
            numpy.ndarray: 母集団のサンプル
        """
        return self.population