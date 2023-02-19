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

def updateDirStructureUsingAppId(rootPath, placeholderAppId, appId):
	applicationIdParts = appId.split(".")
	applicationIdBeginning = applicationIdParts[:-1]
	applicationIdPathBeginning = "/".join(applicationIdBeginning)
	Path(rootPath + applicationIdPathBeginning).mkdir(parents = True, exist_ok = True)
	shutil.move(
		rootPath + placeholderAppId.replace(".", "/"),
		rootPath + appId.replace(".", "/")
	)

if (len(sys.argv) <= 1):
	print("Usage:", sys.argv[0], "APPLICATION_ID")
	exit()

appAndroidTestRootPath = "./app/src/androidTest/java/"
appTestRootPath = "./app/src/test/java/"
placeholderAppId = "ilapin.template"
applicationId = sys.argv[1]

#updateDirStructureUsingAppId(appAndroidTestRootPath, placeholderAppId, applicationId)
#updateDirStructureUsingAppId(appTestRootPath, placeholderAppId, applicationId)
shutil.move(
	appAndroidTestRootPath + placeholderAppId.replace(".", "/"),
	appAndroidTestRootPath + applicationId.replace(".", "/")
)
shutil.move(
	appTestRootPath + placeholderAppId.replace(".", "/"),
	appTestRootPath + applicationId.replace(".", "/")
)

appAndroidTestKtFiles = list(Path(appAndroidTestRootPath).rglob("*.kt"))
for filePath in appAndroidTestKtFiles:
	updateAppIdInFile(str(filePath), placeholderAppId, applicationId)

appTestKtFiles = list(Path(appTestRootPath).rglob("*.kt"))
for filePath in appTestKtFiles:
	updateAppIdInFile(str(filePath), placeholderAppId, applicationId)

updateAppIdInFile("./app/build.gradle", placeholderAppId, applicationId)
