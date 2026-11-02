# CONTINUE_MSG — 2026-11-03 r252

## 本轮完成
**AC4 三选项零调用复算（pfb @ main 6dd3419）**：
- 用 receipt-r9 冻结版数据对三个 AC4 口径选项做纯复算，产出 receipt-r11-ac4-options-recompute.json
- **(a-eo) B-2del-eo**：diff −0.061/−0.033 FAIL。结构性不可测（prompt 组件消融，judge 不可见）——r251 已定位根因
- **(a-fe) B-2del-fe**：diff +0.201/+0.245 FAIL（差 0.05-0.09 到 0.3 阈值）。fe 删功能证据→条目锐减（13/6/0/12 vs A-full 26/38/33/32）但质量未崩，判官仍给 0.72
- **(a-fo) B-2del-fo**：diff +0.812/+0.967 PASS 但是假象——仅 1/4 run 有效，另外 3 个 run 产出只有 246-365 chars（模型 tool-call 截断崩溃），score=null 不参与均值。不是 rubric 区分度，是执行失败碰巧拉低均值
- **结论**：三选项均不能干净收口 AC4。维持推荐 (c) 接受现状：v3 = 一致性+地板测量 rubric（AC1 0.956 / AC2 PASS / AC3 双 PASS），区分度场景另配维度
- RUBRIC-V3-ITERATION.md 补 r252 追记表

## 当前状态
- pfb @ main 6dd3419 pushed；rubric v3 冻结版 = r249f（J1 a4eb67e35fa066d5 + J2 0b8e837239da3fd5），AC1/AC2/AC3 达标、AC4 三选项复算完毕
- localhost:8787 proxy 可用；ninfer :8000/:8099 仍 down
- 微信推送 token 失效（连续五轮 invalid request），播报随 cron 回复送达

## 下一步
1. **【需成璐拍板 · 唯一阻塞项】AC4 口径终裁**（零模型调用收口）：
   - 推荐 (c) 接受现状：v3 定位为「一致性+地板测量 rubric」，AC1/AC2/AC3 全过即冻结，区分度场景另配维度（run 层面 config 对比分析）
   - 若坚持要 AC4 数字上 PASS：(a-fe) 需阈值从 0.3 降到 0.2（diff +0.20/+0.25）或补跑 fo 的 3 个崩溃 run（~6 次模型调用）
   - 拍板后改 replay 脚本 AC4 段 + 重出 receipt 即可收口
2. T8 Part C 派发（P1，纯等通道）：arena binding 需 UI 重绑 + ninfer 人工查。R5 门禁 r249f 已满足。
3. 第三 seed 功效提升 run（P1，卡预算审批 APPROVALS #2 + AC4 拍板）。
4. M8-cover 口径对齐（P2）；G1b family_check 模型身份披露（需人工）；ACTIVE-candidates #4 ORF arXiv 手动上传 / #3 健康 strand 镜像源（需人工）。