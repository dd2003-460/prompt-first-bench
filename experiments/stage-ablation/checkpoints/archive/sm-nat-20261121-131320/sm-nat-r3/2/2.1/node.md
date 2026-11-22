# N8: LFU 相对 LRU 的理论提升上限 ΔH_max：ΔH_max = H_LFU - H_LRU，其中 H_LFU 基于频率优先填充，上限受限于长尾对象的频率方

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N2

## Claim

LFU 相对 LRU 的理论提升上限 ΔH_max：ΔH_max = H_LFU - H_LRU，其中 H_LFU 基于频率优先填充，上限受限于长尾对象的频率方差；当 β=0.9 时，热度分布陡峭，LFU 提升空间主要来自于排除低频大对象，量化为 ΔH_max ≈ (1 - H_LRU) * (1 - P(f < f_threshold | S > C))。

## Corrected Claim

LFU 相对 LRU 的理论提升上限 ΔH_max 主要源于对低频大对象的排除。当热度分布陡峭（如 β=0.9）时，ΔH_max 正比于低频大对象在总请求流中占据的带宽或空间比例，具体数值依赖于对象大小与频率的联合分布。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了父节点公式中的核心组件：H_LFU（子节点1）、H_LRU（子节点2）、低频大对象损失项/上界约束（子节点3）以及修正因子K_ρ（子节点4）。各子节点定义明确，职责分离清晰，无内容重叠或矛盾，且共同构成了计算ΔH_max所需的全部数学要素。）
