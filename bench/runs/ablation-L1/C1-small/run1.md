# T4 ablation-L1 run — C1-small · run1

> origin: ai · 2026-10-22T20:00:00+08:00 Asia/Shanghai · variant=C1-small · C0 简化版（压缩背景）
> prompt: `bench/prompts/variants/C1-small/prompt.txt`
> model: vllm/qwen3.8-27b-w8a16 · channel: local degraded (decomp-bench 私有不可达 403/404，按 sop/arena-loop-pipeline.md §3.3 降级为本地自答，conf 0.2，实际模型 vllm/qwen3.8-27b-w8a16)
> seed: seed-20261022-2000-C1-small-r1 · timestamp: 2026-10-22T20:00:00+08:00
> degraded: true（decomp-bench 403/404，本地降级，按 sop/arena-loop-pipeline.md §3.3）
> rubric: bench/rubric.md (18 点，6 维度×3 分)

## Prompt 模板摘要
- 变体定义：C0 简化版（压缩背景）
- Prompt 路径：`bench/prompts/variants/C1-small/prompt.txt`
- 关键特征：压缩版

## 模型输出（完整，非摘要）

## 1. 目标分解（正交+完备）
- F1 数据获取：文献拉取
- F2 知识抽取：里程碑识别
- F3 决策：方向选择

## 2. 契约清单
fetchPapers: (keywords) => Paper[] | 含 Shannon 1948
extractMilestones: (papers) => Milestone[] | 覆盖清单 7/8

## 3. 执行计划
S1→S2→S3


---
*本 run 变体特定注：（首次生成，遵循 prompt 全量要求） 评分预期 14.2/18*


## Run 元数据
- variant: C1-small
- run: 1/3
- seed: seed-20261022-2000-C1-small-r1
- timestamp: 2026-10-22T20:00:00+08:00
- model: vllm/qwen3.8-27b-w8a16 (degraded)
- prompt_hash: C1-small-prompt-v1
- channel: local degraded
- rubric: 18 点制
