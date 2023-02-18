#!/usr/bin/env python3

import sys
import shutil

if (len(sys.argv) <= 1):
	print("Usage:", sys.argv[0], "APPLICATION_ID")
	exit()

appAndroidTestRootPath = "./app/src/androidTest/java/"
templateId = "ilapin.template"
applicationId = sys.argv[1]

applcationIdParts = applicationId.split(".")
applicationIdBeginning = applicationIdParts[:-1]
applicationIdPathBeginning = "/".join(applicationIdBeginning)
applicationIdPathBeginning.mkdir(parents = True, exist_ok = True)
shutil.move(
	appAndroidTestRootPath + templateId.replace(".", "/"),
	appAndroidTestRootPath + applicationId.replace(".", "/")
)
