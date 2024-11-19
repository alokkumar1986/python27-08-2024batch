class HtmlDocument:
    extension = "html"
    version = 5


d = HtmlDocument()
print(d.extension)
print(d.version)


print(HtmlDocument.extension)
print(HtmlDocument.version)

extension = getattr(HtmlDocument, 'extension')
print(extension)

xyz = getattr(HtmlDocument, 'xyz', 'abcd')
print(xyz)

setattr(HtmlDocument, 'version', 10)
print(HtmlDocument.version)

delattr(HtmlDocument, 'version')
print(HtmlDocument.version)