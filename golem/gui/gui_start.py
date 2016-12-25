from golem.core import test_execution
from golem import gui

def run_gui(port_number):
    gui.root_path = test_execution.root_path
    gui.app.run(debug=True, host='0.0.0.0', port=port_number)