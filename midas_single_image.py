import sys
import os
import cv2
import path_finding as pf

sys.path.append(os.path.join(os.getcwd(), 'Midas'))
import Midas.run as Mid

model_name = 'dpt_swin2_tiny_256'
model_path = f'./Midas/weights/{model_name}.pt'

def init():
    model, transform, net_w, net_h, device = Mid.init_midas(model_path=model_path, model_type=model_name)
    return model, transform, net_w, net_h, device

def run_midas(input, model, transform, net_w, net_h, device):   
    Mid.run(input, './Midas/outputs/forGUI', model, transform, net_w, net_h, device, model_type=model_name, grayscale=True)

def _open_map():
    # open the map
    map = cv2.imread('./Midas/outputs/forGUI/frame.png', cv2.IMREAD_GRAYSCALE)
    return map 

def path(point):
    map = _open_map()
    pf.main(map)

if __name__ == '__main__':
    # Initialize model and other parameters
    model, transform, net_w, net_h, device = init()
    
    # Run MiDaS on the input images
    run_midas('./Midas/inputs/rgb/', model, transform, net_w, net_h, device)
    
    # Open and display the generated map
    map = _open_map()
    cv2.imshow('map', map)
    cv2.waitKey(0)

