#!/usr/bin/env python
## Author: Peter Meckiffe
## @ CERN, Meyrin
## September 27th 2011

from MaterialBudget.CMGTools.savannahBrowser import SavannahBrowser
from datetime import date
import types

class SavannahFormatter(object):
    def __init__(self, username, password, taskID, opts):
        self._savannahBrowser = SavannahBrowser(username,password, taskID)
        self._taskID=taskID
        self._opts = opts
        savOpts = self._savannahBrowser.getOpts()
        self.dict = {"Name": None, "Status": None, "LFN Castor Directory": None, "Castor Directory": None, "Parent Dataset": None, "Physics Group": None, "Date Created": None, "Created By": None, "Last Modified On": None, "Last Modified By":None, "Tags": None, "Root Files": None,"Error Files":None,"No. Files":None, "User Fields":""}
        for i in self._opts:
            if savOpts is not None:
            	if savOpts[i] is not None:
                	self._savannahBrowser.addOption(i, self._opts[i])
        
    def addMain(self, ProcDS, tags, files, castor, lfn):
        self.dict["Name"] = ProcDS['PathList'][0]
        if len(ProcDS['ParentList']) >0 :
            self.dict["Parent Dataset"] = ProcDS['ParentList'][0]
        if 'LastModificationDate' in ProcDS:
            self.dict["Last Modified On"] = date.fromtimestamp(int(ProcDS['LastModificationDate'])).strftime('%d-%m-%Y')
        if 'DateCreated' in ProcDS:
            self.dict["Date Created"] = date.fromtimestamp(int(ProcDS['DateCreated'])).strftime('%d-%m-%Y')
        if "PhysicsGroup" in ProcDS:
            self.dict["Physics Group"]= ProcDS['PhysicsGroup']
        if 'PrimaryDataset' in ProcDS and ProcDS['PrimaryDataset']['Name'] is not None:
            self.dict["Primary Dataset"] = ProcDS['PrimaryDataset']['Name']
        if ProcDS['TierList'] is not None:
            tiers = ""
            for i in ProcDS['TierList']:
                tiers += "\t"+i+"\n"
                self.dict["Tier List"] = tiers
        if "Status" in ProcDS:
            self.dict["Status"] = ProcDS['Status']
        if 'CreatedBy' in ProcDS:
            self.dict["Created By"] = ProcDS['CreatedBy']
        if 'LastModifiedBy' in ProcDS:
            self.dict["Last Modified By"] = ProcDS['LastModifiedBy']
        
        if tags is not None:    
            detailString = ""
            for i in tags:
                tag = tags[i]
                package = i
                detailString +="_"+tag+"_ - "+package +"\n"
            if detailString is not "":
            	self.dict['Tags']="\n"+detailString
        if files is not None:
            detailString=""
            for group in files:
                detailString +=group['name'] + "\n"
                if "missingFiles" in group:
                	detailString +="* Missing Files:\n"
                	for i in group["missingFiles"]: detailString+="** "+ i+"\n"
                if "duplicateFiles" in group:
                	detailString +="* Duplicate Files:\n"
                	for i in group["duplicateFiles"]: detailString+="** "+ i+"\n"
                if "qFiles" in group: detailString += "* No. of Files: " + str(group["qFiles"]) +"\n"
                detailString+="\n"
            self.dict['Root Files'] = "\n" +detailString
        if castor is not None:
            self.dict["Castor Directory"]="\n\t"+castor
        if lfn is not None:
            self.dict["LFN Castor Directory"]="\n\t"+lfn
    
    def _recursiveRead(self, string, input, tabs):
    	if input is None: return "\n"
    	if isinstance(input, int) or isinstance(input, float) or isinstance(input, str):
        	return tabs + " " + str(input)+"\n"
        	
    	elif type(input) is types.DictType :
    		if len(input.keys()) is 0:
    			return "\n"
    		for i in input:
    			if input[i] is not None:
    				string += tabs+"*"+i+"*: "+self._recursiveRead("", input[i], tabs)+"\n"
    		return "\n" + string
        elif type(input) is types.ListType or type(input) is types.TupleType:
        	if len(input) is 0:
        		return "\n"
        	for i in input:
        		
        		string += self._recursiveRead(string, i, tabs)+"\n"
        	return string
        
        elif type(input) is not types.ListType and type(input) is not types.TupleType:
        	if isinstance(input,str) and len(input) is 0:
        		return "\n"
        	else:
        		return tabs + " "+  str(input) 	+"\n"
        else:
        	return ""
        	
	
    def appendExtra(self, Extra):
        if self.dict['User Fields'] is not "":
        	formattedString = self.dict['User Fields']
        else:
        	formattedString = "\n"
        	self.dict['User Fields'] = ""
        self.dict['User Fields']+=self._recursiveRead("", Extra, "")+"\n"
        
    def publish(self):
        info = ""
        for i in self.dict:
        	if self.dict[i] is not None and len(self.dict[i])>0:
        		if i == 'User Fields':
        			info +=self.dict["User Fields"]+"\n"
        		else:
        			info +="*"+ i + "*: " + self.dict[i] +"\n"
        		info+="\n"
        if self._taskID is None:
            self._savannahBrowser.addOption("details", info)
        else: self._savannahBrowser.addOption("comment", info)
        return self._savannahBrowser.post(self._opts['assigned_to'])
            
