# origin: ai — Goal 队列（ralph loop 消费）

> 格式：`- [ ] <goal 短名> | <一句话目标> | <产投比依据>`。完成改 `[x]` + 日期。新导出的候选追加到底部。

## 待办

- [ ] RUBRIC-V3-FULL-AUDIT | rubric-v3 完整消融推进+矛盾/漏洞/优化审计（G1-G6 六子goal，研究级长任务）| 任务书 tasks/RUBRIC-V3-FULL-AUDIT-task-brief.md；队首优先——决定 rubric-v3 能否定稿，含真正的方法论判断（构念效度根因），非 trivial 修补。runner 按 G1→G6 顺序拆子 goal 逐个走 1-loop，每个子 goal 独立收口 merge main 后取下一个
- [ ] R5.2-third-scorer | 第三打分器（不同模型家族）用 packet v2 盲打 r4 三 run，κ 从 2-rater 升到 Fleiss'κ | R5.2 已交付 packet v2（输入对称断言通过），本 goal 直接消费；需 arena 通道或第三个本地模型，产投比中但依赖外部
- [x] T8-matrix-run-r1 (2026-10-30, r101: M8=1.00 团队文件协作/网盘选型域) | 按 tasks/T8-matrix-run-r1.md 任务书执行矩阵 run | 任务书已 push，产投比中

## 已完成

- [x] R5.2-evidence-packet (2026-10-30, r102: baff4b3) — 模板 v2 + packet v2（run1 M2=24/run2 M2=25/run3 null~45；M5 轮数 1/1/2 全带 basis）+ 对称性断言 67/0 exit 0；X2 错配登记（原 packet "run3 任务书25行"张冠李戴）
- [x] R5.2-packet-audit (2026-10-30, r103) — 原 v1 packet 单行摘要 12+1 原子断言全字段审计：8 confirmed / 3 mismatch / 1 unverified；新登记 X4(run1"无降级"vs degraded[3])/X5(14m27s unverified)/X6(step2"49/25/25"双错配，分值结论不变仅理由文本错→APPROVALS 条目 3)/X7("M1-M6定义+"空承诺)；机判脚本 assert-packet-audit.py 16/0/2 exit 0；未改任何冻结分
- [x] R5.2-sourcepath-hardening (2026-10-30, r104) — W1 收口：assert-packet-symmetry.py 删 basename glob 兜底（严格模式：全部 token base join 命中才 PASS + EXEMPT 显式豁免预留）；packet v2 十条 source_path 规范化为完整相对路径（字段值零改动）；重跑 67/0 exit 0 基线维持；模板 v2 补填写规则
- [x] R5.2audit-C12-mechanize (2026-10-30, r105) — C12 "M1-M6 定义+" 形式性检查由 SKIP(manual) 改机判信号输出（声称子串 + 正文正则，只扫 evidence_packet 字段；signal-only、verdict 归类留人工）；重跑 16 PASS / 0 FAIL / 1 SKIP + 1 SIGNAL exit 0；审计表 C12 行补机判引用；未改任何 verdict 与冻结分

## 新导出候选

- [x] R5.2hard-EXEMPT-sentinel (2026-10-30, r106: 6fbd47b) — EXEMPT 非空哨兵警告落地, SELF-TEST 假豁免验证触发, 67/0 exit 0 基线维持
- [ ] R5.2audit-C4-timing-reconstruct | C4 "14m27s" 数值化机判：解析 $WS/run2/loop-state.json channel 时间戳做差值重建耗时区间，与 14m27s 比对输出 SIGNAL（若转录件无逐事件时间戳则降级为"不可重建"信号并登记 X5 状态更新） | R5.2-audit 02.5 A4 导出：C4 属数值计算而非字符串比对，超出 C12 goal 边界；工作量小
- [ ] R5.2audit-signal-counter | assert-packet-audit.py 汇总行 "+ 1 SIGNAL(C12)" 硬编码改为 signal 计数变量（防未来加第二个 signal 时汇总行撒谎） | R5.2c12 04.5 R6/W1 登记，工作量极小
