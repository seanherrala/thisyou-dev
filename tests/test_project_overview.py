from thisyou.project_overview import create_project_overview


def test_create_project_overview_has_three_signals():
    signals = create_project_overview()

    assert len(signals) == 3
    assert signals[0].name == "Identity"
    assert signals[-1].name == "Analysis"
    assert any("orbit" in signal.description.lower() for signal in signals)
