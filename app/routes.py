from flask import Flask, render_template, request, redirect, url_for
import os
from app.vhdl_structures import vhdlBlock
from app.simulations import simulate_hdl
from app import app

app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = {'vhdl', 'vhd'}

ports = []
filepath = None

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
  global ports, filepath
  simulation_result = None

  if request.method == 'POST':
    if 'hdl_file' in request.files:
      file = request.files['hdl_file']
      if file and allowed_file(file.filename):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        with open(filepath, 'r') as f:
          code = f.read()
          top_block = vhdlBlock(code)

    elif 'simulate' in request.form:
      if filepath:
        inputs = {p['name']: request.form.get(p['name']) for p in ports if p['dir'] == 'in'}
        simulation_result = simulate_hdl(filepath, inputs)

  return render_template('upload.html', ports=ports, simulation_result=simulation_result)