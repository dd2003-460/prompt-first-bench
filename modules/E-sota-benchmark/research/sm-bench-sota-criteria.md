# SM Bench SOTA 对标标准 v3（T53-B12 落地）

> origin: ai（T53 AC4 → T53-B12 修订）· 2026-11-16 · 分支 `arena/f65a5a27-prompt-first-bench`
> 上游：v2（2026-11-11，baseline = 本机模型 + 开源框架）；本版补"公开 SOTA 分"这一层，并裁定尺度口径。
> 数字来源：`modules/E-sota-benchmark/research/sm-bench-sota-table.json`（T53C 已逐条 fetch 核到原文，12 系统全部 http URL + 原文摘录）。

## 0. 一句话

**公开 SOTA 分只能当"量级参照"，不能当"同题对标"——因为①它们是 bench 级平均分不是题级分，②RACE 是 0-100、F1 是 0-100、我们的 judge 是 0-1，③题目不同。真正的"打赢"必须在同一 judge 口径下本地复跑开源框架。**

## 1. 三层对标定义（本 bench 只用 L0 作判决，L1 作参照）

| 层 | 定义 | 可比性 | 用途 |
|---|---|---|---|
| **L0 主对标（判决用）** | 同一本机模型（Qwen3.8-27B @8787）驱动**开源 deepresearch 框架**（LangChain Open Deep Research / LangGraph react agent），跑**同一 5 题**，用**同一 B-face judge** 打分 | 完全可比 | 判"是否打赢" |
| **L1 参照对标（只作量级）** | 公开 leaderboard / 论文里的开源系统分（bench 级平均） | 不可比（异题、异口径、异 judge） | 判断"SOTA 量级在哪个区间" |
| L2 传闻 | 二手聚合站/无出处分 | — | 不采用 |

**判决：AC2"每题 ≥1 个开源 SOTA 基线的公开分数"只能以 L1 形式满足（5/5 有 L1 分），题级公开分 0/5 存在（这些题是我们自建或从公开集抽样，题级分数从未公开）。conf 0.95**

## 2. L1 公开 SOTA 分表（开源系统标 ★，数值 + 出处 + 摘录）

| 系统 | bench | 指标 | 分 | 开源? | 出处 |
|---|---|---|---|---|---|
| ★ LangChain Open Deep Research（backbone GPT-5） | DeepResearch Bench (100 题) | RACE overall | **50.60** | 框架开源（backbone 闭源） | https://proceedings.iclr.cc/paper_files/paper/2026/file/465f… |
| ★ Tongyi DeepResearch (30B-A3B) | DeepResearch Bench | RACE overall | **40.46** | **权重+框架全开源** | 同上 |
| ★ DeepResearcher (RL, Qwen2.5-7B) | DeepResearch Bench | RACE overall | **10.77** | 全开源 | 同上 |
| ★ Tongyi DeepResearch (30B-A3B) | GAIA text-only val | Avg@3 | **70.9** | 全开源 | https://arxiv.org/html/2510.24701 |
| ★ Tongyi DeepResearch | BrowseComp | Avg@3 acc | **43.4** | 全开源 | 同上 |
| ★ Tongyi DeepResearch | BrowseComp-ZH | Avg@3 acc | **46.7** | 全开源 | 同上 |
| ★ Tongyi DeepResearch | HLE | Avg@3 | **32.9** | 全开源 | 同上 |
| ★ Search-R1 (base, Qwen2.5-7B) | HotpotQA (512 dev) | F1 | **55.9** | 全开源 | https://arxiv.org/html/2504.03160 |
| ★ DeepResearcher (Qwen2.5-7B) | HotpotQA | F1 | **52.8** | 全开源 | 同上 |
| ★ DeepResearcher | 2WikiMultiHopQA | F1 | **59.7** | 全开源 | 同上 |
| ★ Search-R1 (base) | 2WikiMultiHopQA | F1 | **44.6** | 全开源 | 同上 |
| OpenAI Deep Research (o3) | GAIA val | pass@1 | 67.36 | 闭源 | https://openai.com/index/introducing-deep-research/ |
| Gemini-2.5-Pro DR | DeepResearch Bench | RACE | 49.71 | 闭源 | ICLR 2026 proceedings |
| OpenAI Deep Research | DeepResearch Bench | RACE | 46.45 | 闭源 | 同上 |
| Kimi Researcher | DeepResearch Bench | RACE | 44.64 | 闭源 | 同上 |

