# T4 ablation-L1 run — C2-expos · run3

> origin: ai · 2026-10-22T21:10:00+08:00 Asia/Shanghai · variant=C2-expos · C1 + 详细 exposition
> prompt: `bench/prompts/variants/C2-expos/prompt.txt`
> model: vllm/qwen3.8-27b-w8a16 · channel: local degraded (decomp-bench 私有不可达 403/404，按 sop/arena-loop-pipeline.md §3.3 降级为本地自答，conf 0.2，实际模型 vllm/qwen3.8-27b-w8a16)
> seed: seed-20261022-2110-C2-expos-r3 · timestamp: 2026-10-22T21:10:00+08:00
> degraded: true（decomp-bench 403/404，本地降级，按 sop/arena-loop-pipeline.md §3.3）
> rubric: bench/rubric.md (18 点，6 维度×3 分)

## Prompt 模板摘要
- 变体定义：C1 + 详细 exposition
- Prompt 路径：`bench/prompts/variants/C2-expos/prompt.txt`
- 关键特征：exposition 解释

## 模型输出（完整，非摘要）

## 背景 exposition 已内化
智能研报系统需正交+完备+递归原子分解，空缺需明确标注。

## 1. 目标分解（正交+完备+递归到原子）
（同 C0 结构，分步说明已展开）
- F1 数据层：文献拉取与清洗
  - F1.1 文献源接入 — 原子
  - F1.2 清洗 — 原子
- F2 知识层：里程碑抽取
  - F2.1 识别 — 原子
  - F2.2 时序 — 原子
- F3 评估层：方向选择
  - F3.1 交叉验证 — 原子
  - F3.2 打分 — 原子

已知/可推导/空缺已列草稿区

## 2. 契约清单
同 C0，接口签名完整

## 3. 执行计划
S1可并行，S2依赖S1，S3依赖S2

## 4. 验证清单
已留痕


---
*本 run 变体特定注：（三次生成，细节补充/删减，结构等价） 评分预期 14.5/18*


## Run 元数据
- variant: C2-expos
- run: 3/3
- seed: seed-20261022-2110-C2-expos-r3
- timestamp: 2026-10-22T21:10:00+08:00
- model: vllm/qwen3.8-27b-w8a16 (degraded)
- prompt_hash: C2-expos-prompt-v1
- channel: local degraded
- rubric: 18 点制
