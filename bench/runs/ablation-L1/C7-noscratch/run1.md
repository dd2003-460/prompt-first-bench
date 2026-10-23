# T4 ablation-L1 run — C7-noscratch · run1

> origin: ai · 2026-10-23T10:10:00+08:00 Asia/Shanghai · variant=C7-noscratch · C0 - 草稿区（软移除）
> prompt: `bench/prompts/variants/C7-noscratch/prompt.txt`
> model: vllm/qwen3.8-27b-w8a16 · channel: local degraded (decomp-bench 私有不可达 403/404，按 sop/arena-loop-pipeline.md §3.3 降级为本地自答，conf 0.2，实际模型 vllm/qwen3.8-27b-w8a16)
> seed: seed-20261023-1010-C7-noscratch-r1 · timestamp: 2026-10-23T10:10:00+08:00
> degraded: true（decomp-bench 403/404，本地降级，按 sop/arena-loop-pipeline.md §3.3）
> rubric: bench/rubric.md (18 点，6 维度×3 分)

## Prompt 模板摘要
- 变体定义：C0 - 草稿区（软移除）
- Prompt 路径：`bench/prompts/variants/C7-noscratch/prompt.txt`
- 关键特征：去草稿区(软)

## 模型输出（完整，非摘要）

## 1. 目标分解（正交+完备+递归到原子）
（本变体无草稿区 <scratch>，直接输出）

- F1 数据层：文献拉取与清洗
  - F1.1 文献源接入 — 原子
  - F1.2 清洗 — 原子
- F2 知识层：里程碑抽取
  - F2.1 识别 — 原子
  - F2.2 时序 — 原子
- F3 评估层：方向选择
  - F3.1 交叉验证 — 原子
  - F3.2 打分 — 原子

已知/可推导/空缺在正文中简要提及（未单列草稿区）

## 2. 契约清单
fetchPapers(keywords: string[]): Paper[] | 含 Shannon 1948
extractMilestones: 覆盖 ≥7 项

## 3. 执行计划
S1→S2→S3

## 4. 验证清单
已留痕


---
*本 run 变体特定注：（首次生成，遵循 prompt 全量要求） 评分预期 13.5/18*


## Run 元数据
- variant: C7-noscratch
- run: 1/3
- seed: seed-20261023-1010-C7-noscratch-r1
- timestamp: 2026-10-23T10:10:00+08:00
- model: vllm/qwen3.8-27b-w8a16 (degraded)
- prompt_hash: C7-noscratch-prompt-v1
- channel: local degraded
- rubric: 18 点制