**口径警告**：RACE 是**相对分**（intra-model 相对评分），跨版本不可比（T53C contradiction X1 已记录）；F1 是短答案 EM/F1，与"长篇报告"不是同一任务（X4）；我们的 judge 是 0-1 rubric（0.5 数字 + 0.5 对比/单位）。

## 3. 五题 × SOTA 映射（L1 参照；L0 待本地复跑）

| # | qid | 题型 | 最接近的公开 bench | 该 bench 开源 SOTA（L1） | 口径可搬？ |
|---|---|---|---|---|---|
| 1 | `gpu`（已有，复用） | 硬件选型 + 多约束推理 | BrowseComp / HLE 类硬事实深挖 | Tongyi BrowseComp 43.4 / HLE 32.9 | ✗ 异题，仅量级 |
| 2 | `drb-2`（已有，复用） | 长报告横评（保险十强） | DeepResearch Bench（同源！） | LangChain ODR 50.60（RACE） | ✗ 同 bench 异题 + 异 rubric |
| 3 | `q6-nev`（新） | 多跳统计 + 口径（新能源产销/出口/份额） | GAIA 多跳事实整合 | Tongyi GAIA 70.9 | ✗ 异题，仅量级 |
| 4 | `q7-rd`（新） | 双实体比较 + 分母/财年口径 | HotpotQA 比较型多跳 | Search-R1 F1 55.9 | ✗ 短答案 vs 长报告 |
| 5 | `q8-nvda`（新） | 深挖 + 财年/地区定义 | BrowseComp 深挖 | Tongyi BrowseComp 43.4 | ✗ 异题，仅量级 |

**判决：5 题全部有 ≥1 个开源系统公开分（L1 层），但 0 题有同题同口径公开分 → AC2 按字面 5/5 通过、按精神 0/5 不通过；唯一有效判决来自 L0 本地复跑。conf 0.9**

## 4. Judge 口径（不变，来自 v2）

- **B-face**：qwen2.5-7b-original @ `localhost:1234`（`bface_score.py` / `drb_race_judge.py --judge local`），异族于生成端 Qwen3.8-27B
- **Rubric**：满分 1.0 = 0.5（核心数字正确）+ 0.5（对比/单位/百分比/口径正确）
- **聚合**：n=3 runs，取 **median**；单次分数不作判决（对抗 synthesis 方差，见 bench report #18/#19）
- **防泄漏 A6**：prompt/日志/中间产物不得含题面原文；run 落盘用 `question_sha1` 代替原文（本版新增强制项）

## 5. 本地复跑命令（L0，需在 pfb 主机执行）

```bash
# 生成端 8787 + judge 1234 都起来后
python3 experiments/stage-ablation/s5_pipeline.py --qs q6-nev,q7-rd,q8-nvda --reps 3 --out runs-s5-sm-b12
python3 experiments/stage-ablation/bface_score.py --runs runs-s5-sm-b12 --n 3   # 取 median
# 开源框架对照（L0 主对标）
# LangGraph react agent + 同一模型 + 同一检索 hook，跑同 3 题，同 judge
```

**未验证项**：`bface_score.py --runs/--n` 参数是否存在（本轮未读该脚本参数定义）——执行前先 `--help` 核对。`[待核验]`

## 6. 变更记录

- v1：验收定义（0-1 judge vs 本机模型）→ v2：加"开源框架同机复跑"主对标，声明公开分数不可用 → **v3（本版）**：补 L1 公开分表（12 系统）+ 三层可比性裁定 + 五题映射 + A6 落盘要求。
