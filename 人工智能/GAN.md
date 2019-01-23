# GAN

+ 两个网络都必须进行批量归一化。
+ 采用完全隐藏的连接层不是一个好主意。
+ 避免池化（pooling），简单地跨越你的卷积
+ ReLU 激活是你的朋友（几乎总是）
+ 单边标签平滑：这一点很简单：只需将你的鉴别器目标输出从 [0 = 假图像，1 = 真图像] 切换到 [0 = 假图像，0.9 =真图像]。是的，这改善了训练。 

## DCGAN

文章链接：

-  [https://arxiv.org/abs/1511.06434 ](https://arxiv.org/abs/1511.06434 )

## 改进的DCGAN

文章链接：

+ [https://arxiv.org/abs/1606.03498](https://arxiv.org/abs/1606.03498)

## 条件GAN

文章链接：

+ [https://arxiv.org/abs/1411.1784](https://arxiv.org/abs/1411.1784)

+ 学习画什么和在哪里画

  > （a） 你想要得到的图像内容是什么样，
  >
  > （b）通过边界框/地标来告知元素的位置 

  - [https://arxiv.org/abs/1610.02454](https://arxiv.org/abs/1610.02454)
  - [https://github.com/reedscot/nips2016](https://github.com/reedscot/nips2016)

## StackGAN

> 同时使用2 个 GAN 来提高图像的质量：Stage-I 和 Stage-II。Stage-I 用于获取包含图像「一般」构想的低分辨率图像

文章链接：

+ https://arxiv.org/abs/1612.03242 
+ https://github.com/hanzhanggit/StackGAN 

## Wasserstein GAN

> 改变损失函数以包含 Wasserstein 距离。结果，WassGAN 具有与图像质量相关的损失函数。此外，训练稳定性也提高了，而且不依赖于架构。 

文章链接：

+ https://arxiv.org/abs/1701.07875 

## 链接

+ GAN 应用于视频：https://github.com/SKTBrain/DiscoGAN
+ 图像完成：https://arxiv.org/abs/1609.04802
+ GAN + 可变性 AutoEncoder 混合：https://github.com/junyanz/iGAN
+ 向 GAN 添加一个编码器以重建样本：https://phillipi.github.io/pix2pix/
+ 图像到图像的翻译：https://ishmaelbelghazi.github.io/ALI/
+ 交互式图像生成：https://arxiv.org/abs/1512.09300
+ 使用 GAN 增加图像质量：https://bamos.github.io/2016/08/09/deep-completion/
+ 将鞋子变成等价的包（DiscoGAN）：http://web.mit.edu/vondrick/tinyvideo/
+ 更广泛的研究列表，请查看此链接：https://github.com/zhangqianhui/AdversarialNetsPapers。
+ 此外，在这个 repo（https://github.com/wiseodd/generative-models）中，你会发现 Tensorflow 和 Torch 中的各种 GAN 实现。

 

 

 

 

 
