import sys

import pickle

#flask based modules
from flask import Flask, request, jsonify, make_response, send_file, Response
from flask_cors import CORS, cross_origin
app = Flask('app')

#libraries for generic use
import numpy as np
import test
from PIL import Image


@app.route('/get_output', methods=['POST'])
def get_output():
    print(" -- in get_output --")
    
    try:
        num_imgs=0
        num_imgs=int(request.form['num_imgs'])
    except:
        pass
    names=[]
    for i in range(num_imgs):
        try:
            name='image'+str(i)
            img = Image.open(request.files[name])   # get image
            img = img.convert('RGB')
            img = np.array(img)
            im = Image.fromarray(img)   # saving
            im.save("input/face/"+str(i)+".png")
            names.append(str(i)+".png")
        except:
            pass
    
    try:
        fs=10
        fs=int(request.form['fs'])
    except:
        pass
    
    try:
        w_steps=10
        w_steps=int(request.form['w_steps'])
    except:
        pass
    
    try:
        align_steps1=10
        align_steps1=int(request.form['align_steps1'])
    except:
        pass
    
    try:
        align_steps2=10
        align_steps2=int(request.form['align_steps2'])
    except:
        pass
    
    try:
        blend_steps=10
        blend_steps=int(request.form['blend_steps'])
    except:
        pass
    
    resp=test.blend_imgs(names,fs,w_steps,align_steps1,align_steps2,blend_steps)
    resp=jsonify(resp)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3000)