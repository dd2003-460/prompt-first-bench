# N309: 将95%频率主义置信水平映射到贝叶斯后验概率阈值时，隐含假设了均匀先验 $P(H)=0.5$ 且似然函数对称。若先验 $P(H)$ 偏离0.5，则维持相同错误率

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88

## Claim

将95%频率主义置信水平映射到贝叶斯后验概率阈值时，隐含假设了均匀先验 $P(H)=0.5$ 且似然函数对称。若先验 $P(H)$ 偏离0.5，则维持相同错误率（Type I + Type II error rate）所需的后验阈值 $\theta_{post}$ 需满足 $\theta_{post} = \frac{LR \cdot P(H)}{LR \cdot P(H) + P(\neg H)}$，其中 $LR$ 为观测数据的似然比。

## Corrected Claim

将95%频率主义置信水平映射到贝叶斯后验概率阈值时，隐含假设了均匀先验 $P(H)=0.5$ 且似然函数对称。若先验 $P(H)$ 偏离0.5，则维持相同错误率（Type I + Type II error rate）所需的后验阈值 $\theta_{post}$ 需满足 $\theta_{post} = \frac{LR \cdot P(H)}{LR \cdot P(H) + P(\neg H)}$，其中 $LR$ 为观测数据的似然比。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式是贝叶斯定理计算后验概率 $P(H|D)$ 的标准形式，其中 $LR = P(D|H)/P(D|\neg H)$，代入后得 $P(H|D) = \frac{LR \cdot P(H)}{LR \cdot P(H) + P(\neg H)}$，数学推导严谨且自洽。
