# N187: 替换开销 $\epsilon_{overhead}$ 的量化模型：$\epsilon_{overhead}$ 等于 LFU 元数据更新的时间占比。假设每次替换需

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

替换开销 $\epsilon_{overhead}$ 的量化模型：$\epsilon_{overhead}$ 等于 LFU 元数据更新的时间占比。假设每次替换需 $T_{meta}$ 时间，每次访问需 $T_{acc}$ 时间，则 $\epsilon_{overhead} \approx (N_{repl}/N_{req}) \times (T_{meta}/T_{acc})$。在 50M 请求/天，替换率 $N_{repl} \approx 1\%$ 时，若 $T_{meta}/T_{acc} \approx 0.1$，则 $\epsilon_{overhead} \approx 0.001$。

## Corrected Claim

替换开销 $\epsilon_{overhead}$ 的量化模型：$\epsilon_{overhead}$ 等于 LFU 元数据更新的时间占比。假设每次替换需 $T_{meta}$ 时间，每次访问需 $T_{acc}$ 时间，则 $\epsilon_{overhead} \approx (N_{repl}/N_{req}) \times (T_{meta}/T_{acc})$。在 50M 请求/天，替换率 $N_{repl} \approx 1\%$ 时，若 $T_{meta}/T_{acc} \approx 0.1$，则 $\epsilon_{overhead} \approx 0.001$。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导自洽，数值计算正确（1% * 0.1 = 0.001），量级合理。
