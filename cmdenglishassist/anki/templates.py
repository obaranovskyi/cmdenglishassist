BASE_TEMPLATE_STYLES = """
<style>
  .main-container {
    font-size: 24px; 
    font-family: sans-serif; 
    text-align: center; 
    padding: 20px;
  }
</style>
"""

def to_base_template(value):
    template = f'<div class="main-container">{value}</div>'
    return f'{BASE_TEMPLATE_STYLES}{template}'
