# CONTINUE_MSG — 2026-11-03 r250b/r250c

## 本轮完成
**B-4 结构完整性底线尝试 + 回滚（pfb @ main 10071cd）**：
- r250：按 AC4 结构性诊断给 J2 加 B-4（支撑字段整体缺失→fail），全量重放 receipt-r10：AC1 0.978 PASS / AC2 PASS / AC3 双 PASS / **AC4 FAIL（−0.073/−0.063，比 r249f 更差）**
- 根因定位（实证）：B-2del-eo 删的 evidence/owner 挂在「待研究问题/推导条件」类条目上，J2 的宽容原则 + B-2a 不触发条款把这类条目整体豁免——judge 行为自洽（这些条目本就不需要实抓来源）。prompt 层面无法在不伤 AC1 的前提下解决。
- r250b：B-4 回滚；r250c：修复回滚时误删空行导致的 sha 漂移，J2 text 逐字节恢复 r249f（sha=0b8e837239da3fd5，已验证 MATCH）
- RUBRIC-V3-ITERATION.md 补 r250/r250b 追记，三次实证收敛结论固化

**关键结论：AC4 是评分维度问题，不是 prompt 问题**。r4（放松 J1→AC1 崩）/ r249e（收紧 J2→过度约束）/ r250（加 B-4→judge 自洽豁免）三轮收敛同一答案。

## 当前状态
- pfb @ main 10071cd pushed；rubric v3 冻结版 = r249f（J1 a4eb67e35fa066d5 + J2 0b8e837239da3fd5），AC1/AC2/AC3 达标、AC4 结构性 FAIL
- localhost:8787 proxy 可用；ninfer :8000/:8099 仍 down
- 微信推送 token 失效（invalid request，连续两轮），播报随 cron 回复送达

## 下一步
1. **【需成璐拍板 · 唯一阻塞项】AC4 口径三选一**（拍板后零模型调用复算收口）：
   - (a) 换负例配置：用 B-2del-fe（均值 0.722 vs A-full 0.923，diff≈0.20）或 B-2del-fo（0.111，diff≈0.81）做区分度判据——数据已在 receipt-r9/r10 里，纯复算
   - (b) 条目加权：evidence 缺失条目降权计分——需改 replay 脚本计分逻辑
   - (c) 接受现状：v3 定位为「一致性+地板测量 rubric」（AC1/AC2/AC3 全过即冻结），区分度场景另配评分维度
2. T8 Part C 派发（P1，纯等通道）：arena binding 需 UI 重绑 + ninfer 人工查。R5 门禁（rubric v3 AC1≥0.85 + AC3 双侧达标）r249f 已满足。
3. 第三 seed 功效提升 run（P1，卡预算审批 APPROVALS #2 + AC4 拍板）。
4. M8-cover 口径对齐（P2）；G1b family_check 模型身份披露（需人工）；ACTIVE-candidates #4 ORF arXiv 手动上传 / #3 健康 strand 镜像源（需人工）。