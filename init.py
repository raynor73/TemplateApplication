#!/usr/bin/env python3

import sys
import shutil
import os
from pathlib import Path

def updateAppIdInFile(filePath, placeholderAppId, appId):
	file = open(filePath, "r", encoding="utf-8")
	fileContent = file.read()
	file.close()

	fileContent = fileContent.replace(placeholderAppId, appId)

	filePathOld = filePath + ".old"
	shutil.move(filePath, filePathOld)

	file = open(filePath, "w", encoding="utf-8")
	file.write(fileContent)
	file.close()

	os.remove(filePathOld)

if (len(sys.argv) <= 1):
	print("Usage:", sys.argv[0], "APPLICATION_ID")
	exit()

appAndroidTestRootPath = "./app/src/androidTest/java/"
templateId = "ilapin.template"
applicationId = sys.argv[1]

applicationIdParts = applicationId.split(".")
applicationIdBeginning = applicationIdParts[:-1]
applicationIdPathBeginning = "/".join(applicationIdBeginning)
Path(applicationIdPathBeginning).mkdir(parents = True, exist_ok = True)
shutil.move(
	appAndroidTestRootPath + templateId.replace(".", "/"),
	appAndroidTestRootPath + applicationId.replace(".", "/")
)

appAndroidTestKtFiles = list(Path(appAndroidTestRootPath).rglob("*.kt"))
for filePath in appAndroidTestKtFiles:
	updateAppIdInFile(filePath, templateId, applicationId)
