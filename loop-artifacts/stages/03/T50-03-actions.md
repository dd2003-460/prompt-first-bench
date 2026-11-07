# T50 B1 新题 Gold Tree（Q8/Q9/Q10）— 阶段 03 行动分解

> 创建：2026-11-07 · 阶段：03 · 依据：02/02.5 证据边界 + `loop/prompt-first/03-action-decomposition.md`
> 候选集沿用阶段 01 冻结（Q8/Q9/Q10 三题、四交付物类型），无漂移。全部步骤 owner=agent（本沙箱无 user 交互步骤；push 依赖沙箱 GitHub 凭据，属既有配置非 user 阻塞点）。

---

## 1. 步骤表

| # | owner | 动作 | 输入 | 依赖 | 产出 | 验收方式 |
|---|-------|------|------|------|------|---------|
| A1 | agent | 写 Q8 题面 `bench/questions/Q8-eval-benchmark.txt` | Q6/Q7 题面结构（头注释字段 + preamble + 「问题：」行）、任务书 Q8 题面方向 | — | 题面文件 | 非空；含「问题：」行；`extract_question()` 正则可提取非空段（python 实测） |
| A2 | agent | 写 Q9 题面 `bench/questions/Q9-vlm-arch.txt` | 同上 | — | 题面文件 | 同 A1 |
| A3 | agent | 写 Q10 题面 `bench/questions/Q10-rlhf-align.txt` | 同上 | — | 题面文件 | 同 A1 |
| A4 | agent | 写 `bench/rubric-v3/ablation/gold-Q8.md` | 02 §1 证据 S1-S12、02.5 C3/C4/C5 处置、gold-Q6.md 结构（结论先行/全树/图例/★判断/黑盒表/OC-1 卡片×3/算例/来源表/找不到节） | A1（题面路径引用） | gold tree | grep：`N-` 编号 ≥30、`leaf` ≥10、编号深度 ≤4 段；顶部独立调研声明；每叶子有数值/区间+来源；算例可复算（pass@k 公式代入自检） |
| A5 | agent | 写 `gold-Q9.md` | 02 §2 证据 S13-S24、02.5 C-一致性表、U2/U3 封顶 | A2 | gold tree | 同 A4；GPT-4V tiling 叶子 conf ≤0.8；Gemini 1.0 不引具体数值 |
| A6 | agent | 写 `gold-Q10.md` | 02 §3 证据 S25-S34、02.5 C1/C2 处置（β=0.02、对齐税条件化区间、[待核验] 标注） | A3 | gold tree | 同 A4；**全文 grep 无 "β=0.2" 作为 KL 系数的表述**；对齐税叶子为条件化区间表 |
| A7 | agent | `ablation_harness.py` QUESTIONS 增 Q8/Q9/Q10 | Q6/Q7 条目格式（domain/prompt_file/gold_file/search_query，PFB 常量） | A1-A6（路径存在） | dict 3 条目 | `python3 -c "import ast; ast.parse(...)"` 通过 + grep `"Q8"` `"Q9"` `"Q10"` 命中；路径 join 后文件存在（python 实测） |
| A8 | agent | `research_hook.py` ARXIV_QUERIES 增 Q8/Q9/Q10（每题 1 条精准 query，任务书要求）；同步补 KNOWN_SITES + FILTER_KEYWORDS（G6 决策：Q6/Q7 先例两 dict 均有，补齐保持 hook 行为一致，超任务书最小集部分在 04.5 披露） | Q6/Q7 条目格式、02 来源 URL | A4-A6（gold 内来源表定稿后选 KNOWN_SITES） | dict 3+3+3 条目 | ast.parse 通过；ARXIV_QUERIES 三 key 命中；FILTER_KEYWORDS 存在保证 S2+ 臂来源过滤生效 |
| A9 | agent | 验收自查脚本：逐项跑任务书 checklist（存在性/非空/grep 计数/dict key/独立声明/不改禁改文件） | 任务书验收标准 | A1-A8 | 自查输出 | 8 项全过；`git diff --stat` 确认未触碰 Q1-Q5 / score.py / score_s10.py / gates.py |
| A10 | agent | commit（message 含 "T50"）+ push origin arena/5c63a992-prompt-first-bench | A1-A9 + 全部 loop-artifacts | A9 | git commit | `git log -1` message 含 T50；push 后 `git ls-remote` 分支头 = 本地 HEAD |

## 2. 并行/串行

- A1‖A2‖A3 可并行（互不依赖）；A4/A5/A6 各依赖对应题面；A7/A8 依赖 A1-A6；A9→A10 严格串行收尾。
- 实际执行为单 agent 顺序写文件，并行性仅影响失败隔离（某题失败不阻塞另两题 → 降级 T50-partial 的判断点在 A9）。

## 3. 失败路径与停止条件

| 失败 | 替代 | 停止条件 |
|------|------|---------|
| 某题 gold 计数不足（<30 节点/<10 叶子） | 在该题既有主干上补真实分支（禁止灌水节点：每个新增节点须有证据或黑盒表条目支撑） | 补 2 轮仍不足 → 落盘现状 + 标 T50-partial |
| python ast/实测失败 | 修语法重跑（最多 2 次，循环防护） | 3 轮未过 → 回退该文件改动，单独 commit 其余 |
| push 403 | 重试 1 次 → 记录报错全文 | 仍 403 → 全部工件已 commit 本地分支，报 Lead（SOP §3.3；不静默） |
| 叶子数值缺可靠来源 | 标 [待核验] + conf 0.2（任务书红线：不编数） | — |

## 4. 风险预登记

- R1：gold-Q6 结构要素多（8 节），漏节 = 格式不达标 → A9 自查表逐节 grep。
- R2：节点计数口径歧义（N-0 算不算 / split 节点算不算）→ 采用 gold-Q6 自报口径（41 节点含 N-0 与全部 split；15 叶子 = leaf 标记数），A4-A6 目标定 ≥32 节点 / ≥12 叶子留余量。
- R3：题面语言风格漂移（Q8-Q10 是调研设计类，非 Q6/Q7 算账类）→ preamble 逐字复用 Q6/Q7 模板段，只换「问题：」后正文与头注释。

**阶段判定：pass**（步骤覆盖 D1-D6 全部交付物；每步有产出+验收；依赖无环；失败路径齐；另一执行者可照单执行）
**repair_stage：none**
