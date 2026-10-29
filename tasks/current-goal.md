# Goal: R5.2audit-C12-mechanize — C12 形式性检查纳入机判

> 创建：2026-10-30 · ralph loop runner（goal-queue 新导出候选，R5.2-audit 04.5 W1）
> 依据：`loop-artifacts/stages/04.5/R5.2audit-review.md` W1 + `tasks/goal-queue.md` 候选行

## 【目标】
`r5/assert-packet-audit.py` 当前把 C12（v1 packet "M1-M6 定义 +" 声称 vs 正文缺失）标为 SKIP(manual)。其数据提取部分实为字符串检查，可机判化：
1. **脚本加 C12 机判项**：(a) 声称检测 = packet 含 "M1-M6 定义"；(b) 正文检测 = packet 中是否存在指标名+解释模式（`M[1-6]\s*[:：=（(]`）或定义性词汇；两者组合 → 输出机判信号（claimed & no body = mismatch 信号）。
2. **verdict 归类仍留人工**：脚本只打印机判信号（如 `SIGNAL C12: claimed=yes body=no → 建议 verdict=mismatch(形式性)`），不自动写 verdict——与 04.5 R6 裁决一致（数据提取机判、归类人判）。
3. 审计表 C12 行的证据定位补上该命令输出引用。
4. 重跑 exit 0 且原 16 PASS / 0 FAIL 不变（C12 从 SKIP 变为 SIGNAL 报告项，不影响 exit code 语义）。

## 【阶段】
bench 度量基础设施微加固（R5.2-audit 的 W1 收口）。前置事实已定：r103 审计结论 8 confirmed / 3 mismatch / 1 unverified 冻结；本 goal 只增强机判覆盖，不改任何 verdict 结论与分数。

## 【SOP 索引】
- `sop/arena-loop-pipeline.md`（唯一 SOP 入口）
- `loop/prompt-first/00-common-review.md` + `01..04.5`（阶段定义）
- `bench/self-opt-tester/r5/assert-packet-audit.py`（**改造对象**，SKIP 段 L~110）
- `bench/self-opt-tester/r5/packet-audit-r4-v1.md`（C12 行更新）
- `bench/self-opt-tester/bench.md`（R5.2-audit 节微调一句）

## 【验收标准】
1. 六阶段工件齐全于 `loop-artifacts/stages/<N>/`，文件名带前缀 `R5.2c12-*`
2. 01：C12 机判逻辑设计（声称检测 + 正文检测的正则/关键词方案 + 假阳性边界分析）
3. 02：web-llm 强制步骤执行并留回执（预期三 provider 仍 error → 记录失败继续）
4. 02.5：风险登记（如正文检测正则对合法定义形式的漏报面）+ 对抗核验停止理由
5. 03：每步标 owner=user/agent
6. 04：脚本改造落盘 + 审计表 C12 行更新 + 重跑 exit 0 且 16 PASS / 0 FAIL 维持 + C12 由 SKIP 变 SIGNAL 输出
7. 04.5：反方复核 verdict + repair_stage
8. bench.md R5.2-audit 节补一句（C12 已机判化）
9. commit + push 分支 `ralph/r5.2audit-c12-mechanize` + ls-remote 验证

## 【失败降级】
- web-llm 三 provider 均不可用 → 记录失败回执后继续，不阻塞
- 正文检测正则出现假阳性/假阴性争议 → 机判信号措辞降为"线索"（stdout 明示 signal-only），verdict 仍完全留人工；不得因正则不完美而跳过机判化