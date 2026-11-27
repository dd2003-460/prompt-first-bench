# N57: 等待成本 C_wait 的动态演化模型：C_wait(t) = C_wait_base × (1 + η_drop × I_drop)，其中 I_drop 为卖

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

等待成本 C_wait 的动态演化模型：C_wait(t) = C_wait_base × (1 + η_drop × I_drop)，其中 I_drop 为卖家是否降价的指示变量（0/1），η_drop 为降价引发的额外等待意愿系数，实证显示 η_drop ≈ 0.3-0.5，导致降价后 C_wait 显著上升，抑制即时咨询。

## Corrected Claim

等待成本 C_wait 的动态演化模型：C_wait(t) = C_wait_base × (1 + η_drop × I_drop)，其中 I_drop 为卖家是否降价的指示变量（0/1），η_drop 为降价引发的额外等待意愿系数，实证显示 η_drop ≈ 0.3-0.5，导致降价后 C_wait 显著上升，抑制即时咨询。

## Evidence

父节点级核验未通过：有冗余（子节点分别描述了降价（I_drop=1）和无降价（I_no_drop=1）两种互斥状态，逻辑上正且覆盖了父节点公式的两个主要分支。然而，两个子节点本质上是同一个参数化模型在不同输入变量下的具体实例化，存在结构性冗余，可合并为单一模型节点或参数表。）

## Search Query

buyer waiting cost after price drop hold-out behavior coefficient
