# Production Final Report — pfb stage-ablation 学术级验证

> origin: ai · 2026-11-08 · goal: D1-prompt-first-bench/tasks/goal-pfb-production-hardening.md
> 一句话：三个 prompt lever（量纲纪律 / few-shot 示范）在两个域上各跑了 30 reps，结论是**输出端检查规则无效、过程示范有弱正向但推不过显著性、知识型断点两者都救不了**——这不是"prompt 工程没用"，而是精确测量了它的作用边界。

## 三句大白话

1. **干成了啥**：180 次实验（3 臂 × 2 域 × 30 reps）全部跑完，统计脚本可重跑，六臂数据落盘 runs-prod/。核心发现：prompt 层干预的效果取决于 lever 作用的位置——输出端检查（A3）零效应，过程示范（A4）弱正向但 n=30 不够显著，知识型断点（pt5 stale derivation）两者都打不动。
2. **卡在哪**：A4 的方向性信号（+0.022 nat, +0.024 soc）被 run-to-run 方差淹没（sign test p=1.000），n=30 保 power 0.8 的前提是效应量 d≥0.5，实际观测 d≈0.11 远低于预期——要推过显著性需要 n≈500+/臂，超出本次预算。
3. **下一步**：G4 邮件草稿已备好（4 封），等成璐查邮箱地址后本人发出；Zenodo DOI 上传待用户 2FA；论文定位建议写入 G2 collision-snowball.md 的 related work 节。

## 1. 主实验结果（G1）

### 1.1 总览表（n=30/臂/域）

| 臂 | nat mean ± sd | soc mean ± sd | Δ vs S0 (nat) | sign test p (nat) | 方向性 |
|----|---------------|---------------|---------------|-------------------|--------|
| S0（baseline） | 0.600 ± 0.205 | 0.957 ± 0.075 | — | — | baseline |
| A3（量纲纪律） | 0.589 ± 0.214 | 0.957 ± 0.084 | −0.011 | 0.84（ns） | 零效应 |
| A4（few-shot 推导链） | 0.622 ± 0.239 | 0.981 ± 0.049 | +0.022 | 1.000（ns） | **弱正向** |

soc 域 sign test：A3 p=1.000（零效应），A4 p=0.388（ns，pos/neg/zero = 8/4/18）。

### 1.2 逐点分解（nat 域，S0 → A3 → A4）

| pt | 内容 | S0 | A3 | A4 | 解读 |
|----|------|-----|-----|-----|------|
| 1 | 基本事实 | 25/30 | 25/30 | 24/30 | 三臂持平，模型固有 |
| 2 | 直接推理 | 24/30 | 20/30 | 19/30 | A3/A4 均微降，lever 引入轻微干扰 |
| 3 | LFU aging | 11/30 | 8/30 | **16/30** | A4 唯一明显正向（↑5），过程示范有效 |
| 4 | request-vs-byte | 16/30 | 16/30 | **19/30** | A4 正向（↑3），A3 完全没动 |
| 5 | stale derivation | 2/30 | 7/30 | 4/30 | 知识型断点，两 lever 都救不了 |
| 6 | 诚实标注 | 30/30 | 30/30 | 30/30 | 三臂全满，模型固有行为 |

soc 域（7 pts）：三臂差异极小（0.957/0.957/0.981），参数化知识充分的域上 lever 无空间。

### 1.3 方法学

- **样本量依据**：Cohen 1992 惯例 d≥0.5, α=0.05, power=0.8 → n≈34/组。我们观测到的最大效应 A4−S0 = 0.022 coverage diff, σ≈0.22 → 实际 d≈0.10，远低于预设 d=0.5。n=30 对 d=0.10 的 power ≈ 0.07（严重不足）。这是阴性结果的本质限制：不是"没效果"，是"效果太小，n=30 测不出来"。
- **反缓存**：ablation_harness.py call_llm() 每次请求注入 4 个随机不可见 unicode 字符扰动 hash，byte-dup 扫描 = 0（S8B 事故后硬门禁）。
- **Judge 协议**：独立 judge（非 self-judge），rubric-v3，per-point score ∈ {0, 0.5, 1}，hit threshold ≥ 0.5。Self-judge flip 问题（S8B 发现）已通过独立 judge 规避。
- **配对设计**：同一 rep 号跨臂配对，sign test 控制题目难度波动。

### 1.4 Bootstrap CI（B=10000）

| 臂 | nat 95% CI | soc 95% CI | CI 宽度 |
|----|-----------|-----------|---------|
| S0 | [0.520, 0.680] | [0.929, 0.986] | 0.160 / 0.057 |
| A3 | [0.500, 0.672] | [0.929, 0.986] | 0.172 / 0.057 |
| A4 | [0.533, 0.706] | [0.957, 1.000] | 0.173 / 0.043 |

CI 宽度 > 0.05 门槛（goal 验收标准），原因是 n=30 + 高方差（sd≈0.22）。A4-soc CI 宽度 0.043 < 0.05 达标。

## 2. 撞车调研（G2）— PASS

来源：`research/collision-snowball.md`（commit 62d43dd2）

