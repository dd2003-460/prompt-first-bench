# Lead TODO (ralph stop-hook 读这个文件; "- [ ]" = 未完成, "- [x]" = 完成)

## 已完成
- [x] drb-2 (pid 4633) 跑完 → 验树: id 62/62 唯一 (修复生效), 孤儿 18 (未修, 已报 CC L7), degraded 53/62 全通道型, fanout cap 未生效 (max=4, 已报 CC L7)

## 当前队列

- [x] **[P0 · 成璐直接指令] 读 `research/e-block-prior-pack.md` 然后重新校准 E 块** — 已读完并落盘校准结论 (见下方 e-block 校准节); P3 stop_std_max 已接进主循环并提交; P5 CDF 回标脚本待写 (等 gpu run 出树补 gain 样本)
- [x] gpu 题新题面重跑: 已启动 pid 11150 (proc_07adee4420ac), 无 resume 全新跑, log=drb-pilot/run-gpu-rerun-console.log, watch DONE/FATAL
- [ ] CC bus L6-L16 靶点提案收口 — CC 进程不在运行 (cc-to-lead.md 停在 04:05 C9); L16 已写明重启优先级 (L14 reverify 分型 + L15 闭环协议先读); 等 CC 回执后逐项验收
- [x] runs-s5-sm-gpu.json 废弃决策: 精确数据 12 dup ids (N19-N26 x5) 已报 CC L8, 文件整体废弃留作旧题面对照, D26 走文本匹配
- [x] gpu 新 run 题面确认: log 首行铁证用新题面("不设硬性延迟指标"); sm-gpu-r1/r2.json mtime=昨天21:56/22:08 是旧残留, pid 11150 还没写 ckpt(停在 r1 decompose); N1 claim 待 r1 ckpt 落盘后验
- [x] 修复后 hook 实证: 手动跑 N8 query "A.M. Best 保险前十" → 5 通道返回 5 源(含 ambest.com×2+sohu), 连通性本身没问题, all-5-failed 纯 regex 笔误
- [x] drb-2 51 节点自愈: reverify_drb2.py 全量后台跑 (pid 17041); smoke 1/3 healed(N8 verified), N9/N10 真缺数值源仍 degraded(非 bug); resume 确认救不回
- [x] drb-2 reverify 全量收口: healed 0/51 (smoke 的 N8 healed 是脚本口径误报); 三类分型定稿 = 无源 all-5-failed 35 (query 形态问题) + 有源无数值 16 (真数据缺口, 免费网页没有细粒度金融数据) + 代码 bug 已修非主因; 详见 lead-to-cc.md L14; D26 建议把 drb-2 标为"数据边界受限题"
- [x] gpu 新 run #2 (DONE ~15:40, 153/153 unique) → bench report §2 加 gpu 行 + §3 补 gpu 节（fe0a3016）；L21 已回 CC（L20 P0/P1 撤销）
- [x] P5 CDF 回标脚本：8 个有效 gain 样本（drb-1×3 + drb-2×2 + gpu×3，n_new=0 轮剔除）→ mean 0.896 / std_pop 0.056；stop_std_max 0.15→0.06（1x σ）已落 s5_state_machine.py 并提交；样本+经验 CDF 落盘 p5-cdf-backlabel.json。原 0.15 比实测波动宽 2.7x，等于永不 reset streak——修完这个 E4 判据才真正在回路里

## e-block 校准结论（2026-11-12，读 research/e-block-prior-pack.md 后）

**核心发现：gain_threshold=0.5 是死参数。** 全部现有 run 的 per-round gain（n=7：drb-1×3, drb-2×2, gpu×2）范围 [0.805, 1.0]，mean=0.900，没有一个 < 0.5。代码里 `cfg.gain_threshold` 只在 dataclass 定义处出现一次，主循环从未读取它——实际停止判据是 pass_rate<0.3 + low_gain_streak（line 897）。所以"为什么选 0.5"这个问题本身不成立：它没在回路里。

**先验包的 6 个坑对照现状**：
- P1-P2（retriever 修复）→ 已做（regex 笔误 + junk filter + Bing 标准化），但 L14 证明对硬数据题只解了通道、不解数据边界
- P3（stop_std_max 接主循环）→ **本轮已落地并提交**：近窗 5 轮 gain std > stop_std_max(0.15) 时 reset low_gain_streak，防止探索期被误判收敛
- P4（多采样 contrib_samples>1）→ E2 代码已在（classify_edge_var），默认 contrib_samples=1 退化为现状；启用需付 3x LLM 调用成本，等 gold 题集就绪再开
- P5（CDF 回标 threshold）→ 样本不够（n=7 且全来自 3 条题），等 gpu 新 run 出树补 r3+ 样本后再写回标脚本
- P6（gold 题校验）→ 未开始，依赖 D26 验收口径定稿

**下一步排序**：gpu run 出树 → 验树 + 补 gain/pass_rate 样本 → 写 P5 CDF 回标脚本 → 用回标值替换拍脑袋阈值。
