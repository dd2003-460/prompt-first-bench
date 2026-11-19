# T53-B12 阶段 02：信息调研（题集来源 + SOTA 公开分）

- 上游：01 目标分解
- 边界：本阶段不引用 03/04 的执行结果

## 1. 题集来源核对（工作区实况）

| 来源 | 内容 | 可用性 |
|---|---|---|
| `ablation_harness.QUESTIONS` | `gpu` 等内部题 | 已注册，可跑（复用） |
| DRB 公开集（drb-1/2/16） | DeepResearch Bench 100 题 | 题目运行时从 HF 拉，**仓库内无题面存档**；已跑 drb-1/drb-2 |
| `experiments/stage-ablation/questions/Q1..Q5.md` | pfb 自建 5 题（GPU/模型选型/推理基础设施/RAG/方法论） | 可读，但**无公开 SOTA 分** |
| 公开 bench（GAIA/HotpotQA/BrowseComp） | 题级分数从未公开 | 只能取 bench 级平均分 |

结论：要满足 AC2，"新题"必须挂到有公开分的 bench 上；但题级分不存在 → **只能做到 bench 级参照**（见 02.5 裁定）。

## 2. SOTA 公开分（取自 `modules/E-sota-benchmark/research/sm-bench-sota-table.json`，该表 T53C 已逐条核到原文）

| 系统 | bench | 指标 | 分 | 开源 | URL |
|---|---|---|---|---|---|
| LangChain Open Deep Research (GPT-5) | DRB | RACE overall | 50.60 | 框架开源 | ICLR 2026 proceedings PDF |
| Tongyi DeepResearch 30B-A3B | DRB | RACE | 40.46 | 全开源 | 同上 |
| Tongyi DeepResearch | GAIA val | Avg@3 | 70.9 | 全开源 | arxiv.org/html/2510.24701 |
| Tongyi DeepResearch | BrowseComp | Avg@3 | 43.4 | 全开源 | 同上 |
| Tongyi DeepResearch | HLE | Avg@3 | 32.9 | 全开源 | 同上 |
| Search-R1 (Qwen2.5-7B) | HotpotQA | F1 | 55.9 | 全开源 | arxiv.org/html/2504.03160 |
| DeepResearcher | HotpotQA | F1 | 52.8 | 全开源 | 同上 |
| DeepResearcher | 2WikiMultiHopQA | F1 | 59.7 | 全开源 | 同上 |
| OpenAI Deep Research | GAIA val | pass@1 | 67.36 | 闭源 | openai.com/index/introducing-deep-research |

（完整 12 行见 `sm-bench-sota-table.json`；本表只摘与 5 题相关的行）

## 3. judge 口径来源（代码级核对）

- `bface_score.py`：`JUDGE_URL=http://localhost:1234/v1/chat/completions`，`JUDGE_MODEL=qwen2.5-7b-original` —— 异族于生成端 `qwen3.8-27b`（`ablation_harness.LLM_MODEL`）
- `drb_race_judge.py --judge local --judge-url http://localhost:1234/v1`：DRB 四维 judge 的本地化版本
- 端点清单：生成 `127.0.0.1:8787`，judge `localhost:1234`

## 4. 现有 run 资产盘点

| 文件 | qid | 节点 | 状态 | 备注 |
|---|---|---|---|---|
| `runs-s5-sm-gpu.json` | gpu | 163 | final_state=verified, leak=0 | 未 judge（内部题无 DRB criteria） |
| `runs-s5-sm-drb-2.json` | drb-2 | 62 | rework | judge 0.0（检索全盲期产物） |
| `runs-s5-sm-drb-1.json` | drb-1 | 169 | — | judge 0.0，同上 |
| `runs-s5-sm-nat.json` | nat | 278 | verify | 非本 bench 5 题，仅参考 |

## 5. 本阶段不确定性

- 3 个新题是**本轮自建**（仿 GAIA/HotpotQA/BrowseComp 题型），不是这三个 bench 的原题 → 其"公开分"只能作量级参照，必须在文档里说死。
- DRB 题面未入库（运行时拉取），故"drb-2 有公开同题分"**不成立**：DRB 的 RACE 也是 bench 级平均。
