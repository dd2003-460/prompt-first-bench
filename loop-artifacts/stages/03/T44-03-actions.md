# T44 · Related Work Update (Nov 2026) — 阶段 03：具体行动分解（actions.md）

> 创建时间：2026-11-06 UTC · 阶段：03（行动分解）
> 规则包：`loop/prompt-first/00-common-review.md` + `03-action-decomposition.md` + `04-execution-verification.md`
> 上游输入：`loop-artifacts/stages/01/T44-01-goal-decomposition.md` + `stages/02/T44-02-research.md` + `stages/02.5/T44-02.5-crosscheck.md`

---

## 1. 行动前提锁定（仅基于已过 02.5 核验的证据）

1. **定稿新增文献集（17 篇，编号 `[Ref 32]`–`[Ref 48]`，接续 `paper-draft.md` 既有 `[Ref 1]`–`[Ref 31]`）**：
   - **D1 Agent Benchmarks（3 篇 → §2.1）**：Park et al. (2026, `arXiv:2609.34428`), Yu et al. (2026, `arXiv:2610.25954`), Zhao & Raissi (2026, `arXiv:2608.11232`)。
   - **D2 Prompt Structure Ablation（3 篇 → §2.2 & §2.6）**：Dominici et al. (2026, `arXiv:2610.31639`), Khan et al. (2026, `arXiv:2610.29073`), Jia & Mu (2026, `arXiv:2609.25366`)。
   - **D3 LLM-as-Judge Reliability & Bias（4 篇 → §2.4 & §2.6）**：Ayyagari (2026, `arXiv:2609.33044`), Chae et al. (2026, `arXiv:2608.18091` / `DOI: 10.18653/v1/2026.findings-emnlp.1571`), Kumar et al. (2026, `arXiv:2610.12083` / `DOI: 10.18653/v1/2026.aacl-long.207`), Yin et al. (2026, `arXiv:2610.24320`)。
   - **D4 Deep Research Agents（3 篇 → §2.1 & §2.5）**：Polshkov et al. (2026, `arXiv:2608.14747`), Zhu et al. (2026, `arXiv:2607.20891`), Liu, Sun, & Tan (2026, `arXiv:2609.39154`)。
   - **D5 Calibration 2026 H2（4 篇 → §2.3）**：Hsiao (2026, `arXiv:2609.10996`), Ghosh et al. (2026, `arXiv:2610.25846`), Xu, Liang, et al. (2026, `arXiv:2609.00935` / `DOI: 10.18653/v1/2026.emnlp-main.389`), Schwager et al. (2026, `arXiv:2611.07735` / `DOI: 10.18653/2026.wnut-1.7`)。
   - *时间分布核对*：2026-09~11 共 **14 篇**（≥8），2026-07~08 共 **3 篇**，合计 **17 篇**（≥8）。
2. **文件边界原则**：按任务书「产出 `loop-artifacts/stages/04/T44-related-work-update.md`：新增引用列表 + 建议修改文本（直接可贴进 paper 的段落）+ 矛盾/张力清单」，不擅自覆写冻结稿 `experiments/stage-ablation/paper-draft.md`，而是在 `T44-related-work-update.md` 中给出**带行号锚点的逐节可直接粘贴替换/追加英文段落 + 编号 #32–#48 References 条目**，供 Lead 一键合入。

---

## 2. 原子化执行步骤表（含依赖、并行性与 Owner 标注）

> **Owner 声明**：全部步骤 `owner = agent`（无同步或异步 `user` 阻塞点；GitHub 认证已在沙箱预置）。

