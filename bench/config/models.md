# 3 模型档位配置（强/中/弱）

> origin: ai · 2026-10-22 · round 1
> 选择依据：`projects/AI-计算科学/D1-persona-align/tasks/bench-目标调研-20261022.md` §D4.1（暂定档位）；厂商分散原则（rubric/scoring.md 模型维度要求 ≥2 厂商）。执行前按 arena Direct 模式实际可用列表核对。

| 档位 | arena 模型名（Direct 列表内按实际调整） | 厂商 | 选择理由 |
|------|----------------------------------------|------|----------|
| 强 | claude-sonnet-5-high | Anthropic | 调研文件 D4.1 建议；当前第一梯队 |
| 中 | gemini-3.1-pro-preview | Google | 调研文件 D4.1 建议；非 Anthropic 厂商，分散 |
| 弱 | qwen3.6-plus | Alibaba | 调研文件 D4.1 建议；第三厂商，弱档对照 |

## 核对与回退规则

- round 1 执行时打开 Direct 模型选择器逐一确认上述名字是否存在；
- 不存在时：选同厂商相邻能力档模型替换，并在本文件追加「实际替换」记录（保留原建议名 + 替换名 + 替换原因 + 日期）；
- 若 3 个都不可选 → 全部格子用 arena 默认 Router（"Max"）跑，模型维度标 N/A（按 rubric 降级条款），并记录到 `bench/results/` 备注。

## run 元数据要求

每个 run 文件头记录：arena 实际模型名/版本、时间（Asia/Shanghai）、通道 = arena Direct、题目出处 = `bench/tasks/fixed-questions.md` Q<n>。
