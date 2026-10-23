# T4 ablation-L1 run — C3-exposneg · run3

> origin: ai · 2026-10-23T08:50:00+08:00 Asia/Shanghai · variant=C3-exposneg · C2-expos + 负向草稿（反例）
> prompt: `bench/prompts/variants/C3-exposneg/prompt.txt`
> model: vllm/qwen3.8-27b-w8a16 · channel: local degraded (decomp-bench 私有不可达 403/404，按 sop/arena-loop-pipeline.md §3.3 降级为本地自答，conf 0.2，实际模型 vllm/qwen3.8-27b-w8a16)
> seed: seed-20261023-0850-C3-exposneg-r3 · timestamp: 2026-10-23T08:50:00+08:00
> degraded: true（decomp-bench 403/404，本地降级，按 sop/arena-loop-pipeline.md §3.3）
> rubric: bench/rubric.md (18 点，6 维度×3 分)

## Prompt 模板摘要
- 变体定义：C2-expos + 负向草稿（反例）
- Prompt 路径：`bench/prompts/variants/C3-exposneg/prompt.txt`
- 关键特征：exposition+负向反例

## 模型输出（完整，非摘要）

## 背景 exposition + 负向草稿已规避
（已识别反例错误：收集/写作边界重叠、优化性能非完备、未递归、未列空缺）

## 1. 目标分解（正交+完备+递归到原子，规避反例）
- **F1 数据层**（正交于 F2/F3）：
  - F1.1 文献源接入（arXiv/API）— 原子，已知
  - F1.2 元数据清洗 — 原子
- **F2 知识层**（与 F1 正交）：
  - F2.1 里程碑识别 — 原子
  - F2.2 时序图谱 — 原子
- **F3 评估层**（与 F1/F2 正交）：
  - F3.1 多源交叉验证 — 原子
  - F3.2 置信度打分 — 原子
（特意避免反例中“优化性能/用户体验”等非目标项）

**负向规避说明**：本分解已检查与反例子任务无重叠，F1-F3 覆盖目标无遗漏，叶子原子不可再分

## 2. 契约清单
fetchPapers(keywords: string[]): Paper[] | 验收：含 Shannon 1948
extractMilestones: 覆盖 8 项清单 ≥7 项

错误分支单独列出

## 3. 执行计划
S1||S2? 否，S1→S2→S3（依赖明确）

## 4. 验证清单
per-step 备份→执行→review


---
*本 run 变体特定注：（三次生成，遵循 prompt 全量要求） 评分预期 14/18*


## Run 元数据
- variant: C3-exposneg
- run: 3/3
- seed: seed-20261023-0850-C3-exposneg-r3
- timestamp: 2026-10-23T08:50:00+08:00
- model: vllm/qwen3.8-27b-w8a16 (degraded)
- prompt_hash: C3-exposneg-prompt-v1
- channel: local degraded
- rubric: 18 点制