| 步骤 ID | 动作（原子任务） | 输入 | 依赖 | 可否并行 | Owner | 预期产出 | 验收方式（机器可检） |
|--------|----------------|------|------|---------|-------|---------|-------------------|
| **S1** | 编写主交付物 `loop-artifacts/stages/04/T44-related-work-update.md`（含：① 17 篇新增引用总表［作者/年份/arXivID+DOI/竞品分类/一句话定位/§2 小节映射］；② §2.1–§2.6 可直接贴入 `paper-draft.md` 的英文建议修改段落 + 新增 References `#32`–`#48` + 原稿 Ref #6 副标题顺带勘误提示；③ T1–T6 六条矛盾/张力清单与五维归因） | `T44-02-research.md`, `T44-02.5-crosscheck.md`, `paper-draft.md` L27–65 & L347–380 | — | 串行起点 | `agent` | `loop-artifacts/stages/04/T44-related-work-update.md` | 文件存在且非空；包含全部 3 大核心模块 |
| **S2** | 运行一次性 Python 校验命令（不落地脏临时文件），对 `T44-related-work-update.md` 做硬约束核验：① 新增独立引用数 ≥8；② 每条均含合法 `arXiv:26XX.XXXXX` 或 `10.xxxx/` DOI；③ 与 `paper-draft.md` 现有 31 篇 arXiv/DOI 零重合；④ 全部 17 篇均在建议英文段落及 References `#32`–`#48` 中双向闭合无孤儿引用；⑤ 英文增量词数统计（确保合入后 `paper-draft.md` 总词数仍 < 8,000） | `T44-related-work-update.md`, `paper-draft.md` | S1 | 否（依赖 S1） | `agent` | 终端校验 JSON / 统计摘要 | Python 断言脚本 `exit 0`，5 项计数全部达标 |
| **S3** | 落盘阶段 04 执行记录 `loop-artifacts/stages/04/T44-04-execution-log.md`（粘贴 S2 真实命令与回执输出，对照三道闸闸 1/闸 2 自检） | S1 产物 + S2 终端回执 | S2 | 否（依赖 S2） | `agent` | `loop-artifacts/stages/04/T44-04-execution-log.md` | 文件存在，包含真实命令输出与逐项验收核对表 |
| **S4** | 落盘阶段 04.5 反方最终复核 `loop-artifacts/stages/04.5/T44-04.5-review.md`（对照 `04.5-final-review.md` + `loop/modules/gates-postcheck.md` 三道闸做全链路反方挑刺与交接检查） | `stages/01..04` 全部工件 | S3 | 否（依赖 S3） | `agent` | `loop-artifacts/stages/04.5/T44-04.5-review.md` | 文件存在，涵盖证据链闭环、残余风险（如 5 篇 10 月下旬预印本未经同行评议、WANDR 厂商背景）及下一步交接动作 |
| **S5** | 检查工作区干净度（确认无临时垃圾文件，仅包含 `loop-artifacts/stages/` 下 T44 的 7 个受控 Markdown 文件），执行 `git add`、`git commit -m "T44: related work update Nov 2026"` 与 `git push origin arena/de827540-prompt-first-bench`，并用 `git status` + `git ls-remote` 验证远端同步 | `stages/01..04.5` 全部 7 个文件 | S4 | 否（依赖 S4） | `agent` | Git commit hash + 远端分支更新回执 | `git push` 返回 `exit 0`；`git ls-remote origin refs/heads/arena/de827540-prompt-first-bench` 等于本地 `HEAD` |

**依赖 DAG**：`S1 → S2 → S3 → S4 → S5`（单链无环，全部 `owner=agent`，无 `user`/`agent` 混排歧义）。

---

## 3. 失败替代路径与停止条件

1. **若 S2 机检发现孤儿引用、ID 拼写不一致或总词数超标**：立即在阶段 04 内修订 `T44-related-work-update.md` 并重跑 S2（最多重试 2 次），严禁带着未闭合引用进入 S3。
2. **若 S5 `git push` 遭遇 HTTP 403（如 `sop/arena-loop-pipeline.md` §3.1 历史记录中部分会话曾遇 GitHub App token 只读限制）**：
   - 第一步：检查 `git remote -v` 与 `gh auth status` 诊断原因（最多尝试 1 次替代推送如 `gh api` 检查权限，不死循环重试）；
   - 第二步：保留本地完整 commit，在最终回复中向 Lead 如实报告具体错误码、本地 commit SHA 与全部落盘文件路径，绝不掩盖推送失败。

---

## 4. 阶段 03 门禁自检（对照 `03-action-decomposition.md` 质检标准）

- [x] **覆盖全部目标**：交付文件、1-loop 全阶段落盘、机检断言、三道闸复核、指定 commit message 与 push 全覆盖。
- [x] **原子性与可验证性**：S1–S5 每步对应单一明确工具动作与确定性 `exit code` / 文件验收条件。
- [x] **依赖无环且显式标注 Owner**：全部标明 `owner = agent`，无阻塞歧义。
- [x] **关键退路明确**：针对机检不通过与 GitHub push 403 预设了清晰退路与停止门。

**阶段 03 自检结论**：行动计划可执行、无未核验前提（status: pass → 推进至阶段 04 执行与验证）。
