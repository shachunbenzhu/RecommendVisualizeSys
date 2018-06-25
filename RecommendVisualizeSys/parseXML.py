# coding=utf-8

# 通过解析xml文件
'''
try:
    import xml.etree.CElementTree as ET
except:
    import xml.etree.ElementTree as ET
'''
import xml.etree.ElementTree as ET
import os
import sys

# 遍历xml文件
def traverseXml(element):
    # print (len(element))
    if len(element) > 0:
        for child in element:
            print(child.tag, "----", child.attrib)
            traverseXml(child)
            # else:
            # print (element.tag, "----", element.attrib)


if __name__ == "__main__":
    xmlFilePath = os.path.abspath("les-miserables-test.gexf")
    print(xmlFilePath)

    ET.register_namespace('', "http://www.gexf.net/1.2draft")
    ET.register_namespace('viz', "http://www.gexf.net/1.2draft/viz")
    ET.register_namespace('xsi', "http://www.w3.org/2001/XMLSchema-instance")

    try:
        tree = ET.parse(xmlFilePath)
        print("tree type:", type(tree))

        # 获得根节点
        root = tree.getroot()
    except Exception as e:  # 捕获除与程序退出sys.exit()相关之外的所有异常
        print("parse test.xml fail!")
        sys.exit()
    #print("root type:", type(root))
    #print(root.tag, "----", root.attrib)

    # 遍历root的下一层
    #for child in root:
    #    print("遍历root的下一层", child.tag, "----", child.attrib)

    print(20 * "*")
    # 遍历xml文件
    traverseXml(root)
    print(20 * "*")

    # 根据标签名查找root下的所有标签
    captionList = root.findall("node")  # 在当前指定目录下遍历
    print(len(captionList))
    for caption in captionList:
        caption.set("label", "999999")
    tree.write("les-miserables-test.gexf", encoding="utf-8",xml_declaration=True)
