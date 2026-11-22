# N90: 选择效应量化：假设平台对降价卖家给予流量权重加成 w_boost，低质商品（定义：退货率>10%或描述不符投诉率>5%）在推荐池中的占比变化 ΔShare_lo

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24

## Claim

选择效应量化：假设平台对降价卖家给予流量权重加成 w_boost，低质商品（定义：退货率>10%或描述不符投诉率>5%）在推荐池中的占比变化 ΔShare_low = (Share_low_post - Share_low_pre)，其中 Share_low_pre 需基于历史数据估算（[待核验]，预估基线 5-15%）。

## Corrected Claim

选择效应量化：假设平台对降价卖家给予流量权重加成 w_boost，低质商品（定义：退货率>10%或描述不符投诉率>5%）在推荐池中的占比变化 ΔShare_low = (Share_low_post - Share_low_pre)，其中 Share_low_pre 需基于历史数据估算（具体基线值需根据实际平台数据确定，此处暂缺可靠参考）。

## Evidence

父节点级核验未通过：非正交, 有冗余（1. 冗余性严重：子节点4、5、6（工作点A/B/C）本质上是同一参数 w_boost 在不同取值下的具体案例枚举，属于参数敏感性分析，而非独立的正交维度，应合并为一个“w_boost 敏感性分析”节点。2. 非正交/逻辑矛盾：子节点1-3讨论的是“卖家边际成本”，这与父节点明确限定的“选择效应量化（流量权重加成 w_boost 导致的低质商品占比变化 ΔShare_low）”在概念层级和因果逻辑上脱节。成本分析是选择效应的潜在驱动因素或背景约束，而非选择效应本身的量化组成部分，强行并列破坏了主题聚焦。3. 公式不一致：子节点8给出的公式 ΔShare_low = (λ_low_new * w_boost ...) 与子节点4-6中直接赋值 Share_low_post ≈ λ_low_new 的逻辑存在潜在冲突（未明确 w_boost 是乘法因子还是加法因子，且分母 Total_Listings_post 未定义），导致内部逻辑不自洽。）

## Search Query

marketplace platform recommendation bias low quality sellers traffic boost adverse selection rate
