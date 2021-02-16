from edgar import Company, TXTML, XBRL, XBRLElement

company = Company("INTERNATIONAL BUSINESS MACHINES CORP", "0000051143")
doc = company.get_10K()
text = TXTML.parse_full_10K(doc)
print(text)

company = Company("Oracle Corp", "0001341439")
results = company.get_data_files_from_10K("EX-101.INS", isxml=True)
xbrl = XBRL(results[0])
XBRLElement(xbrl.relevant_children_parsed[15]).to_dict() #returns a dictionary of name, value, and schemaRef