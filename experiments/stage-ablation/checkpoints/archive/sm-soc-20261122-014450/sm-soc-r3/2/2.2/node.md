# N10: ‘降价无响应’机制：主动降价触发‘柠檬市场’逆向选择信号。买家模型更新：P(Defective | Price_Drop) > P(Defective | Pr

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

‘降价无响应’机制：主动降价触发‘柠檬市场’逆向选择信号。买家模型更新：P(Defective | Price_Drop) > P(Defective | Price_Stable)。具体表现为，降价后48小时内新咨询量 ΔQ_consult ≈ -β * (P_drop / P_initial)，其中 β 为价格敏感度系数，且 β 在二手非标品中显著大于标准化品。

## Corrected Claim

‘降价无响应’机制：主动降价可能触发‘柠檬市场’逆向选择信号，导致买家对商品缺陷概率的后验估计上升（P(Defective | Price_Drop) > P(Defective | Price_Stable)）。在二手非标品市场中，这种负面信号效应通常比标准化品更显著，可能导致咨询量或成交意愿下降，但具体下降幅度取决于价格敏感度及市场结构，无统一固定公式。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点中的核心机制（逆向选择信号/β量化）、买家决策逻辑（概率更新）和具体业务指标（咨询量阈值条件），彼此独立且无逻辑重叠。虽然β在子节点1中定义，在子节点3中作为变量使用，但这属于正常的参数引用而非内容冗余。子节点覆盖了父节点提出的所有关键数学关系和验证需求。）

## Search Query

price drop negative signal lemon market second-hand goods consultation drop