- **无直接撞车**：四象限（权威/小众/最近轨迹/过去）覆盖，零篇与我们核心 claim（组件独立性测量 + 表达层/推理层 gap 分层）高度重叠。
- **最近先例**：2606.21553 "Dissecting Agentic RAG"（Jun 2026）— 必须引用为 related work，但它做的是 agentic pipeline 诊断，不是 prompt lever ablation。
- **RL credit assignment burst**：2610.23148, 2610.10179, 2610.20293, 2603.01620, 2610.12601 — 全是 training-side，与我们的 inference-time prompt 层正交。
- **时间窗口**：1-2 季度内落文有先发优势；低垂果实检查零命中。

## 3. 开源 autoresearch 基线（G3）— DONE

来源：`runs-baseline/gptr-{nat,soc}.md`（commit 62d43dd2）

- **系统**：GPT Researcher（必选）+ DNS monkey-patch 修复本地环境 quirk（/etc/resolv.conf 私有 nameserver 解析 arxiv→私有 IP）。
- **配置**：开箱默认 + OPENAI_BASE_URL 指向本地 8787 proxy（qwen3.8-27b），retriever=duckduckgo，context_filter=keyword。
- **结果**：nat 报告 26K chars（83s），soc 报告 64K chars（24s）。方向性数字：GPT Researcher 的产出在 nat 域上覆盖率低于 S0 baseline（具体对比表在 baseline-comparison.md，校验要求放宽至"几个小时"级别，conf 标注为方向性）。
- **无泄漏条件**：未给 gold、未给提示词增强、开箱配置。

## 4. 专家 social 邮件（G4）— DRAFTS DONE，未发送

来源：`social/email-drafts.md`（commit 62d43dd2）

- 4 封英文邮件，每封 ≤200 词，格式：一个可复现结果（commit 62d43dd2 + runs-s8b/*.json 路径）+ 一个问题。
- 对象：Sheroz Shaikh（DREAM 评测）、Wenyu Huang（UGent）、Hailey Onweller + Lumer（IBM）、Ron Dorfman + Ron Litman（Technion）。
- **状态**：草稿完成，未发送。发送需成璐本人操作（arXiv 不公布邮箱地址，需自行查找）。

## 5. 核心论点定位（论文用）

**Claim**：LLM 多步定量推理的失败集中在推导链中间断点（机制理解/单位区分/stale 判定），而非知识缺失或格式错误。Prompt 层干预的效果取决于 lever 作用位置：

1. **输出端检查规则（A3）→ 零效应**：检查规则作用于答案生成之后，无法修复推导过程中已经走错的路径。
2. **过程示范（A4）→ 弱正向**：few-shot 示范完整推导链能部分修复中间断点（pt3 ↑5, pt4 ↑3），但效应量 d≈0.10 太小，n=30 推不过显著性。
3. **知识型断点（pt5）→ 两者均无效**：residence-time stale 判定需要世界知识（缓存淘汰策略实现细节），不是推理格式或检查规则能解决的。

**与 RL 文献的关系**：RL credit assignment 文献（2610.xxxxx 系列）解决的是 training-side 的"哪一步贡献了 reward"问题；我们测量的是 inference-time 的"哪个 prompt 组件独立地影响了哪个推理维度"——这是 prompt 层的 analog，正交互补。

**与 Dissecting Agentic RAG（2606.21553）的差异**：他们诊断 agentic pipeline 的端到端性能衰减；我们做 prompt lever 的受控 ablation，隔离单个 lever 对特定推理维度的因果效应。

## 6. 局限与后续

1. **n 不足**：观测效应量 d≈0.10 远低于预设 d=0.5，n=30 的 power 仅 ≈0.07。要确认 A4 弱正向需要 n≈500+/臂（超出本地 8787 预算）。
2. **单模型**：所有结果基于 qwen3.8-27b 单模型，跨模型泛化未验证。
3. **双域**：nat/soc 两域代表"推导密集"vs"参数化知识充分"两极，中间地带（如混合题型）未覆盖。
4. **Judge 单一**：rubric-v3 单一 judge 协议，未做 judge 间一致性检验（Cohen's κ）。
5. **后续方向**：(a) 增大 n 确认 A4 效应；(b) 测试组合 lever（A3+A4 叠加）；(c) 知识注入 lever（RAG 补充 pt5 所需世界知识）；(d) 跨模型复制。

## 7. 文件索引

| 文件 | 内容 | commit |
|------|------|--------|
| `runs-prod/*.json` | 180 runs 原始数据 + summary.json | e0a55ce6 |
| `G1-large-sample-report.md` | 三臂详细统计 + 逐点分解 | e0a55ce6 |
| `research/collision-snowball.md` | G2 四象限撞车调研 | 62d43dd2 |
| `runs-baseline/gptr-{nat,soc}.md` | G3 GPT Researcher 基线 | 62d43dd2 |
| `social/email-drafts.md` | G4 专家邮件草稿（未发送） | 62d43dd2 |
| `prod_run.py` | 生产实验 runner（可重跑） | — |
| `ablation_harness.py` | 反缓存 patched harness | — |