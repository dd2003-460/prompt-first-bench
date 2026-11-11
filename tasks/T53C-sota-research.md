# T53C-SOTA: DeepResearch Bench SOTA 分数调研

## 任务

查当前最新开源/公开 deepresearch 类 agent 在以下 5 道题（或最接近的 benchmark subset）上的**逐题分数**：

1. "2024年 NVIDIA H200 GPU 的 TDP 是多少瓦？比 H100 SXM 高多少百分比？"
2. "Transformer 原始论文中 multi-head attention 的 head 数是多少？GPT-3 用了多少？差几倍？"
3. "HotpotQA 数据集有多少条标注？其中 compositional 类型占多少比例？"
4. "LLaMA 2 70B 的参数量是多少？训练用了多少 token？"
5. "DeepSeek-V3 的 MoE 总参数和激活参数分别是多少？ratio 是多少？"

## 对标系统（按优先级）

1. **OpenAI Deep Research (o3-pro)** — 2025.02 发布，HLE/broad research 分数公开
2. **GPT-4o + function calling (multi-hop)** — HotpotQA/2WikiMultihop leaderboard 上的经典 baseline
3. **任何 2025-2026 开源 deepresearch agent**（GitHub star >1k 且有公开 bench 结果的）

## 输出格式

```json
{
  "sota_systems": [
    {
      "name": "...",
      "source_url": "...",
      "benchmark": "hotpotqa/2wiki/custom",
      "per_question_scores": {"q1": 0.8, "q2": 1.0, ...},
      "aggregate": {"em": 0.72, "f1": 0.81},
      "notes": "..."
    }
  ],
  "recommended_baseline": "...",
  "reasoning": "为什么选这个作为主要对标"
}
```

## 注意

- 如果找不到逐题分数，给 aggregate EM/F1 + 说明哪篇论文/哪个 leaderboard
- 只收有 URL 可溯源的分数，不编
- 如果某系统没有公开 per-question 数据，标 `null` 并说明

## 验收

- ≥2 个系统的分数落盘
- 每个分数有 source_url
- 推荐 1 个主 baseline + 理由