BASE_TEMPLATE_STYLES = """
<style>
  .main-container {
    font-size: 30px; 
    font-family: sans-serif; 
    text-align: center; 
    padding: 45px;
  }
</style>
"""

def to_base_template(value):
    template = f'<div class="main-container">{value}</div>'
    return f'{BASE_TEMPLATE_STYLES}{template}'
