# idea53 审计最终报告（微信线程 B/C 收口）

# origin: ai · 2026-11-25 04:50 · subagent sa-0-aa026ddc 产出（832s，04:45 被 stop，报告从 live 转录 salvage）
# 触发：D 微信 2026-11-24 10:25/16:09/20:25 三连问（arena 碰撞核查 + 免费 venue + 预印本平台）

## 三条结论（一行版）

1. **碰撞核查**：做过五轮（`arena/f8477718` @ 7dae6431a），但**全查旧 claim 域**（LLM 推理树/交叉梯度 MI 框架）；D 17:39 转向闭式数学（eb1b0598c）后**零轮针对最终 paper**。"NeurIPS'27 E&D P0.30 / workshop P0.55" 基于旧 claim 新颖性，**不可作最终 paper 的决策依据**。
2. **预印本**：未定案。arXiv 包就绪但 D 无背书（路 1 走不通，只能套磁找背书人或 workshop/OpenReview 先行）；D 20:25 追问无闭环。免费替代：GitHub commit hash（已在 repo，0 元防篡改锁时间戳）。
3. **paper**：数学内核可投（预注册合规 + 数字审计过），但 **0 引用、无 References 节、无 track 交付物**（E&D 要 eval/dataset）——"可打磨态"非"可投态"。

## 证据链

- 回执原文：`git show origin/arena/f8477718-prompt-first-bench:tasks/IDEA-review/result.md`（追加2/3/4 三节；**追加1/R1/R2 节缺失**——见下方完整性问题）
- 分支澄清：IDEA-review 在 `f8477718` 分支，**非** `78602cd5`（后者 tip 停在 11-24 12:11，无 IDEA-review 目录）
- 结论演化链：R1 conf 0.45 → R2 转发平凡性一击 → R3 conf 0.7（"链式域已撞：2601.23163 NeurIPS'26 E&D 已录"）→ R4 conf 0.6（"撞车三线占位 DDx 2602.03340 / UoT+BALAR / 步类型分类学；未见同构=树×类型×深度×交叉梯度，novelty 在测量协议不在概念"）→ R5 venue 概率（旧 claim 口径）
- 最终 paper：`tasks/idea53-goal/submission/paper.tex`（3946 行，9pp pdf，Related Work 段有 roofline/attribution 论述但 0 正式引用）
- 05-accept 状态：实质验收通过、程序未闭环（GOAL.md §6 5/6 勾，第 6 条 IDEA-INDEX #53 行实际已更新但未勾）

## 完整性问题（subagent 临终新发现）

result.md 现存节从"追加2（=第三轮）"开始，**R1 首轮 + R2 节缺失**。70dca8efa（02:05）的 commit message 声称"追加#53 撞车核验"，其 diff 确实加了 #53 节——**内容加过但被后续 rebase drop**（追加4 自曝过一次 rebase 丢失第五轮，这次是 R1/R2）。
- 影响：低。R1/R2 内容可从 `git show 70dca8efa:tasks/IDEA-review/result.md` 恢复，且其结论已被 R3-R5 覆盖。
- 处置：不重追加（旧 claim 域，对最终 paper 无决策价值）；在 arena 台账记一笔"rebase 丢节×2，内容可 git 恢复"。

## 三个待决（parent 编排）—— ①②③ 全闭环，剩 arXiv 投稿决策（等 D"投"）

| # | 事项 | 我的判断 |
|---|---|---|
| ① | 预印本路线 | **已闭环（2026-11-25 04:47）**：GitHub hash 时间戳已锁——孤儿分支 `idea53-preprint-ts-v3` @ `52d33c17`（2026-11-25 04:47:21 +0800），只含 submission/ 7 文件（paper.pdf/tex + body/header/formalism-skeleton + SHA256SUMS），零 WIP 泄漏，远程已验证 200。D 20:25 原话授权（"github 如果有 hash 防止篡改也行"）。arXiv 背书套磁 = 并行支线，不阻塞。 |
| ② | 对最终闭式 paper 重做 arena 碰撞核查（GPU 性能建模域） | **已闭环（2026-11-25 05:12）**：round6 回执 git 核验通过（commit bb387d43f @ arena/f8477718，result.md 追加5 节，指纹 6d50c871 ✓）。结论：未撞车（窄空白）conf 0.7；venue 排序 arXiv→ICML27 ML4Systems workshop (P≈0.5-0.6)→MLSys workshop (P≈0.5)→E&D 错配 (P≈0.05-0.08)；最难一击 + 三条件防守见 result.md 追加5。详见 collision-final-paper-firstpass-20261125.md 05:10 更新节 |
| ③ | 补 References（0 引用→≥15 条正式引用） | **已备好（2026-11-25 05:15）**：15 条全部已核验 bib @ submission-staging/references.bib（1df8c91d7），arXiv API + Crossref 逐条核验（非凭 agent 汇报）。并入 paper.tex 时机 = arXiv 投稿决策时（bundle 已锁 @ 52d33c17，改动需 D 确认节奏） |

## 时间戳锁记录（2026-11-25 04:47）

- 分支：`idea53-preprint-ts-v3`（孤儿分支，仅 7 文件）
- commit：`52d33c17ca8d8090520c41f0494dc09301b479ba` @ 2026-11-25 04:47:21 +0800
- 内容：`tasks/idea53-goal/submission/{paper.pdf, paper.tex, body.tex, header.tex, formalism-skeleton.{pdf,tex}, SHA256SUMS.txt}`
- 注意：v1/v2 两次误提交（孤儿分支索引未清，带入全 tasks/ WIP）已即时删除远程分支，最终版 v3 验证过完整树后才推
