import cv2
import cv2.cv as cv
import time

# Devices.
CV_CAP_OPENNI = 900 # OpenNI (for Microsoft Kinect)
# Channels of an OpenNI-compatible depth generator.
CV_CAP_OPENNI_DEPTH_MAP = 0 # Depth values in mm (CV_16UC1)
CV_CAP_OPENNI_POINT_CLOUD_MAP = 1 # XYZ in meters (CV_32FC3)
CV_CAP_OPENNI_DISPARITY_MAP = 2 # Disparity in pixels (CV_8UC1)
CV_CAP_OPENNI_DISPARITY_MAP_32F = 3 # Disparity in pixels (CV_32FC1)
CV_CAP_OPENNI_VALID_DEPTH_MASK = 4 # CV_8UC1
# Channels of an OpenNI-compatible RGB image generator.
CV_CAP_OPENNI_BGR_IMAGE = 5
CV_CAP_OPENNI_GRAY_IMAGE = 6



cap=cv2.VideoCapture(CV_CAP_OPENNI)
width=int(cv.CV_CAP_PROP_FRAME_WIDTH)
height=int(cv.CV_CAP_PROP_FRAME_HEIGHT)



channels = {
            'depth_map':    {'value':0},
            'point_cloud':  {'value':1},
            'disparity':    {'value':2},
            'disparity_32f':{'value':3},
            'valid_depth':  {'value':4},
            'bgr':          {'value':5},
            'gray':         {'value':6}}

for channel,params in channels.iteritems():
    print 'creating writer for {}'.format(channel)

    #create video writers
    params['writer']=cv2.VideoWriter(   filename='output{}.avi'.format(channel),
                                        fourcc=cv.CV_FOURCC('M','J','P','G'),
                                        fps=30,
                                        frameSize=(width,height))

    #create windows
    cv2.namedWindow('{}'.format(channel))



while True:
    cap.grab()
    start=time.time()

    for channel,params in channels.iteritems():
        # print 'getting frame from {}'.format(channel)


        ret,img=cap.retrieve(channel=params['value'])
        if ret:
            pass
            # params['writer'].write(img)
            cv2.imshow('{}'.format(channel),img)
        else:
            print "Unable to retrieve frame from channel: {}".format(channel)
    print time.time()-start



    if cv.WaitKey(10) == 27:
        break
