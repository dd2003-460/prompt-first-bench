# PFB 文献覆盖索引（根目录只当索引 · 2026-11-12）

> origin: ai。约定（成璐指令）：调研结果直接放对应子模块的 `litsurvey/`，本文件只描述
> 每个大领域"被做过多少 + 还剩什么没做"。百分比口径 = 该领域核心问题清单中已有落盘答案的占比。

## 总览

| 模块 | 覆盖 | litsurvey 现状 | 剩余内容（未做/待核验） |
|---|---|---|---|
| A-eval-infra | ~70% | prior-art-eval-bench（10 bench 对照 + judge 协议 + 空白区确认） | ResearchRubrics 作者、DR Tulu id、BrowseComp/SimpleQA/RAGAS 无 arXiv 仅技术报告；「prompt 因果消融是空白」是弱推断，需 arena 交叉验证 |
| B-pipeline-ablation | ~40% | （空——臂设计文档还在 experiments/stage-ablation/，B3 批次迁移时归位） | S 系列各臂的公开对标物未单独调研（竞品事实散在 competitor-survey.md） |
| C-objective-goodhart | ~50% | text-objective-goodhart-survey + v17-hier-decomposition-blowup（历史资产迁入） | Goodhart 防御的理论框架综述未做（F 线 §4 有初步结论：Skalse 定理 + 3 种 hacking 模式，但没成独立 survey） |
| D-decomp-state-machine | ~60% | sm-* 五份 SOP/日志（历史资产迁入） | decomp 状态机本身的 prior art 未系统调研（最接近的是 ODR+/DR Tulu，见 A 报告 Q2）；D35 四文献簇已派 arena（T53-D35-arena-task.md），回执未到 |
| E-sota-benchmark | ~80% | prior-art-sota-systems + closed-sota-v3 + drb-leaderboard×2 + sota-table（本轮补完） | GAIA/HLE/BrowseComp 各 DRA 单项分数 [待核验]；arXiv:2601.06007 成本数值 [待核验]；GR n=10 空壳建议正式报告前复跑固化 |
| F-theory/gradient-descent | ~65% | prior-art-prompt-optimization（conf 0.78，9 工作 × 4 问 + 设计启示） | "无 prior work 讨论 prompt-induced drift" gap 判断 conf 0.70 待 arena 交叉验证；AdaPrompt 具体 id [待核验]；GEPA full text 未读 |

## 跨领域共性缺口（拼回去看漏）

1. **检索通道稳定性**——drb-2 judge total=0.0（53/62 degraded）与 GR 6/10 空壳同模式：ego-browser 通道不修，所有泛化 bench 的 verified 率都上不去。这不是文献缺口，是执行层硬依赖。
2. **两个 gap 判断都是"搜了没找到"级证据**（A 线的 prompt 因果消融空白、F 线的 drift 无人处理）——按红线 1 应外包 arena 多引擎交叉验证后才能当行动前提。
3. **B 模块是唯一没有 litsurvey 的**——它的对标物其实是 A+E 两份报告的交集（现有 bench × 现有系统的管线层面比较），等 B3 迁移完成后可从 competitor-survey.md 拆出来。

## 更新纪律

- 新调研落盘到对应 `modules/*/litsurvey/YYYY-MM-DD-主题.md`，同步更新本表覆盖率和剩余列。
- [待核验] 项被 ego-browser/arena 确认后去掉标记并标来源。