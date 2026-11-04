# T8 C3-v3 fullloop 异源 judge r270 — Arena 派发记录

# origin: ai

## 派发时间
2026-11-04 ~23:35 CST

## 通道
ego-browser → arena.ai agent mode，会话 `01a1a72f-19a8-73c9-93e0-0748500a5339`
URL: https://arena.ai/agent/01a1a72f-19a8-73c9-93e0-0748500a5339

## 关键发现（推翻旧结论）
- **Arena 登录态实际可用**：cookie `arena-auth-prod-v1.0` 存在，页面正常加载。此前"无登录态"诊断错误——真实原因是 ego_lite 的 profile 是另一个浏览器实例，与之前登录用的不同。当前 ego_lite 实例已带登录态。
- **Arena 不透露底层模型身份**（agent 自述规定）。异源性以判分过程为准，无法用"非 Qwen 自报"做硬证明——这是 arena-outsource SOP 需要补的坑。

## 执行约束
- 会话绑定的是 d1-video-recreation 仓库（arena/500a5339 分支），不是 prompt-first-bench。
- Agent 系统规则不允许跨仓库推送 → 采用选项 A：结果写到 d1-video-recreation 的 `outputs/hetero-judge-r270/`，push 到 `arena/500a5339-d1-video-recreation`，之后手动拷贝回 pfb。
- 输出文件：`receipt-r270-hetero-dual-judge.jsonl` + `summary.md`（r269 原文件保留不动）。

## 任务内容
18 份 stage 工件 × J1/J2 双判官逐条目审计（36 cell）+ G2 spread 复算 + κ（vs 本地 qwen3.8-27b 双判官）+ r268 同源基线逐格对照。
任务书：pfb `tasks/T8-C3v3-hetero-judge-task-brief.md`（agent 通过 gh api 读取成功）。

## 盲判披露（agent 自述）
Agent 为确认文件结构打印了 receipt-r269-local-dual-judge-summary.md 前 ~1500 字符（含部分本地 qwen 分数），对这部分非盲判；未读 r268 分数文件。

## 状态
RUNNING（23:35 开始执行，agent 正在跑判分）

## 后续动作
1. 轮询 github dd2003-460/d1-video-recreation 分支 `arena/500a5339-d1-video-recreation` 的 `outputs/hetero-judge-r270/`
2. 完成后拷贝回 pfb runs-fullloop/，commit pfb
3. 更新 T8 task brief 状态

## 完成（2026-11-04 ~23:47 CST）
- commit: `T8 C3v3 heterogeneous dual-judge r270` @ d1-video-recreation `arena/500a5339-d1-video-recreation`
- 已拷回 pfb `experiments/T8-matrix/runs/c3-v3/runs-fullloop/hetero-judge-r270/`（36 行回执 + summary + work/）
- **核心结果**：异源 judge 与本地 qwen 基本不一致（J1 κ=−0.030，J2 κ=0.185）；异源明显更严（J1 总通过 30.7% vs 同源 89.7%）；S01 分解类工件 J1 通过率 0.6% = rubric 效度问题非质量差；G2 同口径 11/12 PASS 但口径本身无信号力；r268 的 0.931 spread 被证明是同源 judge 不稳定性。**不建议据此升档 T8 conf。**
- 披露：agent 盲判前读了 arena-hetero-judge-summary.md 头部 ~1500 字符（含部分本地分数）；事后修正 1 条判定（A-full/D2/S02 G1 pass→fail）；手工逐条判定非程序化调用，不可脚本重放。
