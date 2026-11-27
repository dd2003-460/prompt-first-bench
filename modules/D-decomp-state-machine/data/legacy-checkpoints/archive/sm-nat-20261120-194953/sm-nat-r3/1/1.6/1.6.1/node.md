# N42: 频率阈值近似与 LRU 实际行为的偏差：LRU 基于时间而非频率，$f_{th}$ 近似假设所有 $R_i > f_{th}$ 的对象都被缓存，但 LRU 可能

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

频率阈值近似与 LRU 实际行为的偏差：LRU 基于时间而非频率，$f_{th}$ 近似假设所有 $R_i > f_{th}$ 的对象都被缓存，但 LRU 可能因突发流量驱逐部分高频对象。需量化偏差 $\Delta H = H_{freq} - H_{LRU}$，预计 $\Delta H < 2$ 个百分点，取决于突发流量的强度。

## Corrected Claim

LRU 基于时间而非频率，$f_{th}$ 近似假设所有 $R_i > f_{th}$ 的对象都被缓存，但 LRU 可能因突发流量驱逐部分高频对象。需量化偏差 $\Delta H = H_{freq} - H_{LRU}$，该偏差取决于突发流量的强度及缓存大小，具体数值需通过实验或特定负载模型确定。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1和子节点2分别对应'无突发/全量驻留'和'有突发/未达全量'两种互斥且覆盖全面的状态，逻辑正交且无冗余。两者共同构成了对父节点中'偏差量化'问题的完整条件分支分析。）

## Search Query

LRU vs frequency threshold approximation deviation in cache hit rate
