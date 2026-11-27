# N40: Markov链模型中，状态空间定义为缓存中对象的集合，状态转移概率 P_{S→S'} 由新到达请求的对象ID和LRU驱逐策略决定；稳态分布 π(S) 满足 π 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

Markov链模型中，状态空间定义为缓存中对象的集合，状态转移概率 P_{S→S'} 由新到达请求的对象ID和LRU驱逐策略决定；稳态分布 π(S) 满足 π P = π，命中率 H = Σ_S π(S) * [1 if request_object in S else 0]；对于10万对象，状态空间爆炸，需采用Mean-Field近似或蒙特卡洛模拟求解。

## Corrected Claim

Markov链模型中，状态空间定义为缓存中对象的集合，状态转移概率 P_{S→S'} 由新到达请求的对象ID和LRU驱逐策略决定；稳态分布 π(S) 满足 π P = π，命中率 H = Σ_S π(S) * [1 if request_object in S else 0]；对于10万对象，状态空间爆炸，需采用Mean-Field近似或蒙特卡洛模拟求解。

## Evidence

先验知识/题面给定，逻辑校验通过：Markov链建模LRU缓存是标准理论框架，状态空间随对象数指数爆炸需近似求解符合计算复杂性常识，公式定义自洽。

## Search Query

Markov chain LRU cache steady state distribution mean field approximation
