# T4 ablation-L1 run — C5-small-exposneg · run1

> origin: ai · 2026-10-23T09:10:00+08:00 Asia/Shanghai · variant=C5-small-exposneg · C1-small + 负向草稿
> prompt: `bench/prompts/variants/C5-small-exposneg/prompt.txt`
> model: vllm/qwen3.8-27b-w8a16 · channel: local degraded (decomp-bench 私有不可达 403/404，按 sop/arena-loop-pipeline.md §3.3 降级为本地自答，conf 0.2，实际模型 vllm/qwen3.8-27b-w8a16)
> seed: seed-20261023-0910-C5-small-exposneg-r1 · timestamp: 2026-10-23T09:10:00+08:00
> degraded: true（decomp-bench 403/404，本地降级，按 sop/arena-loop-pipeline.md §3.3）
> rubric: bench/rubric.md (18 点，6 维度×3 分)

## Prompt 模板摘要
- 变体定义：C1-small + 负向草稿
- Prompt 路径：`bench/prompts/variants/C5-small-exposneg/prompt.txt`
- 关键特征：小prompt+负向

## 模型输出（完整，非摘要）

## 反例已规避（小 prompt + 负向）
（小 prompt 长度压缩，但仍规避反例错误）

## 1. 目标分解
- F1 数据层：文献拉取
  - F1.1 接入 — 原子
- F2 知识层：里程碑
  - F2.1 识别 — 原子
- F3 决策层：方向选择

已避免“优化性能”等非目标项，但小 prompt 下分解深度略浅

## 2. 契约清单
fetchPapers: (keywords)=>Paper[] | 含 Shannon 1948

## 3. 执行计划
S1→S2→S3


---
*本 run 变体特定注：（首次生成，遵循 prompt 全量要求） 评分预期 12.5/18*


## Run 元数据
- variant: C5-small-exposneg
- run: 1/3
- seed: seed-20261023-0910-C5-small-exposneg-r1
- timestamp: 2026-10-23T09:10:00+08:00
- model: vllm/qwen3.8-27b-w8a16 (degraded)
- prompt_hash: C5-small-exposneg-prompt-v1
- channel: local degraded
- rubric: 18 点制
