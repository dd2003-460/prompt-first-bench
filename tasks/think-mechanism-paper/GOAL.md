# GOAL: think-mechanism-paper（D 思考机制 → 可发表零成本论文）

# origin: ai · 2026-11-25 · D 指令"按照我的 idea 去写然后让 arena review"
# 模板 = idea53 的最小零成本可靠发表管线（tasks/idea53-goal/minimal-zero-cost-publication-decision-20261125.md）

## §1 目标

把 D 的思考机制（理解=压缩-解压往返无损不动点 + 4 侧面 + 2 推导 + 5 个可注入 general 思考模板）写成一篇**可发表、零成本、可靠**的英文论文。

**可靠 = 硬约束（优先级高于含金量，D 2026-11-25 原话"含金量低也没事，但是必须可靠"）**：
1. 每条引用真实可核验（arXiv API / Crossref 实查，回执落盘）
2. 论文里每个数字可回溯到落盘文件（语料路径/脚本），映射表随稿
3. claim 收窄到**有廉价真值的封闭部分**：描述性形式化 + 操作协议；不 claim 认知科学结论（"人类如何思考"）
4. 7/7 推导测试诚实标注 = 源语料内部一致性检验，**非外部验证**（构造与检验同语料 = 自指，必须写明）
5. AI use statement 入稿（TMLR 要求；arXiv 无强制但防封禁风险）
6. 无"首次/无人做过"类措辞（arena Q5 红线，idea53 先例）

## §2 阶段

| 阶段 | 内容 | 执行 |
|---|---|---|
| 01 decomp | 本文件 + decomposition.md | Lead（已完成） |
| 02 起草 | 英文 LaTeX（底本=D1-persona-align/memory/ 两份源文件） | subagent |
| 02.5 引用核验 | 逐条 arXiv API/Crossref 实查，回执 JSON | Lead（terminal，sub 无网络） |
| 03 arena review | Q1 novelty/Q2 逻辑/Q3 可证伪/Q4 venue/Q5 致命措辞 | Lead 派发（ego-browser，纯 review 会话 GitHub 绑定关） |
| 04 修订+编译 | 按 arena 报告修订，改动引用重验 | subagent |
| 05 时间戳锁 | 孤儿分支 + SHA256SUMS（idea53 v4 模式） | Lead，**等 D"投"** |

venue 决策（已定，沿 idea53 模板）：arXiv（免费锁时间戳，主）+ TMLR（0 元真评审，次，rolling 无截稿）。不投 ICLR tiny track（AI-generated 明文禁令）。

## §3 SOP 索引

- 起草/修订：lead-context-budget（执行细节派 sub，Lead 只验收 claim 措辞）
- arena 派发：`.claude/skills/arena-outsource/SKILL.md`（门禁五条 + tiptap 坑 + 会话台账）
- 引用核验：arXiv API 走 https + 失败重试（memory 11-21/11-24 踩坑记录）
- 数字审计：workshop-number-audit skill（24 条检查）

## §4 验收标准（机器可查）

- A1: `draft/paper.tex` pdflatex 编译 0 error，8-15 页，0 undefined citation
- A2: `receipts/citations-verify-<date>.json` 存在，100% 引用有 URL+核验时间，Lead 独立复算
- A3: `draft/number-trace.md` 存在：论文每个数字 → 源文件路径/命令
- A4: `arena-review-report-raw-<date>.md` 归档 + Lead 抽验 ≥3 条 arena 引用 ID
- A5: grep 论文无 "first"/"no one has"/"unprecedented"（除非限定语境）；7/7 处含 "internal consistency" 限定词；AI use statement 存在
- A6: 全程 0 费用（无注册/版面/差旅）

## §5 失败降级

- arena 不可用 → 修复清单 7 步（skill）→ 降级 ego-browser 网页 LLM ≥2 独立源交叉（回执标降级）
- 起草质量不达标 → claim 再收窄（砍应用节，保核心+推导+模板）
- 引用核验发现编造 → 该引用删除或替换，不硬凑
- TMLR AI 披露政策不确定 → 只投 arXiv，TMLR 等政策明确（不阻塞）
