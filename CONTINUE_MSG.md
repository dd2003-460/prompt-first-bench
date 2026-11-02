# CONTINUE_MSG — 2026-11-02 r247

## 本轮完成
**Rubric v3 六轮迭代 + 全量重放（pfb @ main cc83cd4）**：按 r246 对账的两个根因修 rubric——J1 来源判据三级化（缺失=fail / 声明未实抓=降档 / 实抓=pass）+ 双判官统一 id 锚定（canonical 条目清单注入 prompt，禁自造 id）。J2 保留 v2 原文未动。

经 v3→v3.1f 六次修订冻结（每版都先单点验证再全量），终版 r5 结果：
- **AC1 一致率 0.960 (749/780) ≥0.85 PASS**（v2 是 0.661；越界幻觉 id 从 35.2% 清零）
- **AC2 阳性对照双 fail PASS**
- AC3 B-none 地板 <0.3：J1=0.083 ✓ / J2=0.5 ✗ FAIL
- AC4 A−2del-eo 差 ≥0.3：−0.055/−0.040 FAIL

**关键诊断（不是 judge 还能调的问题）**：
1. AC3 的 J2 侧失败是设计使然——J2 的定位就是宽容对照组，「有具体数字但无 URL」它按设计放过。阈值 <0.3 对 J2 天然不成立，应只对 J1 生效（或 J2 单独设阈值）。
2. AC4 是评分粒度问题——B-2del-eo 删的 evidence/owner 字段在「逐条目过三测」粒度下不在判定关键路径上，它拿满分甚至反超 A-full（分母效应：64 条 vs 26 条）。需要换负例配置（B-2del-fe 分数确实更低）或条目加权，不是拧 prompt 能解决的。
3. 实证教训：r4 一放松 J1 的 ②③ 判据，AC1 立刻从 0.96 掉到 0.772——**一致性达标后不能再动 J1**，否则破坏 AC1。

产出：`calibration/RUBRIC-V3-ITERATION.md`（完整迭代表+诊断）、`judge-prompts-rubric-v3.json` @v3.1f、`replay-rubric-v3.py`、`receipt-r8-rubric-v3-replay.json`。

## 当前状态
- pfb @ main cc83cd4（r247 两个 commit）；本地未 push
- localhost:8787 proxy 可用（qwen3.8-27b）；ninfer :8000/:8099 仍 down
- rubric 修复（原 P1 硬前置）：**一致性部分已完成**，验收口径变更待成璐拍板
- G1b family_check / T8 Part C / seedc 功效 run 卡点不变（见下）

## 下一步
1. **【需成璐拍板】AC3/AC4 验收口径**（r247 新导出，阻塞 seedc 双判门禁的最终确认）：
   - AC3 改为「J1 均值 <0.3」（J2 豁免或单独阈值）？
   - AC4 换负例为 B-2del-fe，或引入条目加权？
   - 或者接受现状：v3 定位为「一致性测量 rubric」，区分度场景另配。
   拍板后更新 receipt 口径复算一次即可收口（零模型调用成本）。
2. **T8 Part C 派发（P1，纯等通道）**：arena binding 需 UI 重绑 + ninfer 人工查（连续第 6 轮 down）。任务书可补一条「开跑前须过 R5 门禁：rubric v3 AC1=0.96 已达标」。
3. **第三 seed 功效提升 run（P1，卡预算审批 + 上面口径拍板）**：APPROVALS #2 待批。
4. M8-cover 口径对齐（P2）；G1b family_check 模型身份披露（需人工）；ACTIVE-candidates #4 ORF arXiv 手动上传 / #3 健康 strand 镜像源（需人工）。