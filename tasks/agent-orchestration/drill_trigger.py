#!/usr/bin/env python3
# origin: ai — D3 触发演练: 矛盾夹具 → signal=矛盾; 无矛盾夹具 → signal=none
import json, os, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import trigger_detector as td

HERE = os.path.dirname(os.path.abspath(__file__))
RCPT = os.path.join(HERE, "receipts")


def run_case(receipt, plan, out_name, expect):
    with tempfile.TemporaryDirectory() as d:
        rp, pp = os.path.join(d, "r.json"), os.path.join(d, "p.md")
        with open(rp, "w", encoding="utf-8") as f:
            f.write(json.dumps(receipt, ensure_ascii=False))
        with open(pp, "w", encoding="utf-8") as f:
            f.write(plan)
        res = td.detect(rp, pp)
    with open(os.path.join(RCPT, out_name), "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
        f.write("\n")
    assert res["signal"] == expect, f"{out_name}: signal={res['signal']} expect {expect}"
    print(f"ok {out_name} signal={res['signal']} count={res['count']}")


def main():
    # 矛盾: 上拍回执 evidence 含"实验节点数 40" vs 本拍任务卡真值"实验节点数 37"
    run_case(
        {"task_id": "drill", "status": "done",
         "evidence": {"smoke": "实验节点数 40 全过"}},
        "# 真值\n- 实验节点数 37 (来源: wc -l)\n",
        "drill-D3-trigger.json", "矛盾",
    )
    # 无矛盾: plan 无数字、无 op 行
    run_case(
        {"task_id": "drill", "status": "done",
         "evidence": {"smoke": "实验节点数 40 全过"}},
        "# 执行\n- 按任务卡执行\n",
        "drill-D3-none.json", "none",
    )
    print("DRILL PASS")


if __name__ == "__main__":
    main()
