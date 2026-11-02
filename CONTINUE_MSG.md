# CONTINUE_MSG — 2026-11-03 r258

## 本轮完成 (r258)
**research-prompt retest-32k 对照实验（@ f45911b pushed）**：
- 动机：R0.5 ×3 (max_tokens=16000) 全崩被初判为模型随机崩塌，但 R0.3 run 输出 30-36K chars 却完整收尾——参数语义存疑
- 固定 prompt/temp 只改 max_tokens=32000 重跑 3 次：runA 完整收尾（五节 5/5 + SELF-CHECK 覆盖全部 4 叶子节点），runB/runC 仍停草稿
- **修正归因**：崩塌率 3/3→2/3，与 max_tokens 配置交互而非纯模型随机；后续消融轮次 run 脚本须统一 max_tokens=32000（服务器上限 32768，40000 实测 HTTP 400）
- COMPARISON.md 关键发现 #2 加修正注记 + retest-32k/ 目录落盘（README + runA/B/C）+ loop-state 更新
- 注意：runA 研究路径退化为 4 个平铺一级节点（无 R0.3 的三级树深度），S3 满分靠 SELF-CHECK 全覆盖不是拆解深度——lead 复核 S1/S2 大概率降档

## 上轮完成 (r257)
**research-prompt R0.4 中期评分（@ f58e3ee pushed）**：
- score-v2.py 机械评分器落盘（S3/C2 自动定档 + 8 维信号供 lead 复核，判据与 R0~R0.3 对齐）
- run1 **FAIL**：草稿区写到一半截断（23K chars），五节结构 0/5 —— max_tokens=16000 对 R0.4 的草稿+五节双段结构不够用
- run2：S3=2（新契约生效——5 个叶子节点全带 SELF-CHECK 行，前四版都停在 1 分档）；C2=1（TCO 对比表有数值但缺 Prefill(s)/Decode(s) 独立两列，按 R0.4 契约不得满分）
- run3 进行中（run-r04.py 串行循环 @ :8787，每 run ~76s+）
- 中期结论：S3 短板修复确认；C2 短板未修复（强制语写在第 3 节格式说明里离填表位置太远，TCO 表先满足了「有数值表」的心理预期）

## 上轮完成 (r256)
**decomp T21 收口联动**：flagship-eval S3 按 T21-RR 实测锚定重算（混合 [26.8,32.5] tok/s，云租优势修正），主报告 §9.2 发现 5 并入，decomp @ d1edf93，GPU 选型主线闭环。

## 历史完成
**M8-cover 口径对齐（pfb @ main a4fb25d，ralph/m8-cover-caliber-reconcile）**：
- 上轮 r254/r254b 已收口 v3 rubric（AC4 移出验收，overall_pass=True），但「下一步 #4 M8-cover 口径对齐（P2）」未动。
- 本轮执行：把 receipt-r7-cover-recompute.json（r241, 95b17c3）的 loose-keyword 独立复算数字回填 matrix-v11.md——新增 r254c 节（9 config × R5 D3 / R6 D1D2 双轮均值 cover 对照表 + gap 定性 + 方法后缀口径声明）。
- 顺销 matrix-v11.md L43 过期「待裁定」行（空分母口径 + cover 门槛 -0.05 早在 r62z 已裁定保守口径，该行一直没更新）。
- 零 LLM 调用纯复算；核心结论不受影响（freeze task-type-dependent 反转、truth+cover 联合判读要求均不变）。

## 当前状态
- pfb @ main a4fb25d pushed；rubric v3 冻结版 = r249f，R5 门禁 4/6 PASS（AC4 移出验收后实际阻塞项仅家族隔离）
- **T8 Part C 派发门禁条件仍满足**（AC1≥0.85 + AC3 双侧达标），纯等通道：arena binding 需 UI 重绑 + ninfer :8000/:8099 人工查（r255 复查 :8000 仍 down，:8787 proxy 可用）
- BRIDGE-REPORT.md 无新报告；arena 侧无可对账产出
- decomp 侧联动（r256, d1edf93）：T21 收口完成——flagship-eval S3 按 T21-RR 实测锚定重算 + 主报告并入，GPU 选型主线 T19→T20→T21 闭环，decomp 本地可执行项清零

## 下一步
1. **T8 Part C 派发**（P1，纯等通道）：ninfer 恢复或 arena UI 重绑后，按 TASK-pilot-run.md 派发 9 run（复用 01a195cb 会话先例）。r258 复查：:8000/:8099 仍 down，:8787 up（retest-32k 实调验证可用）。pilot-matrix 的 run 脚本 max_tokens 建议提到 32000（retest-32k 教训）。
2. **第三 seed 功效提升 run**（P1，卡预算审批 APPROVALS；AC4 收口后不再是前置条件）。
3. G1b family_check 模型身份披露（blocked-on-human：非 Qwen API key / arena 人工过 Cloudflare / 平台披露三选一）。
4. ACTIVE-candidates #4 ORF arXiv 手动上传 / #3 健康 strand 镜像源（需人工）。
5. ~~M8-cover 口径对齐~~ **已完成 (r254c)**。