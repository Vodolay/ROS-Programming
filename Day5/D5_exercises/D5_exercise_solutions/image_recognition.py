#!/usr/bin/env python
import rospy
from sensor_msgs.msg import CompressedImage
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2
import numpy as np
import tensorflow as tf
import classifier


class RosTensorFlow():
    def __init__(self):
        classifier.maybe_download_and_extract()
        self._session = tf.Session()
        classifier.create_graph()
        self._cv_bridge = CvBridge()

        self._sub = rospy.Subscriber('image', CompressedImage, self.callback, queue_size=1)
        self._pub = rospy.Publisher('result', String, queue_size=1)
        self.score_threshold = rospy.get_param('~score_threshold', 0.1)
        self.use_top_k = rospy.get_param('~use_top_k', 5)

    def convert_ros_compressed_to_cv2(self, compressed_msg):
        np_arr = np.fromstring(compressed_msg.data, np.uint8)
        return cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    def callback(self, image_msg):
        cv_image = self.convert_ros_compressed_to_cv2(image_msg)
        # copy from
        # classify_image.py
        image_data = cv2.imencode('.jpg', cv_image)[1].tostring()
        # Creates graph from saved GraphDef.
        softmax_tensor = self._session.graph.get_tensor_by_name('softmax:0')
        predictions = self._session.run(
            softmax_tensor, {'DecodeJpeg/contents:0': image_data})
        predictions = np.squeeze(predictions)
        # Creates node ID --> English string lookup.
        node_lookup = classifier.NodeLookup()
        top_k = predictions.argsort()[-self.use_top_k:][::-1]
        for node_id in top_k:
            human_string = node_lookup.id_to_string(node_id)
            score = predictions[node_id]
            if score > self.score_threshold:
                rospy.loginfo('%s (score = %.5f)' % (human_string, score))
                self._pub.publish(human_string)

    def main(self):
        rospy.spin()

if __name__ == '__main__':
    classifier.setup_args()
    rospy.init_node('rostensorflow')
    tensor = RosTensorFlow()
    tensor.main()
