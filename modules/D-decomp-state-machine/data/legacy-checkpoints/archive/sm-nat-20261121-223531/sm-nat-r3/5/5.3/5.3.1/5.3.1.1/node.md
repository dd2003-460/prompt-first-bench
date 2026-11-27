# N190: LRU 下界 $H_{LRU, base}$ 中“被驱逐对象”集合 $\mathcal{E}$ 的定义：在容量 $C$ 下，$\mathcal{E}$ 为按 L

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N67

## Claim

LRU 下界 $H_{LRU, base}$ 中“被驱逐对象”集合 $\mathcal{E}$ 的定义：在容量 $C$ 下，$\mathcal{E}$ 为按 LRU 堆栈距离排序后，累计大小超过 $C$ 的对象集合。在独立性假设（$\rho=0$）下，$\mathcal{E}$ 的大小仅取决于 $C$ 与 $S_{total}$ 的比值。

## Corrected Claim

LRU 下界 $H_{LRU, base}$ 中“被驱逐对象”集合 $\mathcal{E}$ 的定义：在容量 $C$ 下，$\mathcal{E}$ 为按 LRU 堆栈距离排序后，累计大小超过 $C$ 的对象集合。在独立性假设（$\rho=0$）下，$\mathcal{E}$ 的大小仅取决于 $C$ 与 $S_{total}$ 的比值。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU 驱逐机制基于堆栈距离，在独立性假设下，驱逐集合仅由容量与总大小的比例决定，符合缓存理论基本逻辑。
