import pytest
from dash.testing.application_runners import import_app

@pytest.fixture
def dash_app():
    app = import_app('app')  
    return app

def test_header_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    header = dash_duo.find_element('h1')
    assert header.text == 'Pink Morsel Sales Visualizer'
    print("✅ Header check passed")

def test_visualisation_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    graph = dash_duo.find_element('.dash-graph')
    assert graph is not None
    print("✅ Visualization check passed")

def test_region_picker_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    region_filter = dash_duo.find_element('#region-filter')
    assert region_filter is not None
    print("✅ Region picker check passed")
