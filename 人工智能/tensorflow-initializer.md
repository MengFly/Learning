# tensorflow-initializer

+ 常量初始化
  + **tf.constant_initializer()**

+ 零初始化
  + **tf.zeros_initializer()**

+ 一初始化
  + **tf.ones_initializer()**

+ 截断正态分布的随机数，一般只需要设置stddev这一个参数就可以了

  + **tf.TruncatedNormal(stddev=0.01)**
  + **tf.truncated_normal_initializer(stddev=0.01)**

+ 标准正态分布的随机数

  + **tf.random_normal_initializer(mean, stddev, seed, dtype)** 

+ 均匀随机分布

  + **tf.random_uniform_initializer(minval, maxval, seed, dtype)**
  + **tf.RandomUniform()**

+ 均匀随机分布，不需指定最大最小值

  + **tf.uniform_unit_scaling_initializer(factor, seed)**
  + **tf.UniformUnitScaling()**

+ 生成正交矩阵的随机数，需要生成的参数是2维时，这个正交矩阵是由均匀分布的随机数矩阵经过[SVD](https://www.baidu.com/s?wd=SVD&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)分解而来

  + **tf.orthogonal_initializer()**
  + **tf.Orthogonal()**

+ Xavier uniform initializer 由一个均匀分布（uniform distribution)来初始化数据

  + **tf.glorot_uniform_initializer()**

    算法：$$limit = \sqrt{6/(fan\_in + fan\_out)}$$ 其中，fan_in 和fan_out 为输入单元节点数和输出单元节点数

+ Xavier normal initializer 由一个 truncated normal distribution来初始化数据

  + **tf.glorot_normal_initializer()**

    算法： $$stddev = \sqrt{ 2/ (fan\_in + fan\_out)}$$

+ 初始化为变尺度正太、均匀分布

  + **tf.variance_scaling_initializer(mode, distribution, seed, dtype)**
    +  **mood** : fan_in, fan_out, fan_avg , 控制计算 stddev
    + **distribution** : normal, uniform 截断正太分布Or均匀分布