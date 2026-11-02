# CONTINUE_MSG — 2026-11-03 r260

## 本轮完成 (r260)
**T8-C3-v3-seedc-powerup（第三 seed 功效提升 run · CONTINUE_MSG 上轮下一步 #2）— 降级通道实跑收口，待 commit**：
- 动机：R6 主分析 n=4/cell 功效不足（所有 Δ 只报方向），加 seedc 把 D1/D2 每 cell 提到 n=3 seeds，看 F1（freeze 主效应三域一致为负）能否过「三 seed 同向」检查升级声明
- 通道：arena :8000/:8099 down → 按 runner 外包规则降级本地 ninfer :8787 qwen3.8-27b（conf−0.2 标注），全程零人工介入
- 冻结面（开跑前落盘并验证）：design/r6-seedc-powerup-design.json（seedc brief 文本 + 18 prompt sha256_16）；prompt builder 对 R4 全部 32 份 stored prompt 逐字节复刻验证通过后才使用；opportunity-sets-v1.json 扩展 brief_c 机会集（D1 9 项 / D2 10 项，_meta.r260_extension 登记）
- 执行：18/18 run 落盘 runs-seedc/runs/<config>/<domain>/seedc-r1.json（output_chars 4174-9242，零 HTTP 失败，gen max_tokens=32000 temp=0.7）+ J1v11/J2v11 双判 36/36 成功 + cover brief_c 判读 18/18
- **G3 = SIGNAL（重要发现，比预期更有价值）**：
  - F1 三 seed 同向性检查 FAIL：freeze 主效应 A-full−B-nofreeze，seedc D1 = 0.0（vs R4 +0.391 反向）、D2 = +0.75（同向）。F1 维持「只报方向」不升级
  - 根因不在工件在测量系统：J1v11 条目抽取跨 run 漂移——同一 A-full/D1 cell，R4 两 run 抽 7/10 条 numeric id 得 0.857/1.0，seedc 抽 3 条 X-prefix 得 0.0。per-config 分数方差里相当部分是「judge 抽了哪些条目」的方差 → **R4/R5/R6 所有 per-config Δ 的功效被系统性高估**
  - 推论：对抗核验 FAIL 1（M8-fixed 独立标注员预建冻结机会表 + 逐机会判定）从「seedc 前置条件」升级为**一切后续消融分析的前置条件**；在此之前新 run 分数只能作单 run 快照
  - 副产物复现：cover「高 cover ≠ 真核验」警示再次命中（B-none cover 1.0/1.0 而 J1 truth 0.0/0.0）；J2v11 15/18 run 恒 1.0（R4 同样），宽松版无区分力再确认；J1/J2 item-level 分歧 28/107=0.262 < 0.30 stop_rule 未触发
- 回执：receipt-r8-seedc.json（run/judge 全指纹）；queue 已划掉 seedc 项并登记结果
- wx-push 首次失败（retry-without-token invalid request），留痕继续干活（协议内不重试）

## 上轮完成 (r259)
**keepalive 状态核实（零 LLM 调用，纯核查）**：research-prompt retest-32k 定案收口（R0.3 定版七版消融完结）；pfb @ ae0a96f 与 origin/main 零 diff；pilot-matrix κ 回执已在 main（overall κ=0.857 过门禁）；BRIDGE-REPORT 无新报告；通道 :8000/:8099 down / :8787 up。

## 当前状态
- pfb @ main e92a0e4 pushed（origin/main 同步）；**r260 产出待 commit**（runs-seedc/ 全套 + design + opportunity-sets 扩展 + receipt-r8 + queue + 本文件）
- T8 Part C exploratory 已收口（r245s, T8-partC-exploratory.md exploratory-closed）；其 confirmatory 四条解锁条件中第 1 条（异源判官）仍 blocked-on-human，第 2 条（M8-fixed 逐机会标注）现在被 r260 证据升级为最高优先
- decomp 侧可执行项清零（r259 确认）；research-prompt 七版消融完结
- 卡人项不变：G1b family_check（非 Qwen key）/ B2 协议重设计候裁 / ORF arXiv 手动上传 / web-llm 三 provider 登录

## 下一步
1. **commit + push r260 产出**（P0，下轮第一件事或本轮收尾做）：`git add experiments/T8-matrix/runs/c3-v3/{runs-seedc,design/r6-seedc-powerup-design.json,design/opportunity-sets/opportunity-sets-v1.json,receipt-r8-seedc.json} tasks/goal-queue.md CONTINUE_MSG.md` → commit "r260: seedc powerup run 收口 — F1 未复现于 D1, 根因定位 J1v11 条目抽取漂移, M8-fixed 升级为前置条件" → push origin main
2. **T8-C3-v3-m8fixed-opportunity-table**（P1，新导出）：独立标注员（lead/成璐）预建 D1/D2/D3 × brief_a/b/c 冻结机会表 + 等价 pattern 机判 assert + 盲双判复核模板——这是 FAIL 1 修复，做完之前不再开任何新消融 run（避免再攒不可比数据）
3. G1b family_check 模型身份披露（blocked-on-human：非 Qwen API key / arena 人工过 Cloudflare / 平台披露三选一）
4. ACTIVE-candidates #4 ORF arXiv 手动上传 / #3 健康 strand 镜像源（需人工）
5. ~~T8 Part C 派发~~ **已完成 (r245s exploratory-closed)**；~~第三 seed 功效提升 run~~ **已完成 (r260)**