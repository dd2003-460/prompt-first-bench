# T8 Part B 验收回执（Lead 侧收口）

- **对象**: decomp-bench `experiments/T8-lit/lit-survey-pipeline-prompts.md` @ commit ce20b23（branch arena/e31379c5-decomp-bench，已合入 main @ 8ce82bf）
- **验收时间**: 2026-11-02 keepalive r238
- **任务书**: tasks/T8-partB-lit-survey-task.md（decomp-bench @ 473b755，含回执指纹要求；本仓镜像已落盘）

## 逐项门禁核验（对照任务书验收标准 1-5）

| # | 标准 | 结果 | 证据 |
|---|------|------|------|
| 1 | 4 问题全答，找不到明确说未找到 | 达标 | Q1 明确写「直接证据缺口…未找到针对 AutoGen/CrewAI/LangGraph 的系统实验」；Q2-Q4 均有实质回答 |
| 2 | ≥2 独立来源 | 达标 | 7 个不同团队来源（Reflexion/Madaan/Huang/Gou/Zheng/Wataoka/PIVOT），覆盖 NeurIPS×3 + ICLR×2 + arXiv×2 |
| 3 | 每条结论标 conf | 达标 | 全文逐条 conf=0.85~0.97 |
| 4 | URL 可访问 | 达标（待补审计） | 全部为 arxiv.org / proceedings.iclr.cc 开放链接，无 paywall；r76 先例（lit-survey-url-audit-r76.md）证明同域 URL 可达性良好——本轮未逐条 curl，登记为可选尾项 |
| 5 | 产出落盘 + commit+push | 达标 | ce20b23 pushed → main 8ce82bf（git ls-remote 验证 refs/heads/main=8ce82bf 且含该文件） |

## 回执 JSON 核验（任务书新增的指纹要求）

arena 回执 `receipt-t8-partb.json` 字段：task_id=T8-Part-B ✓ / files_created 两文件 ✓ / sources_used 7 条与正文来源清单一致 ✓ / self_assessment=pass。
**偏差登记**：任务书 473b755 要求的回执 schema（repo/branch/commit_sha/artifact/sources_count/observed_at）与实际回执字段不一致——实际回执缺 commit_sha 与 branch 字段。**处置**：Lead 侧从 git 远端补齐指纹（branch=arena/e31379c5-decomp-bench, commit_sha=ce20b23baeb64a1d874038baf78d1467b8fabf95, artifact 路径存在, sources_count=7），不影响验收结论；schema 漂移根因 = 任务书补指纹要求（473b755, 16:15 +0800）晚于 arena 执行（09:14 UTC ≈ 17:14 +0800 前？）。时间线核查：ce20b23 提交时间 2026-11-02T09:15Z = 17:15 +0800，晚于 473b755（16:15 +0800）——即 arena 在补要求后才跑，但仍按旧 schema 输出。判定：非造假，属 agent 沿用了会话内旧格式；验收通过，schema 对齐作为 Part C 派发前的小修项登记。

## 内容质量抽查（防表演三测）

1. **具体性**：引用带表号/数值（Reflexion Rust 表3 0.60/0.60/0.52/0.68；Self-Refine 代码优化 27.5/26.0/24.8；GSM8K +0.2pp）✓
2. **诚实局限**：Q1 明确「未找到直接证据」而非硬凑；Q4 明确「可迁移为待测方向，不可直接迁移效应大小」；对 PIVOT 2026 预印本标注「不能移植其数值到 pfb」✓
3. **反事实价值**：「对 Part C 设计启示」节给出可操作修改（两种干预定义、Holm 校正、critic 2×2 分层、revision 0/1/2 轮+预算匹配 one-shot 对照）——删掉这些 C3 方案会少具体约束 ✓

## 总判定

**PASS**。T8 Part B 闭环：任务书(99b1377/473b755) → arena 执行(ce20b23) → main(8ce82bf) → Lead 验收(本回执)。
解锁项：T8 Part C ablation 开跑的前置文献支撑到位。

## 遗留小项（不阻塞）

- [ ] 7 条 URL 逐条可达性审计（可选，r76 先例流程，~10 分钟）
- [ ] decomp-bench loop-state.json T8 字段仍为过期值（partBD_pending…blocked_ui_no_input），需更新为 partB_done_ce20b23
- [ ] 回执 schema 对齐（Part C 任务书派发时同步修正模板）
