import numpy as np
import bpy
from os import listdir

scene = bpy.context.scene

PATH = bpy.path.abspath("//../../output/RocketQuat/SC_tracking")
path = PATH + "/" + sorted(listdir(PATH))[-1]
path += "/" + sorted(listdir(path))[-1]
print(path)

FPS = scene.render.fps
scene.frame_current = 0

try:
    X = np.genfromtxt(path+"/X.txt", delimiter=',')
    U = np.genfromtxt(path+"/U.txt", delimiter=',')
    t = np.genfromtxt(path+"/t.txt", delimiter=',')
except OSError:
    print("Data not found.")
    #continue

K = X.shape[0] # number of states
scene.frame_end = int(t[-1] * FPS) #we will have time * fps frames

body_ob = bpy.data.objects.get("rck")
eng_ob = bpy.data.objects.get("eng")
fir_ob = bpy.data.objects.get("fir")
leg1_ob = bpy.data.objects["leg_mesh"]
leg2_ob = bpy.data.objects["leg_mesh.001"]
leg3_ob = bpy.data.objects["leg_mesh.002"]
leg4_ob = bpy.data.objects["leg_mesh.003"]

body_ob.animation_data_clear()
eng_ob.animation_data_clear()
fir_ob.animation_data_clear()
leg1_ob.animation_data_clear()
leg1_ob.animation_data_clear()
leg3_ob.animation_data_clear()
leg4_ob.animation_data_clear()

T_max = np.max(np.linalg.norm(U[:, :3], axis=1))

for k in range(K):
    scene.frame_current = int(t[k] * FPS)
    x = X[k]
    u = U[k, :3] #exclude roll torque

    body_ob.location = x[1:4] / 100
    body_ob.rotation_quaternion = x[7:11]
    body_ob.keyframe_insert(data_path='location')
    body_ob.keyframe_insert(data_path='rotation_quaternion')

    rx = np.arctan(-u[1] / u[2])
    ry = np.arctan(u[0] / u[2])
    min_l = 1
    l = min_l + 6 * (np.linalg.norm(u) / T_max) #7 should be max, 1 min
    eng_ob.rotation_euler = (rx, ry, 0)
    eng_ob.keyframe_insert(data_path='rotation_euler')
    fir_ob.scale[2] = l 
    fir_ob.keyframe_insert(data_path='scale')
    
    if k == int(K * 0.8):
        for leg in [leg1_ob, leg2_ob, leg3_ob, leg4_ob]:
            leg.rotation_euler[0] = 90.4 / 180 * np.pi
            leg.keyframe_insert(data_path='rotation_euler')

    if k == min(int(K * 0.95), K - 1):
        for leg in [leg1_ob, leg2_ob, leg3_ob, leg4_ob]:
            leg.rotation_euler[0] = -25 / 180 * np.pi
            leg.keyframe_insert(data_path='rotation_euler')
        
scene.frame_current += 5

fir_ob.scale[2] = 0
fir_ob.keyframe_insert(data_path='scale')

scene.frame_current = 0