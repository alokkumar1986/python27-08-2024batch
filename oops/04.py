class HtmlDocument:
    extension = "html"
    version = 5


d = HtmlDocument()
print(d.extension) #Html
print(d.version)  #5


print(HtmlDocument.extension) #Html
print(HtmlDocument.version) #5

extension = getattr(HtmlDocument, 'extension')
print(extension) #Html

xyz = getattr(HtmlDocument, 'xyz', 'abcd')
print(xyz)

setattr(HtmlDocument, 'version', 10)
print(HtmlDocument.version)

delattr(HtmlDocument, 'version')
print(HtmlDocument.version)