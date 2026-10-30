# CONTINUE_MSG — pfb 工作区

## 当前状态 @ 2026-10-30 21:28 +0800（keepalive r20/r21 续跑）

**r20 claude (PID 75102) 已收口退出（max-turns 200 耗尽，正常）**：单轮连推三个 goal 全部 merge main——r146 RV3G3cdx-queue-hygiene-sweep（main @ 16b063f）→ r147 RV3G3cdx-batch2-schema-lint（--lint-only 入口落地，main @ 0bb55ce）→ r148 RV3G3cdx-closure-checklist-assert（assert-closure-checklist.py 落盘，main @ 84ff11d）。

**r21 claude (PID 82143) 在跑（~27min），已连推两个 goal 并正在开第三个**：r149 RV3G3cdx-queue-dedup-lint（assert-queue-lint.py 三分支 + 七样例矩阵 7/7；收口时前序 commit 漏翻 checkbox 被自家新门禁 assert-closure-checklist.py 首战拦截 → 补做翻转 commit 8d7ce8b，工具自证价值，main @ 8d7ce8b）→ r150 RV3G3cdx-crossdomain-lint-coverage-expand（crossdomain 脚本扩展键集检查+prompt_version 最小消费 + 四新负样例持久落盘 + 9/9 FAIL 出口矩阵全核对 + 八脚本基线零漂移，main @ f7d3674）→ 当前正写 r151 RV3G3cdx-queue-format-contract 阶段 01。等 max-turns 耗尽或进程退出后验证收口 → 取下一个可做 goal（closure-gate-integration 为剩余最高优先纯仓库内项）。

**RV3G6-gmr-caliber-u3 goal 收口（六阶段全过，merge main @ efbbca7 = r124）**：
- U3 口径裁定落地：AUDIT §3.2 L103 / §5 L166「gmr 6.4→8.6」独立复算（冻结 JSON，0-based 协议）显示 G3 F3b L48 全部 7 列 = 冻结 gmr 复算值 +1.0（rank 起点差）→ 判定为 G3「gold 平均排名」口径（1-based rank 记法）被 AUDIT 误标为 gmr，**非 global gmr 数值错误**（6.4/8.6 在其自身口径下数值正确，不触发二次勘误）
- 走加注路径（二选一之「其他口径」）：L103/L166 保留原值 + 就地加 1-based 口径注记与冻结 0-based 等价值 5.40→7.60；U3 段转「已裁定项」
- 定性结论零改动且序关系更清晰（7.60 < 9.80 < 10.20 逐对不变）；assert-audit8-erratum.py 扩展检查组⑤（11 断言）32 PASS/0 FAIL + 变异测试确认实义；冻结数据零修改
- web-llm unverified：`ralph prompt-first web-llm` 报 `[Errno 2] .../pfb/ralph-loop.md` 缺失（连 provider 调用都未发生）→ 导出 RV3B1-webllm-tool-fix 候选（优先级高于 receipt-per-goal）

## 下一步（按优先级）

0. **P0 · r21 收口验证**：claude (PID 82143) 跑完 r151 (queue-format-contract) 或 max-turns 耗尽退出后——查 `git log main..HEAD` + 六阶段工件齐不齐 → 验证 merge main + push → queue 划掉+结果注记 → 立即取下一个 goal（closure-gate-integration）。若进程死亡且 r151 未收口 → 读 /tmp/ralph-loop-r21.log 定位，简化 prompt 重试一次
1. **P1 · C3 v3 paired runs**（WORK_QUEUE 最高优先未完成项）：前置 G1 subagent 盲标+仲裁 → G2 judge 实测 → G3-G5 门禁；ninfer HTTP :8000 直跑（不走 arena）。阻塞：judge 家族隔离（ninfer 只有 qwen3.8-27b）等用户决策
3. **P2 · 回 arena 会话 01a18567 取 307 行 survey 原文回填 research/interpretability/literature-survey.md**
4. **P2 · 评估 :8787 node 网关容量竞争根因**（cron 400 too large 元凶），决定是否切直连 :8000
5. **P2 · rubric-v3 遗留 #1「独立 judge 盲测 p̃」**：决定性检验，需 ≥3 个独立 LLM 服务盲估 31 节点 p̃ 对照 prior-estimates.json 算一致性——另开 goal

## 阻塞项

- **judge 家族隔离**：ninfer 只有 qwen3.8-27b（Qwen 家族），C3 v3 的 G2 judge 实测需异源 → 等待用户决策
- **web-llm 三 provider 登录态失效**：perplexity/chatgpt/gemini 全部 error → 需人工浏览器登录（一次性 web-llm-authorize）；各 goal 按失败降级继续（r124 已在 02.5 工件标注 unverified）
- **ralph CLI 入口文件缺失**：`ralph-loop.md` 在工作树与 git 历史均无，web-llm 工具完全不可用 → 见 RV3B1-webllm-tool-fix
- **R5.2-third-scorer 外部依赖**：需 arena 通道或第三本地模型（不同家族）
- **σ_d 无先验数据**：MDE/n_task 反推待 pilot 数据

## 分支状态

- main @ efbbca7（r124 gmr-caliber-u3 merge）；注意 r143 (44b31f0) 在 ralph/rv3g6-kappa-formula-adjudicate 分支上未 merge，等 r18 收口验证后 merge
- ralph/rv3g6-gmr-caliber-u3 @ 0ca6d30（收口分支，可删）
- 历史收口分支（r112-r123 系列，均可删）：ralph/rubric-v3-audit-g1..g5 / ralph/rv3g6-* 等