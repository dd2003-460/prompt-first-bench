from ralph_runtime.nodes import DEFAULT_GRAPH


def test_default_graph_has_ordered_nodes_and_exploration():
    assert DEFAULT_GRAPH.ids() == ("01", "02", "02.5", "03", "04", "04.5", "05", "06", "exploration", "completed")
    assert DEFAULT_GRAPH.get("02").on_success == "02.5"
    assert DEFAULT_GRAPH.get("02.5").on_success == "03"
    assert DEFAULT_GRAPH.get("03").on_success == "04"
    assert DEFAULT_GRAPH.get("04").on_success == "04.5"
    assert DEFAULT_GRAPH.get("04.5").on_success == "exploration"
    assert DEFAULT_GRAPH.get("06").on_success == "exploration"
    assert DEFAULT_GRAPH.get("exploration").on_success == "01"
