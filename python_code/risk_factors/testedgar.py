from edgar import Company, TXTML

company = Company("Oracle Corp", "0001341439")
#company = Company("INTERNATIONAL BUSINESS MACHINES CORP", "0000051143")
tree = company.get_all_filings(filing_type = '10-K')
docs = Company.get_documents(tree, no_of_documents=1)
#doc = company.get_10K()
text = TXTML.parse_full_10K(docs)

print (text)