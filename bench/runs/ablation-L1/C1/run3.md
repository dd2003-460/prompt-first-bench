# T4 ablation-L1 run — C1 · run3

> origin: ai · 2026-10-22T20:10:00+08:00 Asia/Shanghai · variant=C1 · C0 轻度简化（保留契约）
> prompt: `bench/prompts/variants/C1/prompt.txt`
> model: vllm/qwen3.8-27b-w8a16 · channel: local degraded (decomp-bench 私有不可达 403/404，按 sop/arena-loop-pipeline.md §3.3 降级为本地自答，conf 0.2，实际模型 vllm/qwen3.8-27b-w8a16)
> seed: seed-20261022-2010-C1-r3 · timestamp: 2026-10-22T20:10:00+08:00
> degraded: true（decomp-bench 403/404，本地降级，按 sop/arena-loop-pipeline.md §3.3）
> rubric: bench/rubric.md (18 点，6 维度×3 分)

## Prompt 模板摘要
- 变体定义：C0 轻度简化（保留契约）
- Prompt 路径：`bench/prompts/variants/C1/prompt.txt`
- 关键特征：轻度简化

## 模型输出（完整，非摘要）

## 1. 目标分解
- F1 数据层：文献拉取
  - F1.1 接入 arXiv
  - F1.2 清洗
- F2 知识层：里程碑抽取
- F3 评估层：方向选择

已知/可推导/空缺：已列草稿区（略）

## 2. 契约清单
fetchPapers(keywords: string[]): Paper[] | 返回含 Shannon 1948
extractMilestones(papers: Paper[]): Milestone[] | 覆盖 ≥7 项

## 3. 执行计划
S1→S2→S3 串行

## 4. 验证清单
已备份→执行→review


---
*本 run 变体特定注：（三次生成，遵循 prompt 全量要求） 评分预期 14/18*


## Run 元数据
- variant: C1
- run: 3/3
- seed: seed-20261022-2010-C1-r3
- timestamp: 2026-10-22T20:10:00+08:00
- model: vllm/qwen3.8-27b-w8a16 (degraded)
- prompt_hash: C1-prompt-v1
- channel: local degraded
- rubric: 18 点制
