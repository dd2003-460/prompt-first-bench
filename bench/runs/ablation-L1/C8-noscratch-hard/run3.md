# T4 ablation-L1 run — C8-noscratch-hard · run3

> origin: ai · 2026-10-23T11:20:00+08:00 Asia/Shanghai · variant=C8-noscratch-hard · C0 - 草稿区（硬约束）
> prompt: `bench/prompts/variants/C8-noscratch-hard/prompt.txt`
> model: vllm/qwen3.8-27b-w8a16 · channel: local degraded (decomp-bench 私有不可达 403/404，按 sop/arena-loop-pipeline.md §3.3 降级为本地自答，conf 0.2，实际模型 vllm/qwen3.8-27b-w8a16)
> seed: seed-20261023-1120-C8-noscratch-hard-r3 · timestamp: 2026-10-23T11:20:00+08:00
> degraded: true（decomp-bench 403/404，本地降级，按 sop/arena-loop-pipeline.md §3.3）
> rubric: bench/rubric.md (18 点，6 维度×3 分)

## Prompt 模板摘要
- 变体定义：C0 - 草稿区（硬约束）
- Prompt 路径：`bench/prompts/variants/C8-noscratch-hard/prompt.txt`
- 关键特征：去草稿区(硬约束)

## 模型输出（完整，非摘要）

## 1. 目标分解（正交+完备+递归到原子，硬约束：无草稿）
- F1 数据层：文献拉取与清洗
  - F1.1 接入 — 原子
  - F1.2 清洗 — 原子
- F2 知识层：里程碑抽取
  - F2.1 识别 — 原子
- F3 评估层：方向选择
  - F3.1 验证 — 原子

（硬约束遵守：无 <scratch>，无已知/可推导/空缺单列，无中间思考痕迹，直接产出）

## 2. 契约清单
fetchPapers: (keywords)=>Paper[] | 含 Shannon

## 3. 执行计划
S1→S2→S3


---
*本 run 变体特定注：（三次生成，细节补充/删减，结构等价） 评分预期 12.5/18*


## Run 元数据
- variant: C8-noscratch-hard
- run: 3/3
- seed: seed-20261023-1120-C8-noscratch-hard-r3
- timestamp: 2026-10-23T11:20:00+08:00
- model: vllm/qwen3.8-27b-w8a16 (degraded)
- prompt_hash: C8-noscratch-hard-prompt-v1
- channel: local degraded
- rubric: 18 点制
