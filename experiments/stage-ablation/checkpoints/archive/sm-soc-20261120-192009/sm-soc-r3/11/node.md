# N118: 随机偏好噪声的演化衰减项：在长期演化均衡中，观察到的噪声方差 $\sigma_{obs}^2$ 是初始噪声 $\sigma_{init}^2$ 经过定向压力筛选

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

随机偏好噪声的演化衰减项：在长期演化均衡中，观察到的噪声方差 $\sigma_{obs}^2$ 是初始噪声 $\sigma_{init}^2$ 经过定向压力筛选后的结果，公式为 $\sigma_{obs}^2 = \sigma_{init}^2 * e^{-\lambda_{selection} * T_{market}}$。若 $T_{market}$ 较短（如48小时），衰减项 $e^{-\lambda_{selection} * T_{market}} \approx 1$，意味着短期内随机噪声主导行为；若 $T_{market}$ 较长，定向压力将显著降低噪声，使行为趋同于理性基准。

## Corrected Claim

在长期演化均衡中，观察到的噪声方差 $\sigma_{obs}^2$ 可能随时间 $T_{market}$ 衰减，其具体形式（如指数衰减 $\sigma_{obs}^2 = \sigma_{init}^2 e^{-\lambda T}$）取决于具体的选择压力模型和动力学假设，并非通用物理定律；短期内噪声主导，长期内行为趋同于理性基准的定性结论在多数选择模型中成立。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的三个独立变量/条件：初始噪声定义、时间参数计算示例、以及基于衰减结果的临界判断条件。三者逻辑独立，无重复或矛盾，且完整覆盖了父节点中涉及的量化定义、参数计算和阈值判断。）

## Retrieval Sources

- {'url': 'https://blog.csdn.net/Logic_9527/article/details/164187740&rut=9e1cfc2ff8b69f0b55b1d27311a6062ac99738d2d114430ea7495f421f7e4cf0', 'type': 'ddg', 'title': 'Icml 2026，固定预算噪声演化策略中的深度与保真度权衡-csdn博客'}
- {'url': 'https://www.alphaxiv.org/zh/overview/2607.17255&rut=11c4e078afbbe53a99ab0f7164fe50f54e227f8fc0d8b57e7e26d5d44ac4dae2', 'type': 'ddg', 'title': '具有小且渐近粗糙噪声的随机演化方程的长时间占据测度的大偏差 | alphaXiv'}
- {'url': 'https://steven-yl.github.io/mywebsite/%E6%89%A9%E6%95%A3%E6%A8%A1%E5%9E%8B%E4%B8%AD%E7%9A%84%E5%99%AA%E5%A3%B0%E8%B0%83%E5%BA%A6noise-schedule-%E5%AE%8C%E6%95%B4%E7%90%86%E8%AE%BA%E7%AC%94%E8%AE%B0/&rut=e6dd64b334573513864881efad0179cedb1851611a69febd120504a424f5a2de', 'type': 'ddg', 'title': '扩散模型中的噪声调度（Noise Schedule）—— 完整理论笔记'}
