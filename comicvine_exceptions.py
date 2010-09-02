#!/usr/bin/env python
#encoding:utf-8
#author:swc/Steve
#project:comicvine_api
#repository:http://github.com/swc/comicvine_api
#license:Creative Commons GNU GPL v2
# (http://creativecommons.org/licenses/GPL/2.0/)

"""Custom exceptions used or raised by comicvine_api
Modified from http://github.com/dbr/tvdb_api
"""

__author__ = "swc/Steve"
__version__ = "1.01"

__all__ = ["comicvine_error", "comicvine_userabort", "comicvine_seriesnotfound", "comicvine_issuenotfound", "comicvine_attributenotfound"]

class comicvine_exception(Exception):
    """Any exception generated by comicvine_api
    """
    pass

class comicvine_error(comicvine_exception):
    """An error with www.comicvine.com (Cannot connect, for example)
    """
    pass

class comicvine_userabort(comicvine_exception):
    """User aborted the interactive selection (via
    the q command, ^c etc)
    """
    pass

class comicvine_seriesnotfound(comicvine_exception):
    """Series cannot be found on www.comicvine.com (non-existant series)
    """
    pass

class comicvine_issuenotfound(comicvine_exception):
    """Issue cannot be found on www.comicvine.com
    """
    pass

class comicvine_attributenotfound(comicvine_exception):
    """Raised if an issue does not have the requested
    attribute (such as a issue name)
    """
    pass
