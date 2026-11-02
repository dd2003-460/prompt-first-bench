# CONTINUE_MSG — 2026-11-02 r249f/r249g

## 本轮完成
**rubric v3 B-2a 三轮迭代收口（pfb @ main 9db3295）**：
- r249（B-2a 条文进 J2，sha 未同步遗留 bug）→ receipt-r8 AC1 0.968 PASS / AC3 双 PASS（J2 B-none=0.0）/ AC4 FAIL
- r249e（3-step 强制流程版，sha 仍未同步）→ 无新全量回执；与 r249f 对比后判定「不可跳步」无额外收益且有过度约束风险
- **r249f（冻结版）：B-2a 降回普通底线**，J2 sha=0b8e837239da3fd5（已同步），replay --out 参数化 → receipt-r9：AC1 0.956 PASS / AC2 PASS / **AC3 首次双侧达标**（J1=0.083, J2=0.083）/ AC4 FAIL（diffs −0.061/−0.033）
- r249g：修正 RUBRIC-V3-ITERATION 追记里的错误记录 + 固化两条教训（判据改动先冒烟；改 text 必须同步 sha）

**关键结论**：AC3 不再需要口径变更——B-2a 条文本身就把 J2 的 B-none 地板压下来了（v3.1f 时代没有 B-2a 才放过）。宽容对照组设计意义保留（B-nofreeze J2=0.22 vs J1=0.72）。

## 当前状态
- pfb @ main 9db3295 pushed；prompt 文件 sha 全部 MATCH
- localhost:8787 proxy 可用（qwen3.8-27b）；ninfer :8000/:8099 仍 down
- rubric v3 冻结版 = J1 a4eb67e35fa066d5 + J2 0b8e837239da3fd5，三项验收达标、一项结构性 FAIL

## 下一步
1. **【需成璐拍板 · 仅剩 AC4 一项】区分度负例口径**（阻塞 seedc 双判门禁最终确认）：
   - 换负例配置为 B-2del-fe（删功能证据，分数确实更低）？
   - 或引入条目加权（evidence 缺失条目降权计分）？
   - 或接受现状：v3 定位为「一致性+地板测量 rubric」（AC1/AC2/AC3 全过），区分度场景另配。
   拍板后零模型调用复算 receipt 即可收口。
2. T8 Part C 派发（P1，纯等通道）：arena binding 需 UI 重绑 + ninfer 人工查（连续第 6 轮 down）。任务书补「开跑前须过 R5 门禁：rubric v3 AC1≥0.85 + AC3 双侧达标（r249f 已满足）」。
3. 第三 seed 功效提升 run（P1，卡预算审批 APPROVALS #2 + 上面 AC4 拍板）。
4. M8-cover 口径对齐（P2）；G1b family_check 模型身份披露（需人工）；ACTIVE-candidates #4 ORF arXiv 手动上传 / #3 健康 strand 镜像源（需人工）。