# CONTINUE_MSG — 2026-11-03 r251

## 本轮完成
**B-4 v2 设计 + 回滚，AC4 prompt 路线彻底关闭（pfb @ main 5f91d49）**：
- r251：按 r250 失败模式重设计 B-4（显式限定「断言了具体结论/事实/数字但无支撑」+ 明文豁免研究计划类条目），未跑全量即定位到更深根因并回滚
- **结构性根因**：B-2del-eo 删的 evidence/owner 是 prompt 侧组件（阶段指令段，见 prompts/MANIFEST.json ops），不是工件条目内字段。judge 只审计模型产出的工件正文，看不到 prompt 里被删了什么 → 任何「缺支撑→fail」判据都检测不到这个消融。AC4 在条目级 judge 粒度下结构性不可测
- J2 text 精确恢复 r249f（sha=0b8e837239da3fd5 验证 MATCH）；RUBRIC-V3-ITERATION.md 补三次 prompt 尝试关闭记录

## 当前状态
- pfb @ main 5f91d49 pushed；rubric v3 冻结版 = r249f，AC1/AC2/AC3 达标、AC4 结构性 FAIL（prompt 路线已穷尽）
- localhost:8787 proxy 可用；ninfer :8000/:8099 仍 down
- 微信推送 token 失效（连续四轮 invalid request），播报随 cron 回复送达

## 下一步
1. **【需成璐拍板 · 唯一阻塞项】AC4 口径三选一**（零模型调用复算收口）：
   - (a) 换负例配置：B-2del-fe（diff≈0.20）或 B-2del-fo（diff≈0.81）做区分度判据——数据在 receipt-r9/r10 现成
   - (b) 条目加权：evidence 缺失条目降权计分——需改 replay 脚本计分逻辑
   - (c) 接受现状：v3 定位为「一致性+地板测量 rubric」（AC1/AC2/AC3 全过即冻结），区分度场景另配维度（如 run 层面 config 对比分析）
2. T8 Part C 派发（P1，纯等通道）：arena binding 需 UI 重绑 + ninfer 人工查。R5 门禁 r249f 已满足。
3. 第三 seed 功效提升 run（P1，卡预算审批 APPROVALS #2 + AC4 拍板）。
4. M8-cover 口径对齐（P2）；G1b family_check 模型身份披露（需人工）；ACTIVE-candidates #4 ORF arXiv 手动上传 / #3 健康 strand 镜像源（需人工）。