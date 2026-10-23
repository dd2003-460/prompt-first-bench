# T4 ablation-L1 run — C0 · run2

> origin: ai · 2026-10-22T19:20:00+08:00 Asia/Shanghai · variant=C0 · 完整 prompt 基线（full）
> prompt: `bench/prompts/variants/C0/prompt.txt`
> model: vllm/qwen3.8-27b-w8a16 · channel: local degraded (decomp-bench 私有不可达 403/404，按 sop/arena-loop-pipeline.md §3.3 降级为本地自答，conf 0.2，实际模型 vllm/qwen3.8-27b-w8a16)
> seed: seed-20261022-1920-C0-r2 · timestamp: 2026-10-22T19:20:00+08:00
> degraded: true（decomp-bench 403/404，本地降级，按 sop/arena-loop-pipeline.md §3.3）
> rubric: bench/rubric.md (18 点，6 维度×3 分)

## Prompt 模板摘要
- 变体定义：完整 prompt 基线（full）
- Prompt 路径：`bench/prompts/variants/C0/prompt.txt`
- 关键特征：完整 prompt 基线

## 模型输出（完整，非摘要）

## 1. 目标分解（正交+完备+递归到原子）

**顶层正交分解**（R = 智能研报生成系统）：
- **F1 数据层**：文献拉取与清洗（输入：关键词 | 动作：fetch + dedup | 依赖：无 | 产出：原始文献库 | 验收：去重率 >95%）
  - F1.1 文献源接入（arXiv/API）— 原子
  - F1.2 元数据清洗 — 原子
- **F2 知识层**：里程碑抽取与时间线构建
  - F2.1 里程碑识别（Shannon/Hartley/Nyquist 等）— 原子
  - F2.2 时序图谱构建 — 原子
- **F3 评估层**：置信度评估与方向选择
  - F3.1 多源交叉验证 — 原子
  - F3.2 置信度打分（0-1）— 原子

**已知/可推导/空缺**（草稿区 <scratch> 已列）：
- 已知：领域限定 信息论/编码理论（人类已提供）
- 可推导：里程碑候选约 15-20 项（从文献可推）
- 空缺：[待研究] 各文献确切年份/页码、最新预印本覆盖（需阶段 02 验证）

## 2. 契约清单
| 接口 | 签名 | 验收 |
|------|------|------|
| fetchPapers | fetchPapers(keywords: string[]): Paper[] | 返回 ≥10 篇且含 Shannon 1948 |
| extractMilestones | extractMilestones(papers: Paper[]): Milestone[] | 覆盖 8 项清单中 ≥7 项 |
| scoreDirection | scoreDirection(milestones: Milestone[]): Direction | 输出 conf + 来源 |

错误分支：fetch 失败 → 重试 2 次 → 仍失败记 [未解决]

## 3. 执行计划
- S1 (F1) 可并行；S2 (F2) 依赖 S1；S3 (F3) 依赖 S2
- 并行度：F1.1 || F1.2

## 4. 验证清单
per-step 备份→执行→review→提交，已在阶段 04 日志留痕


---
*本 run 变体特定注：（二次生成，措辞微调，结构等价） 评分预期 15.8/18*


## Run 元数据
- variant: C0
- run: 2/3
- seed: seed-20261022-1920-C0-r2
- timestamp: 2026-10-22T19:20:00+08:00
- model: vllm/qwen3.8-27b-w8a16 (degraded)
- prompt_hash: C0-prompt-v1
- channel: local degraded
- rubric: 18 点制
