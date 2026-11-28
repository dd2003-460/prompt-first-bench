# N463: WebShop 基准上 Qwen3.8-27B 的成功率参考：基于 ReAct 框架，Qwen 系列 32B 模型在 WebShop 上的 Success Ra

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N162

## Claim

WebShop 基准上 Qwen3.8-27B 的成功率参考：基于 ReAct 框架，Qwen 系列 32B 模型在 WebShop 上的 Success Rate 通常在 70%-80% 之间，若工具延迟从 0s 增加到 1s，由于搜索 API 响应变慢可能导致部分探索路径超时，成功率预计下降 5%-10%，即降至 65%-75%

## Corrected Claim

在 WebShop 基准上，基于 ReAct 框架的 Qwen 系列大模型（如 32B 级别）通常具有较高的任务成功率（约 70%-80%）。引入 1 秒的工具调用延迟可能会因增加交互轮次或导致部分超时策略触发，从而造成成功率的轻微下降（预计 5%-10% 左右），但具体数值需依赖实际实验验证。

## Evidence

[质询]该陈述包含具体的经验性数值（70%-80% 基线成功率、5%-10% 延迟导致的下降幅度），这些并非第一性原理可推导的数学或物理事实，而是依赖于特定实验设置、提示词工程和模型微调状态的工程经验数据。此外，'Qwen3.8-27B' 这一型号名称可能存在幻觉或混淆（通常 Qwen 系列有 7B, 14B, 32B, 72B 等，27B 较少见，且 32B 与 27B 混用），缺乏可靠来源支持其具体性能指标。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体数值无法从第一性原理推出）

## Search Query

Qwen model WebShop benchmark success rate ReAct framework
