from lxml import etree, objectify

E = objectify.ElementMaker(annotate=False)
anno_tree = E.annotation(
    E.folder('ljy'),
    E.filename("ljy.jpg"),
    E.source(
        E.database('lala'),
        E.annotation('lala'),
        E.image('lala'),
        E.url("http://test.jpg")
    ),
    E.size(
        E.width(800),
        E.height(600),
        E.depth(3)
    ),
    E.segmented(0),
)

E2 = objectify.ElementMaker(annotate=False)
anno_tree2 = E2.object(
    E.name("person"),
    E.bndbox(
        E.xmin(100),
        E.ymin(200),
        E.xmax(300),
        E.ymax(400)
    ),
    E.difficult(0)
)
anno_tree.append(anno_tree2)

etree.ElementTree(anno_tree).write("text.xml", pretty_print=True)