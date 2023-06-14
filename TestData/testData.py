import os
# present working directory
file_location = os.path.dirname(os.path.realpath(__file__))
firstfile = f"{file_location}\diabetes1.pdf"
# to convert the path to the correct format for the operating system
firstfile = os.path.normpath(firstfile)
secondfile = f"{file_location}\diabetes2.pdf"
secondfile = os.path.normpath(secondfile)
# drag file path
drag_file = f"{file_location}\cancer.pdf"
drag_file = os.path.normpath(secondfile)


firstDraftGenPageData = {

    "topic": "how to treat diabetes?",
    "tone": "professional",
    "reading_level": "postgraduate",
    "online_source1": "https://my.clevelandclinic.org/health/diseases/7104-diabetes",
    "online_source2": "https://www.endocrine.org/patient-engagement/endocrine-library/diabetes-treatments",
    "file_path1": firstfile,
    "file_path2": secondfile,
    "drag_file_path": drag_file

}

rephraserPageData = {

    "upload_url": "https://my.clevelandclinic.org/health/diseases/7104-diabetes",
    "tone": "professional",
    "reading_level": "postgraduate"

}
