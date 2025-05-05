INSTALL_CONTENT = """
# Transformers installation
! pip install transformers datasets evaluate accelerate
# To install from source instead of the last release, comment the command above and uncomment the following one.
# ! git clone https://github.com/huggingface/transformers.git && cd transformers && pip install .
"""

notebook_first_cells = [{"type": "code", "content": INSTALL_CONTENT}]
black_avoid_patterns = {
    "{processor_class}": "FakeProcessorClass",
    "{model_class}": "FakeModelClass",
    "{object_class}": "FakeObjectClass",
}