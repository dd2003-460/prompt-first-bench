# CONTINUE_MSG — 2026-11-03 r278b KB.1 第7篇收口轮

## 本轮完成（r278b）
- **KB.1 第7篇教材 note 收口**：notes/retrieval-vs-long-context.md（检索 vs 长上下文，RAG 存废问题）落盘。A 段 10 概念块各含 是什么/为什么/边界+conf；B 段判断+自我质询+动机+可证伪 idea（LoCoMo 全文塞入对照组，判死条件 <5pp/>20pp）。素材锚定 decomp T17 gold tree + LoCoMo full01 在途实验 + 前 6 篇留的口子
- **drift-check 100/100**：145 句/均句 42.6（无 >55），第一人称率 0.207≥0.2，空话 0。三项硬门槛全过
- **INDEX.md 加行 + loop-state.json current_task 更新**（iteration 7, stage→next/C区剩余方向或LoCoMo对照组）
- **commit d401aec9 pushed origin/main**（workspace 仓）
- **goal kb-note-7-retrieval-vs-longctx-r278 五阶段全过 complete**
- T17-full 顺手核验：conv3 已到 98/199（上轮 94），runner 62585 健康，累计 ~483 题已判

## 当前状态
- workspace main @ d401aec9 pushed；pfb @ c01c6d5 pushed；decomp clean；tools/memory-benchmarks 本地 5 commits 未推（403 已知阻塞）
- goal kb-note-7-retrieval-vs-longctx-r278 completed (5/5)
- C 区 #10 agent 记忆基础设施三线闭合（外壳/内脏/存废）

## 下一步（最高产投比）
1. **T17-full 跑完后的事**：conv3 剩 ~100 题 ≈1.5h，conv4-7 ≈18h。跑完后重算 top_10 overall（base 483+）vs smoke01 baseline，噪声 ±1.5pp 判定；然后按 note B 段 idea 决定要不要开"全文塞入对照组"（成本 ~20h）
2. find-goal SOP 下一候选：C 区剩余兴趣方向（见 projects/知识/D1-knowledge-base/memory/interest-directions.md）——目前只剩这一条纯本地线，外部候选全 blocked（:8787 gateway 评估等成璐拍板 / survey backfill 需 arena 01a18567 / judge 三方选择待 T8 closeout）
3. WORK_QUEUE 队首不变：C3 v3 ninfer HTTP :8000 直跑 paired runs（前置 G1-G5 门禁，卡 T8）

## T17-full 进度（runner 62585 健康）
conv0 152✅ · conv1 81✅ · conv2 152✅ · conv3 98/199 · 累计 ~483 题已判
基线口径：top_10 438 题 overall 0.395 (sh .400/temp .390/mh .411/od .320)——下轮重算时纳入新增 conv3 题
按当前速度 conv3 剩 ~100 题 ≈ 1.5h；conv4-7 约 1400 题 ≈ 18h。checkpoint 可续传，不动它

## 其他卡人项不变
erratum-27 / G1b family_check / R121 / ORF arXiv 上传 / Arena 沙箱恢复探测（ls-remote 4 分支 HEAD 是否变化）
