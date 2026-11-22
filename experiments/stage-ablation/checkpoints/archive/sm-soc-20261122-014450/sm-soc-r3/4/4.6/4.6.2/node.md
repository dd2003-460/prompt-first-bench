# N84: 卖家策略性回升的临界条件：当降价后的预期收益 E[R_low] < 回升后的预期收益 E[R_high] + C_switch 时，卖家会在 T_revert 

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N21

## Claim

卖家策略性回升的临界条件：当降价后的预期收益 E[R_low] < 回升后的预期收益 E[R_high] + C_switch 时，卖家会在 T_revert 天后回升价格；需量化 T_revert 与 w 的关系，确保 w 足够大以使得 T_revert > 48小时（激励窗口）

## Corrected Claim

卖家策略性回升的临界条件通常建模为：当降价后的预期收益 E[R_low] 小于回升后的预期收益 E[R_high] 加上切换成本 C_switch 时，卖家倾向于回升价格。具体回升时间 T_revert 与参数 w 的关系需通过实证数据或特定模型校准确定，以确保激励窗口（如48小时）的有效性。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了父节点要求的三个核心维度：1. 收益临界条件方程（对应 E[R] 比较与阈值求解）；2. T_revert 与 w 的函数关系（对应时间量化与 w 的最小值）；3. C_switch 的具体构成（对应成本量化）。三者分别处理收益平衡、时间动力学和成本参数，逻辑上正交且无重叠。虽然 C_switch 出现在子节点1的方程中，但子节点3专门负责其内部结构的分解，这是合理的参数化分解，不构成冗余。）

## Search Query

dynamic pricing incentive reversal behavior seller strategy second-hand market

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/552993159&rut=bf99cd9ae242dfc047f849ac6c906fa6c2548c862ea19b8e492dc2cdb12eaafc', 'type': 'ddg', 'title': '智能条件单策略交易类型 - 知乎 - 知乎专栏'}
