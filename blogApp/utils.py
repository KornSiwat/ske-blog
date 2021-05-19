import uuid
import os
from os.path import splitext


def generate_newname(instance, filename):
    # Save original file name in model
    instance.original_file_name = filename

    # Get new file name/upload path
    base, ext = splitext(filename)
    newname = "%s%s" % (uuid.uuid4(), ext)

    return newname


def path_for_article_thumbnail(instance, filename):
    newname = generate_newname(instance, filename)

    return os.path.join("article/thumbnail/", newname)


def path_for_banner(instance, filename):
    newname = generate_newname(instance, filename)

    return os.path.join("banner/", newname)


def path_for_profile_pic(instance, filename):
    newname = generate_newname(instance, filename)

    return os.path.join("profile/profilepic/", newname)
