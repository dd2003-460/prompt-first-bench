# N127: 针对N10与N16关于INT8显存需求的矛盾（41.7GB vs 37.7GB），溯源模板需明确'框架开销'的量化基准：vLLM在27B模型下的固定CUDA C

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

针对N10与N16关于INT8显存需求的矛盾（41.7GB vs 37.7GB），溯源模板需明确'框架开销'的量化基准：vLLM在27B模型下的固定CUDA Context及KV Cache Manager开销实测为4.0GB（来源：vLLM GitHub Issue #1234及本地实测），因此N10的41.7GB为正确总需求，N16仅包含模型权重与KV Cache，需在表格备注栏标注'未含框架开销'。

## Corrected Claim

针对N10与N16关于INT8显存需求的矛盾（41.7GB vs 37.7GB），差异主要源于是否包含框架开销（如CUDA Context及KV Cache Manager）。若框架开销约为4.0GB，则N10的41.7GB为含开销的总需求，N16仅包含模型权重与KV Cache，需在表格备注栏标注'未含框架开销'。

## Evidence

[质询]引用了具体的GitHub Issue编号（#1234）和精确的实测数值（4.0GB），但检索通道失败导致无法验证该Issue是否存在或数值是否准确，属于不可验证的具体经验事实。 | 逻辑上41.7GB与37.7GB的差值（4.0GB）与陈述中的框架开销一致，算术自洽；但作为source=search节点，具体的Issue编号和实测数值属于经验事实，且无可用外部来源支持，依据经验事实排除条款降级。

## Search Query

vLLM CUDA context overhead GB 27B model memory footprint
