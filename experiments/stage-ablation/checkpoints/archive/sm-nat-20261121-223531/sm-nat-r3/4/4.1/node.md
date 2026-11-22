# N16: LRU缓存中，对象更新导致的字节命中率折损因子 $D_{LRU}$ 定义为 $1 - \frac{\text{更新导致的无效缓存占用比例}}{\text{总缓存

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

LRU缓存中，对象更新导致的字节命中率折损因子 $D_{LRU}$ 定义为 $1 - \frac{\text{更新导致的无效缓存占用比例}}{\text{总缓存容量}}$。在稳态下，若更新率 $\lambda_{upd}=1\%$/天，且更新对象在缓存中的平均驻留时间 $T_{res}$ 服从指数分布，则因更新而提前淘汰（或需重写）的字节占比近似为 $1 - e^{-\lambda_{upd} T_{res}}$。对于热门对象，$T_{res}$ 较大，折损显著；对于冷门对象，$T_{res} \approx 0$，折损可忽略。

## Corrected Claim

LRU缓存中，对象更新导致的字节命中率折损因子 $D_{LRU}$ 定义为 $1 - \frac{\text{更新导致的无效缓存占用比例}}{\text{总缓存容量}}$。在稳态下，若更新率 $\lambda_{upd}=1\%$/天，且更新对象在缓存中的平均驻留时间 $T_{res}$ 服从指数分布，则因更新而提前淘汰（或需重写）的字节占比近似为 $1 - e^{-\lambda_{upd} T_{res}}$。对于热门对象，$T_{res}$ 较大，折损显著；对于冷门对象，$T_{res} \approx 0$，折损可忽略。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 10 column 5 (char 793)
