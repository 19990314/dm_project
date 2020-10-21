from imageai import Detection

modelpath = "mycomputer/myfolder/yolo.h5"

yolo = Detection.ObjectDetection()
yolo.setModelTypeAsYOLOv3()
yolo.setModelPath(modelpath)
yolo.loadModel()


